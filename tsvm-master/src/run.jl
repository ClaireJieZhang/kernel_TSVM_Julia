using ArgParse
include("TSVM.jl")
using TSVM
include("utils.jl")
using utils
using DataStructures
using NPZ

function parse_commandline()
    s = ArgParseSettings()
    @add_arg_table s begin
        "datafile"
            help = "file where data is kept"
            required = true
        "--c"
            help = "penalty weighting for training examples"
            arg_type = Float64
            default = 0.25
        "--cstar"
            help = "penalty weighting for test examples"
            arg_type = Float64
            default = 0.1
    end
    return parse_args(s)
end

function evaluate(predictions, labels)
    correct = 0
    for i in 1:length(predictions)
        if predictions[i] == labels[i]
            correct += 1
        end
    end
    return correct / length(predictions)
end

function calculate_positive_percentage(predictions, data, test_ids, non_minority_p_num, minority_p_num)

    for i in 1:length(test_ids)
        if data.features[test_ids[i]][1]==1 && predictions[i]==1
            non_minority_p_num+=1
        end
        if data.features[test_ids[i]][1]==-1 && predictions[i]==1
            minority_p_num+=1
        end
    end
    return non_minority_p_num, minority_p_num
end

function one_cross_validation(data,k,randorder, c, cstar)
    takeoutsize = trunc(Int, 400 / k)
    testids = collect(501:1500)
    trainids = randorder[takeoutsize+1:end]
    cross_val_ids=randorder[1:takeoutsize]
    predictions, error = train_tsvm(
        trainids,
        testids,
        cross_val_ids,
        data,
        c,
        cstar,
        false)
    return error
end

function cross_val_label_data(data, k, randorder, c, cstar)
    testids = collect(3001:9000)
    results = []
    takeoutsize = trunc(Int, 3000 / k)
    trainids = randorder[takeoutsize+1:end]
    cross_val_ids=randorder[takeoutsize/2:takeoutsize]
    predictions, num_plus_in_svm, error = train_svm(
        trainids,
        testids,
        cross_val_ids,
        data,
        c,
        cstar,
        false)
    println("SVM ERROR1")
    println(error)
    #predictions, error = train_tsvm(
    #    trainids,
    #    testids,
    #    cross_val_ids,
    #    data,
    #    c,
    #    cstar,
    #    false)
    #println("TSVM ERROR1")
    #println(error)
    for i in 2:k-1
        trainids = randorder[1:takeoutsize*(i-1)]
        cross_val_ids=randorder[(takeoutsize*(i-1)+1):(takeoutsize*(i))]
        append!(trainids, randorder[(takeoutsize*(i)+1):end])
        predictions, num_plus_in_svm, error = train_svm(
            trainids,
            testids,
            cross_val_ids,
            data,
            c,
            cstar,
            false)
        println("SVM ERROR")
        println(error)
    #    predictions, error = train_tsvm(
    #            trainids,
    #            testids,
    #            cross_val_ids,
    #            data,
    #            c,
    #            cstar,
    #            false)
    #    println("TSVM ERROR")
    #    println(error)
    end
    trainids = randorder[1:(takeoutsize*(k-1))]
    cross_val_ids=randorder[(takeoutsize*(k-1)+1):end]
    predictions, num_plus_in_svm, error = train_svm(
        trainids,
        testids,
        cross_val_ids,
        data,
        c,
        cstar,
        false)
    println("SVM ERROR")
    println(error)
    #predictions, error = train_tsvm(
    #    trainids,
    #    testids,
    #    cross_val_ids,
    #    data,
    #    c,
    #    cstar,
    #    false)
    #println("TSVM ERROR")
    #println(error)
end



function cross_val(data, k, c, cstar)
    if k < 4
        k = 4
    end
    cross_val_iter=1
    results = []
    randorder = shuffle(collect(1:length(data.features)))
    testsize = trunc(Int, length(data.features) / k)
    trainids = randorder[testsize+1:end]
    testids = randorder[1:testsize]
    predictions = train_tsvm(
        trainids,
        testids,
        data,
        c,
        cstar,
        false)

    non_minority_p_num=0
    minority_p_num=0
    non_minority_p_num, minority_p_num = calculate_positive_percentage(predictions, data, randorder[1:testsize], non_minority_p_num, minority_p_num)
    println("cross_val_iter:")
    println(cross_val_iter)
    println("non_minority_p_num")
    println(non_minority_p_num)
    println("minority_p_num")
    println(minority_p_num)

    push!(
        results, evaluate(predictions, data.labels[randorder[1:testsize]]))
    for i in 2:k-1
        cross_val_iter+=1
        println("cross_val_iter:")
        println(cross_val_iter)
        trainids = randorder[1:testsize*(i-1)]
        append!(trainids, randorder[(testsize*(i)+1):end])
        testids = randorder[(testsize*(i-1)+1):(testsize*(i))]
        predictions = train_tsvm(
            trainids,
            testids,
            data,
            c,
            cstar,
            false)
        non_minority_p_num, minority_p_num = calculate_positive_percentage(predictions, data, testids, non_minority_p_num, minority_p_num)
        println("non_minority_p_num")
        println(non_minority_p_num)
        println("minority_p_num")
        println(minority_p_num)
        push!(results, evaluate(predictions, data.labels[testids]))
    end
    trainids = randorder[1:(testsize*(k-1)+1)]
    testids = randorder[(testsize*(k-1)+1):end]
    predictions = train_tsvm(
        trainids,
        testids,
        data,
        c,
        cstar,
        false)

    non_minority_p_num, minority_p_num = calculate_positive_percentage(predictions, data, testids, non_minority_p_num, minority_p_num)
    cross_val_iter+=1
    println("cross_val_iter:")
    println(cross_val_iter)
    println("non_minority_p_num")
    println(non_minority_p_num)
    println("minority_p_num")
    println(minority_p_num)

    push!(results, evaluate(
        predictions, data.labels[randorder[(testsize*(k-1)+1):end]]))
    return results, non_minority_p_num, minority_p_num
