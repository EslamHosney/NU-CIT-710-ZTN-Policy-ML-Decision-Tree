# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:37:23 2021

@author: eslam
"""
import netaddr
import csv

from KiplingTrafficFlow import KiplingTrafficFlow

class StaticPolicyAgent:
    """
    Ignore: UserID=eslam,destinationID="Server",AppID="SSH",ContentID="Content",When="Noon",Where="Cairo",Action="allow",Action="deny"
    It’s a well known fact by now that ZT policies contain more data/input than
    the normal legacy network policies.
    Static policies will be the most dominant component in the PE structure as 
    it contains policies configured by security engineers normally this will be 
    used to map a specific organization policy or as a first mitigation technique 
    in case of a zero day attack. 
    """
    def __init__(self,*initial_data,**kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self,key,dictionary[key])
        for key in kwargs:
            setattr(self,key,kwargs[key]) 

    def validateFlow(self,flow,policiesFileName):
        #return action based on Static Security input might be (allow, deny, None)

        #Read csv into list of dict
        # with open('StaticPolicyAgentPolicies.csv') as f:
        with open(policiesFileName) as f:            
            StaticPolicyAgentPolicies = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]

        #Check if any policy matches the flow using Class KiplingTrafficFlow if matched return action else return None
        for policy in StaticPolicyAgentPolicies:
            policyFlow = KiplingTrafficFlow(policy)
            
            # temp = vars(flow)
            # for item in temp:
            #     print (item , ' : ' , temp[item])
            
            if flow == policyFlow: return policy['Action']
        return None
    
# if __name__ == "__main__":
#     flow = KiplingTrafficFlow({"UserID":"Mostafa", "destinationID":"DB","AppID":"SSH","ContentID":"Content","When":"Noon","Where":"Alex"})
#     policy = StaticPolicyAgent()
#     print (policy.validateFlow(flow))
