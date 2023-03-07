from sklearn import tree
import pandas as pd

data = pd.read_csv("Lab_exp_5/DT.csv")
print(data)
from sklearn.preprocessing import LabelEncoder

Le = LabelEncoder()
data["OL"] = Le.fit_transform(data["OL"])
data["Temp"] = Le.fit_transform(data["Temp"])
data["Hum"] = Le.fit_transform(data["Hum"])
data["Wind"] = Le.fit_transform(data["Wind"])
data["PT"] = Le.fit_transform(data["PT"])
print(data)
y = data["PT"]
X = data.drop(["PT"], axis=1)
clf = tree.DecisionTreeClassifier(criterion="entropy")
clf = clf.fit(X, y)
# To view the tree as a graph
import graphviz

dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
print(graph)
# To view the tree in Text Format
from sklearn.tree import export_text
feature_names = list(X.columns)
r = export_text(clf,feature_names=feature_names)
print(r)
