from model import model
import sys

config = dict()

def open_file_train_dataset(file):
    global attributes, dataset, X

    attributes = dict()
    dataset = dict()
    X = []

    with open(file) as fp:
        line = fp.readline()

        firstLine = True
        while line:
            if firstLine:
                #ako je prva linija
                firstLine = False
                values = line.strip().split(',')

                for val in values:
                    dataset[val] = []
                    X.append(val)
                line = fp.readline()
                continue
            #ako je neprva linija
            values = line.strip().split(',')
            for i, val in enumerate(values):
                dataset[X[i]].append(val)
            line = fp.readline()


        #region v(x) structure
        for feature in dataset.keys():
            attributes[feature] = set(dataset[feature])
        #endregion

def open_file_test_dataset(file):
    global dataset, X, y

    dataset = list()
    X = []
    y = []

    with open(file) as fp:
        line = fp.readline()

        firstLine = True
        while line:
            if firstLine:
                # ako je prva linija
                firstLine = False

                for attr in line.strip().split(','):
                    X.append(attr)
                line = fp.readline()
                continue
            # ako je neprva linija

            values = line.strip().split(',')
            new_sample = dict()
            for i, val in enumerate(values):
                new_sample[X[i]] = val
            y.append(values[-1])        #pretpostavlja se da je zadnja rijec labela
            dataset.append(new_sample)
            line = fp.readline()

def open_file_config(file):
    global config

    #region config instantiation
    config['mode'] = 'test'
    config['model'] = 'id3'
    config['max_depth'] = -1
    config['num_trees'] = 1
    config['feature_ratio'] = 1.
    config['example_ratio'] = 1.
    #endregion

    with open(file) as fp:
        line = fp.readline()
        while line:
            configValues = line.strip().split('=')
            config[configValues[0]] = configValues[1]
            line = fp.readline()

def read_argv(argv):
    global Test_file, Train_file, Config_file
    Train_file = argv[1]
    Test_file = argv[2]
    Config_file = argv[3]

#stavi si train_dataset i test_dataset
if __name__ == "__main__":
    read_argv(sys.argv)

    open_file_config(Config_file)

    #region ucenje
    open_file_train_dataset(Train_file)

    id3 = model(config, attributes, columns=X, hyperParam=config['max_depth'])
    learning_output = id3.fit(dataset)

    print(learning_output)
    #endregion

    #region testiranje
    open_file_test_dataset(Test_file)

    testing_output = id3.predict(dataset)
    print(testing_output)
    #endregion

    #region accuracy i confusion matrix
    y_real = y
    y_predicted = testing_output.strip().split(' ')
    y_set = sorted(list(set(y)))

    #accuracy
    correct=0
    for i in range(len(y_real)):
        if y_real[i] == y_predicted[i]:
            correct += 1
    accuracy = correct / len(y_real)
    print(str(round(accuracy, 5)))

    #instantiate confusion matrix
    confusion_matrix = list()
    for i in range(len(y_set)):
        row = list()
        for j in range(len(y_set)):       #iako je dulj(y_real)==dulj(y_predicted) uvijek
            row.append(0)
        confusion_matrix.append(row)

    #fill up confusion matrix
    for i in range(len(y_real)):
        i1 = y_set.index(y_real[i])
        i2 = y_set.index(y_predicted[i])
        confusion_matrix[i1][i2] += 1

    #print confusion matrix
    confusion_matrix_output = ""
    for i, row in enumerate(confusion_matrix):
        for j, _ in enumerate(row):
            confusion_matrix_output += str(confusion_matrix[i][j]) + " "
        confusion_matrix_output = confusion_matrix_output[:-1] + "\n"
    confusion_matrix_output = confusion_matrix_output[:-1]
    print(confusion_matrix_output)
    #endregion



