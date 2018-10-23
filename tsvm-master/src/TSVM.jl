module TSVM

using JuMP
using Ipopt
using DataStructures
using NPZ
export TSVMData, svm_dual_predict, solve_svm_qp_dual, train_svm, train_tsvm

type TSVMData
     features
     labels
end

function constrain_vectors!(m, y, w, x, b, xi)
    for i in 1:length(x)
        @constraint(m, (y[i] * (dot(w, x[i]) + b)) >= (1 - xi[i]))
        @constraint(m, xi[i] >= 0)
    end
end

function initialize_vars!(v, val)
    for i in 1:length(v)
        setvalue(v[i], val)
    end
end


function RBF(x, y, sigma)
    Ke=exp(-(norm(x-y)^2)/sigma)
    return Ke
end

function linear_kernel(x, y)
    Ke=dot(x, y)
    return Ke
end


function solve_svm_qp_dual(training_features,
                            training_labels,
                            test_features,
                            test_predictions,
                            C,
                            C_star_minus,
                            C_star_plus, sigma)

    num_points=length(training_features)
    #create a n*n matrix
    K=zeros(num_points, num_points)
    for i in 1:num_points
        for j in 1:num_points
            K[i,j]=RBF(training_features[i], training_features[j], sigma)
        end
    end
    m = Model(solver=IpoptSolver(
        print_level=0))
    @variable(m,alpha[1:num_points])
    initialize_vars!(alpha, 0)
    one_matrix=ones(size(alpha))

    #ksi, currently not used in dual
    #@variable(m, m_training_margin[1:length(training_labels)])
    for i in 1:num_points
        @constraint(m, alpha[i]<=C)
        @constraint(m, alpha[i]>=0)
    end
    @constraint(m, dot(alpha, training_labels)==0)

    @objective(m, Max, -0.5*transpose((alpha.*training_labels))*K*(alpha.*training_labels) + dot(one_matrix, alpha))
    status = solve(m)
    if status != :Optimal
        println("NOT OPTIMAL!")
    end
    has_b=false
    ind=0
    #To calculate b we pick an arbitrary support vector
    for i in 1:length(alpha)
        if (getvalue(alpha[i])>=C*0.00001 && getvalue(alpha[i])<= C*(1-0.00001))
            ind=i
            has_b=true
            break
        end
    end

    if (has_b)
        b=training_labels[ind]-dot(getvalue(alpha), training_labels.*K[:,ind])
    else
        b=0
    end

    return [getvalue(alpha[i]) for i in 1:length(alpha)], b
end

function svm_dual_predict(one_data,
        alpha, b, training_features,
        training_labels, sigma)
    #Given the optimal dual variables of the SVM problem, the bias,
    #the training data, the training labels and a data point x, it
    #calculates the margin for x
    m = length(alpha)
    prod = zeros(m, 1)
    for i in 1: m
        prod[i]=RBF(one_data, training_features[i], sigma)
        #prod[i]=linear_kernel(one_data, training_features[i])
    end
    margin= b + dot(alpha, training_labels.*prod)
    return margin
end

function calculate_pos_neg_index(test_predictions)
    pos = zeros(Int64, 0)
    neg = zeros(Int64, 0)
    for i in 1:length(test_predictions)
        if test_predictions[i]==1
            append!(pos, i)
        else
            append!(neg, i)
        end
    end
    return pos, neg
end


