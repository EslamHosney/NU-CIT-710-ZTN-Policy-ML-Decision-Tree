# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:37:56 2021

@author: eslam
"""
import netaddr
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier 
from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn import preprocessing

class MLPolicies:
    """
    Machine learning could be used to discover hidden patterns in data. 
    A machine learning algorithm could be trained to discover the hidden 
    pattern in the network connectivity Using the same features in Kappling 
    method (who, what, when, where, why, how) we could deal with the allow/block 
    queries as a classification method and train it using (white team provide 
    the allow data set and red team (pentest team) provides the block data set) 
    Or we could use a trusted team member from each team to build the policy 
    based on his behavior. 
    After the flow is validated against the static policies and security feeds 
    it will be validated against the trained model Algorithms to be used 
    (Decision tree)
    """
    def __init__(self, identity=None, name=None, ip=None):
        self.identity = identity
        self.name = name
        self.ip = ip

    def validateFlow(self,flow):
        #return action based on ML Policies input might be (True, None, False)
        return True


if __name__ == "__main__":
    # flow = KiplingTrafficFlow({"UserID":"Mostafa", "destinationID":"DB","AppID":"SSH","ContentID":"Content","When":"Noon","Where":"Alex"})
    # policy = StaticPolicyAgent()
    # print (policy.validateFlow(flow))

    # Read Training set from csv file 
    policies = pd.read_csv("StaticPolicyAgentPolicies.csv")
    trafficFlow = policies.values[:, :-1]           # features
    policyAction = policies.values[:, -1]           # class

    # OneHotEncoder for X 
    enc = OneHotEncoder(handle_unknown='ignore')    # Transform string features into 1 and 0
    enc.fit(trafficFlow)                            # fit training data

    trafficFlowEncoded = enc.transform(trafficFlow).toarray()
    # featureNamesEncoded = enc.get_feature_names(["UserID","destinationID","AppID","ContentID","When","Where"])
    # get features names
    featureNamesEncoded = enc.get_feature_names(list(policies.head())[:-1])

    # LabelEncoder for y
    le = preprocessing.LabelEncoder()
    le.fit(np.unique(policyAction))
    # print (le.classes_)
    # print (le.transform(policyAction))
    policyActionEncoded = le.transform(policyAction)
    # print (policyActionEncoded)

    # Fit the classifier with default hyper-parameters
    clf = DecisionTreeClassifier(random_state=1234)
    model = clf.fit(trafficFlowEncoded, policyActionEncoded)

    text_representation = tree.export_text(clf, feature_names=list(featureNamesEncoded))
    print(text_representation)

    # le.fit(np.array(set(policyAction)))
    # print (le.fit(np.unique(policyAction)))
    # print(le.transform["allow", "allow", "deny"])

    # # Fit the classifier with default hyper-parameters
    # clf = DecisionTreeClassifier(random_state=1234)
    # model = clf.fit(trafficFlow, policyAction)

    # text_representation = tree.export_text(clf)
    # print(text_representation)
    # print ("Hello World!")

    # # Prepare the data data
    # iris = datasets.load_iris()
    # X = iris.data
    # print (type(X))
    # input("X:")
    # y = iris.target
    # print (y)
    # input("y:")
    # # Fit the classifier with default hyper-parameters
    # clf = DecisionTreeClassifier(random_state=1234)
    # model = clf.fit(X, y)

    # text_representation = tree.export_text(clf)
    # print(text_representation)