# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:44:19 2021

@author: eslam
"""
import netaddr
#import pandas as pd
import csv



from DAAS import DAAS

class KiplingTrafficFlow:
    """
    Machine learning could be used to discover hidden patterns in data. 
    UserID=eslam,destinationID="Server",AppID="SSH",ContentID="Content",When="Noon",Where="Cairo"
    """
    #def __init__(self,UserID=None,destinationID=None,AppID=None,ContentID=None,When=None,Where=None,*initial_data,**kwargs):
    def __init__(self,*initial_data,**kwargs):
        # self.UserID = UserID
        # self.destinationID = destinationID
        # self.AppID = AppID
        # self.ContentID = ContentID
        # self.When = When
        # self.Where = Where 
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self,key,dictionary[key])
        for key in kwargs:
            setattr(self,key,kwargs[key]) 

    def __eq__(self,other):
        if (self.UserID == other.UserID and self.destinationID == other.destinationID and self.AppID == other.AppID and self.ContentID == other.ContentID and self.When == other.When and self.Where == other.Where):
            return True
        else:
            return False

    def __ne__(self,other):
        return not self.__eq__(other)


if __name__ == "__main__":
    # eslam = DAAS(identity="Exchange",ip='1.1.1.1/32')
    # ahmed = DAAS(identity="Exchange",ip='1.1.1.2/32')    
    # eslamFlow = KiplingTrafficFlow(UserID=eslam,AppID="SSH",ContentID="Content",When="Noon",Where="Cairo")
    # ahmedFlow = KiplingTrafficFlow(UserID=ahmed,AppID="SSH",ContentID="Content",When="Noon",Where="Cairo")
    # print(eslamFlow != ahmedFlow)
    # file = pd.read_csv("staticFlows.csv")
    # print (file)
    # flow = {"UserID":"eslamdict", "destinationID":"Server","AppID":"SSH","ContentID":"Content","When":"Noon","Where":"Cairo"}
    # flowDict = KiplingTrafficFlow(flow)
    # print (flowDict.Where)
    with open('StaticPolicyAgentPolicies.csv') as f:
        flowsDict = [{k: v for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
    print (flowsDict)
    for flow in flowsDict:
        policyFlow = KiplingTrafficFlow(flow)
        print(policyFlow.UserID)
