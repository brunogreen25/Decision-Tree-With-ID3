# Decision-Tree-With-ID3
Decision Tree model implemented from scratch.
<br/>
This model was a part of the Bachelor's assignment from the course Introduction to Artificial Intelligence.
It uses decision tree model with the ID3 algorithm.
<br/>
Expected output is in the following form: 
1) the decision tree graph structure
2) classification labels on the test set
3) accuracy
4) confusion matrix

To run the program, execute the following command with arguments:

1) **Volleyball Dataset** <br/>
python solution.py datasets/volleyball.csv datasets/volleyball_test.csv config/id3.cfg

**Expected output:** <br/>
0:weather, 1:wind, 1:humidity <br/>
yes yes yes yes no yes yes yes no yes yes no yes no no yes yes yes yes <br/>
0.57895 <br/>
4 7 <br/>
1 7 <br/>

2) **Logic Formula Dataset** <br/>
python solution.py datasets/logic_small.csv datasets/logic_small_test.csv config/id3.cfg

**Expected output:** <br/>
0:A, 1:C <br/>
False False True False False True <br/>
0.50000 <br/>
3 2 <br/>
1 0 <br/>

3) **Titanic Dataset** <br/>
python solution.py datasets/titanic_train_categorical.csv datasets/titanic_test_categorical.csv config/id3.cfg

**Expected output:** <br/>
0:sex, 1:passenger_class, 2:age, 3:fare, 4:cabin_letter, 4:cabin_letter,
4:cabin_letter, 3:fare, 4:cabin_letter, 4:cabin_letter,
4:cabin_letter, 3:fare, 4:cabin_letter, 4:cabin_letter, 3:fare,
4:cabin_letter, 4:cabin_letter, 4:cabin_letter, 3:fare,
4:cabin_letter, 4:cabin_letter, 2:age, 3:fare, 4:cabin_letter,
3:fare, 4:cabin_letter, 4:cabin_letter, 2:age, 3:fare,
4:cabin_letter, 3:cabin_letter, 4:fare, 1:cabin_letter, 2:age,
3:fare, 4:passenger_class, 3:fare, 4:passenger_class, 2:fare, 3:age,
3:age, 4:passenger_class, 3:age, 4:passenger_class, 3:age, 2:fare,
3:age, 4:passenger_class, 3:age, 4:passenger_class,
4:passenger_class, 3:age, 4:passenger_class, 3:age,
4:passenger_class, 2:fare, 3:age, 4:passenger_class, 3:age,
4:passenger_class, 2:age, 3:fare, 4:passenger_class, 2:age, 2:age,
3:passenger_class, 4:fare, 4:fare, 4:fare, 3:fare, 4:passenger_class,
4:passenger_class, 3:fare, 3:fare, 4:passenger_class, 3:fare, 3:fare,
4:passenger_class, 4:passenger_class, 3:fare, 4:passenger_class,
4:passenger_class, 4:passenger_class, 4:passenger_class,
3:passenger_class, 4:fare, 4:fare <br/>
no no no no no no no no no no no yes yes no no no yes yes no yes no no no
no no no yes no no no yes no yes yes yes no no no no yes no no no no
no yes no no yes no no no yes no no no no no no yes yes no no yes yes
yes yes no yes no no no no no no yes yes yes no yes no yes no no yes
yes no no no yes yes no yes no no no no yes no no no <br/>
0.78218 <br/>
56 9 <br/>
13 23 <br/>


All of the files can also have a tree with set max depth (to prevent overfitting). <br/>
To do so, use "config/id3_maxd1.cfg" instead of "config/id3.cfg".

