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
from sklearn.metrics import classification_report



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
    def __init__(self):
        return

    def validateFlow(self,testingPoliciesFileName = "TestingPolicies.csv",policiesFileName = "StaticPolicyAgentPolicies.csv"):
        # print (graphviz.__file__)
        # Read Training set from csv file 
        trainingPolicies    = pd.read_csv(policiesFileName)
        testingPolicies     = pd.read_csv(testingPoliciesFileName)
    
        trainingFlow        = trainingPolicies.values[:, :-1]               # features
        trainingAction      = trainingPolicies.values[:, -1]                # class
    
        testingFlow         = testingPolicies.values[:, :-1]                # features
        testingAction       = testingPolicies.values[:, -1]                 # class
    
        # OneHotEncoder for X 
        featuresEncoder = OneHotEncoder(handle_unknown='ignore')                        # Transform string features into 1 and 0
        featuresEncoder.fit(trainingFlow)                                               # fit training data
    
        trafficFlowEncoded = featuresEncoder.transform(trainingFlow).toarray()
        testingFlowEncoded = featuresEncoder.transform(testingFlow).toarray()
        # get features names ["UserID","destinationID","AppID","ContentID","When","Where"]
        featureNamesEncoded = featuresEncoder.get_feature_names(list(trainingPolicies.head())[:-1])
    
        # LabelEncoder for y trainig
        trainingLabelEncoder = preprocessing.LabelEncoder()
        trainingLabelEncoder.fit(np.unique(trainingAction))
        trainingActionEncoded = trainingLabelEncoder.transform(trainingAction)
        # print ("Training encoded")
        # print (trainingActionEncoded)
        
        # LabelEncoder for y testing
        testingLabelEncoder = preprocessing.LabelEncoder()
        testingLabelEncoder.fit(np.unique(testingAction))
        testingActionEncoded = trainingLabelEncoder.transform(testingAction)
        # print ("Testing encoded")
        # print (testingActionEncoded)
        
        
        
        # Fit the classifier with default hyper-parameters
        clf = DecisionTreeClassifier(random_state=1234)
        model = clf.fit(trafficFlowEncoded, trainingActionEncoded)
    

        # Run against testing Data
        testingActionPredictedEncoded = clf.predict(testingFlowEncoded)
        # print (labelEncoder.inverse_transform(testingActionPredictedEncoded))
        for action in trainingLabelEncoder.inverse_transform(testingActionPredictedEncoded):
            print (action)
        
        # Print ML metrices
        print (testingActionEncoded)
        print (testingActionPredictedEncoded)
        print (classification_report(y_true=testingActionEncoded, y_pred=testingActionPredictedEncoded))
        
        # Visual Representation on teh Algorithm
        text_representation = tree.export_text(clf, feature_names=list(featureNamesEncoded))
        print(text_representation)
        
        fig = plt.figure(figsize=(50,50))
        _ = tree.plot_tree(clf, 
                        feature_names=featureNamesEncoded,  
                        class_names=["allow", "deny"],
                        max_depth=4,
                        proportion=True,
                        filled=False,
                        fontsize=32)
        fig.savefig("decistion_tree_Copy.png")
        return True


if __name__ == "__main__":
    
    x = MLPolicies()
    # x.validateFlow()
    x.validateFlow(testingPoliciesFileName = "TestingPolicies - Copy.csv",policiesFileName = "StaticPolicyAgentPolicies - Copy.csv")
 