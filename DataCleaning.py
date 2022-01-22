# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 11:19:45 2022

@author: eslam
"""
import netaddr
import csv
import numpy as np

from KiplingTrafficFlow import KiplingTrafficFlow

class DataCleaning:
    """
    Ignore: UserID=eslam,destinationID="Server",AppID="SSH",ContentID="Content",When="Noon",Where="Cairo",Action="allow",Action="deny"
    To enable more generic polices and defination for Zero Trust access rules.
    We will provide a basic regix * to be replaced with all available options.
    Initial policies file name will be provided then the * will be repolaced with all other values available in the same column
    """
    def __init__(self, rawFileName=None, policiesFileName=None):
        self.rawFileName = rawFileName
        self.policiesFileName = policiesFileName
        # self.generatedPolicies = []
        # policy = StaticPolicyAgent()
        generatedPolicies = self.expandPolicies()
        self.save_csv(generatedPolicies, policiesFileName)
        # for x in generatedPolicies:
        #     print(x)
            
        
    def getUniqueValuesColumn(self,twodList,columnId,removedValues):
        buff = list(set([ x[columnId] for x in twodList]))                      #this will ensure only 1 existance of each value
        for value in removedValues:
            buff.remove(value)
        
        return buff
         
        
    def expandPolicies(self):
        generatedPolicies=[]
        raw_policies = list(csv.reader(open(self.rawFileName)))
        raw_policies = raw_policies[1:]                                         #remove first row which contains cloumn names
        
        # print(self.getUniqueValuesColumn(raw_policies, 0))
        
        while True:
            for x in range(len(raw_policies)):
                if('*' in raw_policies[x]):
                    for y in range(len(raw_policies[x])):
                        if (raw_policies[x][y] == '*'):
                            valuesColumn = self.getUniqueValuesColumn(raw_policies, y, ['*'])
                            for value in valuesColumn:
                                buff = raw_policies[x].copy()
                                buff[y] = value
                                generatedPolicies.append(buff)              
                else:
                    generatedPolicies.append(raw_policies[x])
            
            if (any("*" in sublist for sublist in generatedPolicies)):          #check if the result still comntains * to be removed in case of 1 line 2 *
                raw_policies = generatedPolicies.copy()
                generatedPolicies=[]
            else:
                break
            
        raw_policies = list(csv.reader(open(self.rawFileName)))
        generatedPolicies.insert(0,raw_policies[0].copy())
        return generatedPolicies

    def save_csv(self, twodList, fileName):
        f = open(fileName, 'w')
        for item in twodList:
            f.write(','.join([str(x) for x in item]) + '\n')
        f.close()
        
    
if __name__ == "__main__":

    # fileName = "RawStaticPolicyAgentPolicies.csv"
    rawFileName = "RawStaticPolicyAgentPolicies.csv"
    policiesFileName = "StaticPolicyAgentPolicies.csv"
    data = DataCleaning(rawFileName, policiesFileName)
    # print (policy.validateFlow(flow))