function solve_tsvm_qp_dual(training_features,training_labels, test_features, test_predictions,
                            C, C_star_minus, C_star_plus, sigma)
        #ksi test, not currently used in dual
        #@variable(m, m_test_margin[1:length(test_predictions)])

        test_pos_index,test_neg_index=calculate_pos_neg_index(test_predictions)
        println("length(test_pos_index)")
        println(length(test_pos_index))
        println("length(test_neg_index)")
        println(length(test_neg_index))

        num_train_points=length(training_features)
        test_pos_index.+=num_train_points
        test_neg_index.+=num_train_points
        num_test_points=length(test_features)
        total_num=num_train_points+num_test_points
        #create a n*n matrix
        total_features=vcat(training_features, test_features)
        total_labels=vcat(training_labels, test_predictions)

        K=zeros(total_num, total_num)
        for i in 1:total_num
            for j in 1:total_num
                K[i,j]=RBF(total_features[i], total_features[j], sigma)
            end
        end
        m = Model(solver=IpoptSolver(print_level=0))
        @variable(m,alpha[1:total_num])
        initialize_vars!(alpha, 0)
        one_matrix=ones(size(alpha))
        #ksi, currently not used in dual
        for i in 1:num_train_points
            @constraint(m, alpha[i]<=C)
            @constraint(m, alpha[i]>=0)
        end
        #need update of index to distinguish between c+ and c-
        for i in 1: num_test_points
            @constraint(m, alpha[num_train_points+i]>=0)
        end

        for i in 1:length(test_pos_index)
            alphaindex=test_pos_index[i]
            @constraint(m, alpha[alphaindex]<=C_star_plus)
        end

        for i in 1:length(test_neg_index)
            alphaindex=test_neg_index[i]
            @constraint(m, alpha[alphaindex]<=C_star_plus)
        end

        @constraint(m, dot(alpha, total_labels)==0)
        @objective(m, Max, -0.5*transpose((alpha.*total_labels))*K*(alpha.*total_labels) + dot(one_matrix, alpha))
        status = solve(m)
        if status != :Optimal
            println("NOT OPTIMAL!")
        end
        has_b=false
        ind=0
        #To calculate b we pick an arbitrary support vector
        for i in 1:length(alpha)
            if (getvalue(alpha[i])>=C*0.00001 && getvalue(alpha[i])<= C*(1-0.00001))
                ind=i
                has_b=true
                break
            end
        end
        if (has_b)
            b=training_labels[ind]-dot(getvalue(alpha), total_labels.*K[:,ind])
        else
            b=0
        end

        all_ksi=calculate_ksi([getvalue(alpha[i]) for i in 1:length(alpha)], b, total_features, total_labels, sigma)
        ksi_labeled=all_ksi[1:num_train_points]
        ksi_unlabeled=all_ksi[num_train_points+1: length(all_ksi)]
        return [getvalue(alpha[i]) for i in 1:length(alpha)], b, ksi_labeled, ksi_unlabeled
end

#given y_i and f(x_i), calculate ksi. #note, ksi is calculated along with each optimization,
#i.e. each time alpha, b are solved, with given c, we can calculate ksi corresponding to this optimization result
function calculate_ksi(alpha, b, all_features, all_labels, sigma)
    predictions=zeros(length(all_labels))
    for i in 1:length(predictions)
        predictions[i]=svm_dual_predict(all_features[i], alpha, b, all_features, all_labels, sigma)
    end

    ksi=zeros(length(all_labels))
    for i in 1:length(ksi)
        ksi[i]=1-all_labels[i]*predictions[i]
    end
    return ksi
end

function compute_fraction(data, trainids)
    return sum(ones(length(trainids)) .* (data.labels[trainids] .== 1)) /
        length(trainids)
end


function train_svm(training_ids,test_ids,data,c,c_star,num_plus,debug,sigma)
    training_features = data.features[training_ids]
    training_labels = data.labels[training_ids]
    (alpha, b) = solve_svm_qp_dual(training_features,
                                training_labels,[],[],c,0, 0, sigma)
    test_features = data.features[test_ids]
    test_labels=data.labels[test_ids]
    result=zeros(length(test_ids))
    for i in 1:length(test_ids)
        result[i]=svm_dual_predict(test_features[i], alpha, b, training_features, training_labels, sigma)
    end
    results=classify_num_plus(result, num_plus)
    return results
end

function classify(margins)
    error=0
    result_convert=[result[i]>=0 for i in 1:length(result)]
    results=zeros(length(result))
    for i in 1:length(result_convert)
        if result_convert[i]==true
            results[i]=1
        else
            results[i]=-1
        end
    end
    for i in 1:length(results)
        if results[i]!=test_labels[i]
            #println(results[i])
            #println("test_labels[i]")
            #println(test_labels[i])
            error+=1
        end
    end
    return results, error
end

function classify_num_plus(raw_results, num_plus)
    index_result = collect(enumerate(raw_results))
    sorted_result = sort(index_result, by = x -> x[2])
    best_indices = collect(sorted_result[i][1] for i in length(raw_results)-num_plus+1:length(raw_results))
    results = -1*ones(Int64, length(raw_results))
    results[best_indices] = 1
    return results
end

