# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:37:42 2021

@author: eslam
"""
import netaddr
import csv

from KiplingTrafficFlow import KiplingTrafficFlow

class SecurityFeeds:
    """
    Gather information from different resources Continuous diagnostics and 
    mitigation (CDM) system This gathers information about the enterprise 
    asset’s current state. Threat intelligence feed(s) external sources and 
    provide information about newly discovered attacks or vulnerabilities. 
    SIEM solutions provide log analysis on logs from different sources and 
    alerts based on configured use cases.
    """
    def __init__(self,*initial_data,**kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self,key,dictionary[key])
        for key in kwargs:
            setattr(self,key,kwargs[key]) 

    def validateFlow(self,flow,policiesFileName = "StaticPolicyAgentPolicies.csv"):
        #return action based on Static Security input might be (allow, deny, None)

        #Read csv into list of dict
        with open('SecurityFeeds.csv') as f:
            SecurityFeeds = [{k: v for k, v in row.items()}
                for row in csv.DictReader(f, skipinitialspace=True)]

        #Check if any policy matches the flow using Class KiplingTrafficFlow if matched return action else return None
        for feed in SecurityFeeds:
            # policyFlow = KiplingTrafficFlow(policy)
            # print (feed, flow.destinationID, feed['maliciousDest'] == flow.destinationID)
            if flow.destinationID == feed['maliciousDest']: return 'deny'
        return None
    
if __name__ == "__main__":
    flow = KiplingTrafficFlow({"UserID":"Samy", "destinationID":"malserver","AppID":"SSH","ContentID":"Content","When":"Noon","Where":"Cairo"})
    policy = SecurityFeeds()
    print (policy.validateFlow(flow))