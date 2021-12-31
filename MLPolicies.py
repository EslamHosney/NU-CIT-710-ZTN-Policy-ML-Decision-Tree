# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:37:56 2021

@author: eslam
"""
import netaddr

class MLPolicies:
    """
    Machine learning could be used to discover hidden patterns in data. 
    A machine learning algorithm could be trained to discover the hidden 
    pattern in the network connectivity Using the same features in Kappling 
    method (who, what, when, where, why, how) we could deal with the allow/block 
    queries as a classification method and tarin it using (white team provide 
    the allow data set and red team (pentest team) provides the block data set) 
    Or we could use a trusted team member from each team to build the policy 
    based on his behavior. 
    After the flos is validated against the static policies and security feeds 
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