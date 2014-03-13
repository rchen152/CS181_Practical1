import classification_starter as classify
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from sklearn import tree
from sklearn.externals.six import StringIO
import pickle
import pydot
import util

NUM_MALEWARE = 15

matrix_train = open('matrix_train', 'rb')
mat,key,cats = pickle.load(matrix_train)

matrix_test = open('matrix_test', 'rb')
test_mat,ids = pickle.load(matrix_test)


clf = tree.DecisionTreeClassifier()
clf = clf.fit(matrix_train,cats)
util.write_predictions(clf.predict(test_mat),ids,'syscall_count_by_type-1.csv')




with open("syscall.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

'''
dot_data = StringIO() 
tree.export_graphviz(clf, out_file=dot_data) 
graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
graph.write_pdf("tree_some.pdf")'''