#find indexes to swap
function find_problems(
        predictions::Vector{Int64}, xi_star::Vector{Float64}, swapped_dict)
    index1 = -1
    index2 = -1
    found_problem = false
    for i in 1:(length(predictions)-1)
        for j in (i+1):length(predictions)
            if ((predictions[i] * predictions[j] < 0) && (xi_star[i] > 0) &&
                    (xi_star[j] > 0) && (xi_star[i] + xi_star[j] > 2)) &&
                    (get(swapped_dict, (i,j), 0) < 10)
                swapped_dict[(i,j)] = get(swapped_dict, (i,j), 0) + 1
                index1 = i
                index2 = j
                found_problem = true
            end
        end
        if found_problem
            break
        end
    end
    return (index1, index2)
end

function train_tsvm(training_ids,test_ids,data,c,c_star,num_plus,debug,sigma)
    predictions=train_svm(training_ids,test_ids,data,c,c_star,num_plus,debug,sigma) # error is not useful
    training_features = data.features[training_ids]
    training_labels = data.labels[training_ids]
    test_features = data.features[test_ids]
    #c_star_minus=10^-5.0
    #c_star_plus=10^-5.0*num_plus/(length(test_ids)-num_plus)
    c_star_minus=1
    c_star_plus=1*num_plus/(length(test_ids)-num_plus)

    count = 1
    while (c_star_minus < c_star) || (c_star_plus < c_star)
        (alpha, b, xi, xi_star) =
        solve_tsvm_qp_dual(training_features, training_labels,
            test_features, predictions, c, c_star_minus,c_star_plus, sigma)
        if debug
            message = "Iteration: $(count)"
            println(message)
            print_report(
                message, predictions, alpha, b, xi, xi_star)
            count += 1
        end
        continue_refinement = true
        swapped_dict = Dict()
        swapped_iter = 0
        while continue_refinement && (swapped_iter < 50)
            println("in swap iter loop")
            swapped_iter += 1
            #(index1, index2) = find_problems_fair1(test_features, predictions, xi_star, swapped_dict)
            #(index1, index2) = find_problems_fair2(test_features, predictions, xi_star, swapped_dict, w, b, 0.3)
            (index1, index2) = find_problems(predictions, xi_star, swapped_dict)
            println("index1, index2")
            println(index1, index2)
            if (index1 != -1) && (index2 != -1)
                if debug
                    println("#### Sum: $(xi_star[index1] + xi_star[index2])")
                    print_problems(index1, index2, xi_star)
                end
                predictions[index1] = -1*predictions[index1]
                predictions[index2] = -1*predictions[index2]
                (alpha, b, xi, xi_star) = solve_tsvm_qp_dual(training_features, training_labels,
                    test_features, predictions, c, c_star_minus,c_star_plus, sigma)
                #println("w, b after swapping")
                #println(w, b)
                if debug
                    message = "Iteration: $(count)\nSwapped $(index1) and $(index2)"
                    println(message)
                    print_report(
                        message, predictions, alpha, b, xi, xi_star)
                    count += 1
                end
            else
                continue_refinement = false
            end
        end
        c_star_minus = min(c_star_minus*2, c_star)
        c_star_plus = min(c_star_plus*2, c_star)
        if debug
            print_cstars(c_star_plus, c_star_minus)
        end
    end
    return predictions
end










function objective_f(w, C, xi, C_star_minus, C_star_plus, xi_star)
    return 0.5 * dot(w, w) + C * sum(xi) +
        C_star_minus * sum(xi_star .* (xi_star .== -1)) +
        C_star_plus * sum(xi_star .* (xi_star .== 1))
end



function print_report(
        message, predictions, w, b, xi, xi_star)
    println("########################################")
    println("$(message)")
    println("predictions:\t$(predictions)")
    println("weights:\t$(w)")
    println("bias:\t$(b)")
    println("training penalties:\t$(xi)")
    println("testing penalties:\t$(xi_star)")
    println("#--------------------------------------#")
end

function print_cstars(c_star_plus, c_star_minus)
    println("CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC")
    println("\tC_star_plus:\t$(c_star_plus)")
    println("\tC_star_minus:\t$(c_star_minus)")
    println("C**************************************C")
end

function print_problems(index1, index2, xi_star)
    println("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
    println("\tindex1:\t$(index1)\t$(xi_star[index1])")
    println("\tindex2:\t$(index2)\t$(xi_star[index2])")
    println("I**************************************I")
end

end
