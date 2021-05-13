from Node import Node
from math import log2

class model:
    def __init__(self, config, attributes, columns, hyperParam):
        self.depth = hyperParam
        self.config = config
        self.attributes = attributes
        self.columns = columns

    #region fit functions

    #ovo ode isto ako ima vise max-ova mora vratit onaj koji je prvi abecedno
    #kao arg mu posalji listu
    def argmax(self, y):

        #prima argument kao listu i vrati onaj koji se pojavljuje najcesce (ili abecedno ako ih je vise) npr y = [DA, NE, DA]
        frequencies = {a: y.count(a) for a in y}  # npr frequencies = {DA:2, NE:1}
        max_frequency = max(frequencies, key=frequencies.get)  # npr max_frequency = DA

        for yy in frequencies.keys():
            if frequencies[yy] == frequencies[max_frequency] and yy < max_frequency:
                max_frequency = yy

        return max_frequency     #vraca najcesci element u 'clas'

    #uzima se prvi po redu, ali nije bitno koji je to koji je prvi, jer sve znacajke imaju isti broj vrijednosti znacajki
    def D_size(self, D):
        for (key, val) in D.items():
            return len(val)

    def information_gain(self, D, X, y):
        inf_gains = dict()
        samples_size = self.D_size(D)

        #za gornji E
        # optimizacija moze bit da pamti ovaj E gornji
        labels = y  # npr vals = [DA,NE,DA]    jer y.keys()[0] je odbojka?
        frequencies = {a: labels.count(a) for a in labels}  # npr frequencies = {DA:2, NE:1}

        max_frequency = self.argmax(y) #npr max_frequency = DA

        for x in X:    #negleda za label-ove (samo features)
            #za gornji E
            E = 0
            for f in frequencies.values():
                E -= f / samples_size * log2(f / samples_size)

            counter = dict()
            counter_denom = dict()

            for i in range(samples_size):
                if (D[x][i], y[i]) not in counter.keys():    #svaki put doda novo
                    counter[(D[x][i], y[i])] = 1
                else:
                    counter[(D[x][i], y[i])] += 1

                if D[x][i] not in counter_denom.keys():
                    counter_denom[D[x][i]] = 1
                else:
                    counter_denom[D[x][i]] += 1

            for (key, count) in counter.items():
                denom_key = key[0]
                E += count / counter_denom[denom_key] * log2(count / counter_denom[denom_key]) * counter_denom[denom_key] / samples_size

            inf_gains[x] = E

        #racunanje max-a od information gainsova
        max_feature = max(inf_gains, key = inf_gains.get)

        #ako je vise maxova isto, neka vraca abecedno
        for x in X:
            if inf_gains[x] == inf_gains[max_feature] and x < max_feature:
                max_feature = x

        return max_feature, max_frequency

    def dict_deepcopy(self, D):
        DD = dict()
        for (key, val) in D.items():
            DD[key] = val.copy()
        return DD

    def remove_sample(self, Dx, filter, y):
        feature = filter[0]
        feature_value = filter[1]

        #kopiraj dict u novi
        D = self.dict_deepcopy(Dx)
        y = list(y)

        indexes_to_remove = []
        samples_size = len(D[feature])
        for i in range(samples_size):
            if D[feature][i] != feature_value:      #npr vrijeme!=suncano za ovaj i
                indexes_to_remove.append(i)

        for i in sorted(indexes_to_remove, reverse=True):
            for (_, vals) in D.items():  # u svakoj listi D-a izbrisi ovaj i
                vals.pop(i)
            y.pop(i)

        return D, y

    def uniform_decision(self, y):      #TRUE ako su svi elementi liste isti
        return len(set(y)) == 1

    def id3(self, D, Dparent, X, y, yparent, depth):
        if self.D_size(D) == 0:           #or y is empty
            #sta ovo radiii

            v = self.argmax(yparent)
            return Node(v)
        v = self.argmax(y)
        if len(X) == 0 or self.uniform_decision(y) or int(depth) == int(self.depth):       #ovaj desno od 'and' je samo da neudje u prvoj iteraciji; ovaj depth je za 4.zad
            return Node(v)
        x, highest_final_class_label = self.information_gain(D, X, y)
        subtrees = []

        X.remove(x)
        for v in self.attributes[x]:
            Dx, yx = self.remove_sample(D, (x, v), y)

            t = self.id3(Dx, D, list(X), yx, y, depth+1)

            subtrees.append((v, t)) #npr (suncano, Node1)  (oblacno, Node2)  (kisno, Node3)
        return Node(x, highest_final_class_label, subtrees)
    #endregion

    def print_tree(self, tree, depth):
        if len(tree.subtrees) == 0:
            #ako je ovo list, vrati se nazad
            return
        if tree.name:
            #provjeri da postoji ime
            self.learning_output += str(depth) + ":" + tree.name + ", "
        for subtree in tree.subtrees:
            self.print_tree(subtree[1], depth + 1)

    def fit(self, dataset):
        self.tree = self.id3(dataset, self.dict_deepcopy(dataset), list(dataset.keys())[:-1], dataset[self.columns[-1]], list(dataset[self.columns[-1]]), 0)     #self.attributes.keys() mi je = X

        self.learning_output = ""
        self.print_tree(self.tree, 0)
        return self.learning_output[:-2]


    def test_tree(self, tree, sample):
        if tree.subtrees == []:
            return tree.name

        if tree.name in list(sample.keys()):
            for subtree in tree.subtrees:
                if subtree[0] == sample[tree.name]:
                    return self.test_tree(subtree[1], sample)
            return tree.highest_final_class_label       #da vrati varijablu sa najcescon frekv ako je neka nova vrijednost znacajke dosla

    def predict(self, dataset):
        testing_output = ""

        for i, sample in enumerate(dataset):
            testing_output += str(self.test_tree(self.tree, sample)) + " "

        return testing_output[:-1]







