# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:24:18 2021

@author: eslam
"""
import netaddr
import csv

from DAAS import DAAS
from KiplingTrafficFlow import KiplingTrafficFlow
from StaticPolicyAgent import StaticPolicyAgent
from SecurityFeeds import SecurityFeeds
from MLPolicies import MLPolicies
from DataCleaning import DataCleaning

if __name__ == "__main__":
    rawFileName = "RawStaticPolicyAgentPolicies - Copy.csv"
    policiesFileName = "StaticPolicyAgentPolicies - Copy.csv"                                                            
    testingPoliciesFileName = "TestingPolicies - Copy.csv"
    securityFeedsFileName = "SecurityFeeds - Copy.csv"
    MLpoliciesFileName = "StaticPolicyAgentPolicies - Copy.csv" 

    # rawFileName = "RawStaticPolicyAgentPolicies.csv"
    # policiesFileName = "StaticPolicyAgentPolicies.csv"                                                            
    # testingPoliciesFileName = "TestingPolicies.csv"
    # securityFeedsFileName = "SecurityFeeds.csv"
    # MLpoliciesFileName = "StaticPolicyAgentPolicies.csv" 
    
    # Data cleaning
    data = DataCleaning(rawFileName, policiesFileName)

    # Read Cleaned Policies
    with open(testingPoliciesFileName) as f:
        testingDict = [{k: v for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]

    # Static Policies
    print("Static Policies Action")        
    policy = StaticPolicyAgent()    
    for flow in testingDict:
        # print (flow)
        policyFlow = KiplingTrafficFlow(flow)
        print (policy.validateFlow(policyFlow, policiesFileName = policiesFileName))

    # Security Feeds
    print("Security Feeds Action")
    policy = SecurityFeeds()    
    for flow in testingDict:
        policyFlow = KiplingTrafficFlow(flow)
        print (policy.validateFlow(policyFlow, policiesFileName = securityFeedsFileName))
        
    # Machine Learning Policies
    print("Machine Learning Action")
    policy = MLPolicies()
    policy.validateFlow(testingPoliciesFileName = testingPoliciesFileName, policiesFileName = MLpoliciesFileName)

