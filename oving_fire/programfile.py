import tekstanalyse


class main:
    f = tekstanalyse.FileHandler()
    stop_words = f.make_list_from_file('./data/stop_words.txt')
    positive_filepaths = f.make_filepath_list('./data/subset/train/pos/')
    negative_filepaths = f.make_filepath_list('./data/subset/train/neg/')

    data = tekstanalyse.DataSet(positive_filepaths, negative_filepaths)
    data.make_words_from_filepaths(n_grams=1)
    data.remove_words(stop_words)
    data.calculate_popularity()
    data.prune(2)
    data.make_vocabulary()
    data.calculate_info_value()

    print("Setup completed!")
    print(sorted(data.positive_words.values()))
    print(sorted(data.negative_words.values()))

    for string in data.vocabulary:
        if string not in data.positive_words.keys():
            print(string, 'not in positive words!')
    for string in data.vocabulary:
        if string not in data.negative_words.keys():
            print(string, 'not in negative words!')

    print('Testing negatives...')
    negatives = 0
    positives = 0
    filepaths = f.make_filepath_list('./data/subset/test/neg/')
    for filepath in filepaths:
        if data.evalute_review(filepath) == 'positive':
            positives += 1
        else:
            negatives += 1
    print('Positives:', positives)
    print('Negatives:', negatives)
    print('Correct:', str((negatives/len(filepaths) * 100)) + '%')


    print('Testing positives...')
    negatives = 0
    positives = 0
    positive_filepaths = f.make_filepath_list('./data/subset/test/pos/')
    for filepath in positive_filepaths:
        if data.evalute_review(filepath) == 'positive':
            positives += 1
        else:
            negatives += 1
    print('Positives:', positives)
    print('Negatives:', negatives)
    print('Correct:', str((positives/len(filepaths) * 100)) + '%')