end

function small_test(data, k, c, cstar)
    println("in small_test")
    println("length of data features")
    println(length(data.features))
    #lenth(data.features) will return how many data points
    trainsize = convert(Integer, ceil(0.7 * length(data.features)))
    println("trainsize")
    println(trainsize)
    results = []
    for _ in 1:k
        randorder = shuffle(collect(1:length(data.features)))
        predictions = train_svm(
            #trainset
            randorder[1:trainsize],
            #testset
            randorder[trainsize+1:end],
            data,
            c,
            cstar,
            true
        )
        println("data.labels[randorder[trainsize+1:end]]")
        println(data.labels[randorder[trainsize+1:end]])
        println("length(predictions)")
        println(length(predictions))
        push!(results, evaluate(
            predictions, data.labels[randorder[trainsize+1:end]]))
    end
    return results
end


function one_tsvm(trainids, testids, data, c, cstar, num_plus, debug, sigma)
    predictions = train_tsvm(trainids,testids,data,c,cstar,num_plus, debug, sigma)

    #non_minority_p_num=0
    #minority_p_num=0
    #println("TSVM error")
    #println(error)
    #non_minority_p_num, minority_p_num = calculate_positive_percentage(predictions, data, testids, non_minority_p_num, minority_p_num)

    error=0
    test_labels = data.labels[testids]
    for i in 1:length(test_labels)
        if predictions[i]!=test_labels[i]
            error+=1
        end
    end

    return error
end

function one_svm(data, c, cstar)
    trainids = collect(1:479)
    testids = collect(480:1479)
    predictions, num_plus_in_svm, error = train_svm(
        trainids,
        testids,
        data,
        c,
        cstar,
        false)

    non_minority_p_num=0
    minority_p_num=0
    println("SVM error")
    println(error)
    non_minority_p_num, minority_p_num = calculate_positive_percentage(predictions, data, testids, non_minority_p_num, minority_p_num)
    #npzwrite("svm-predictions.npz", predictions)
    return non_minority_p_num, minority_p_num, error
end



function main()
    parsed_args = parse_commandline()
    data = get_data(parsed_args["datafile"])

    ids=shuffle(collect(1:863))

    trainids = collect(i for i in 1:length(data.labels) if data.labels[i]!=0)
    testids= collect(i for i in 1:length(data.labels) if data.labels[i]==0)

    #predictions = train_svm(
    #    trainids, testids, data, 2000000, 1, 131, false, 1)

    #test_labels=data.labels[testids]
    #error=0
    #for i in 1:length(predictions)
    #    if predictions[i]!=test_labels[i]
            #println(results[i])
            #println("test_labels[i]")
            #println(test_labels[i])
    #        error+=1
    #    end
    #end

    #println("###################SVM RESULT#########################")
    #println(predictions)
    #println("###################SVM ERROR#########################")
    #println(error)

    tsvm_error=one_tsvm(trainids, testids, data, 2000000, 2000000, 371, true, 1)

    println("################### TSVM ERROR#########################")
    println(tsvm_error)

    #randorder = shuffle(trainids)
    #npzwrite("random_order.npz", randorder)
    #randoreder=npzread("random_order.npz")
    #error_accumulator=0
    #for i in 1: 100
    #    randorder = shuffle(trainids)
    #    error_accumulator = error_accumulator+one_cross_validation(data,k,randorder, 1.0, 4.0)
    #end
    #println("error")
    #println(error_accumulator/100)

    #cross_val_label_data(data, k, randorder, parsed_args["c"], parsed_args["cstar"])
    #results, non_minority_p_num, minority_p_num = cross_val(data, k, parsed_args["c"], parsed_args["cstar"])
    #non_minority_p_num, minority_p_num, error = one_svm(data, parsed_args["c"], parsed_args["cstar"])
    #non_minority_p_num, minority_p_num, error= one_tsvm(data, parsed_args["c"], parsed_args["cstar"])
    #resultrs = small_test(data, k, parsed_args["c"], parsed_args["cstar"])
    #println(results)
    #println(sum(results)/k)
    #println("non_minority_p_num")
    #println(non_minority_p_num)
    #println("minority_p_num")
    #println(minority_p_num)
    #println("error")
    #println(error)

end

main()
