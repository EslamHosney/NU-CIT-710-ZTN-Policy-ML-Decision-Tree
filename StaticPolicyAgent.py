# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:37:23 2021

@author: eslam
"""
import netaddr

from DAAS import DAAS
from KiplingTrafficFlow import KiplingTrafficFlow
from StaticPolicyAgent import StaticPolicyAgent
from SecurityFeeds import SecurityFeeds
from MLPolicies import MLPolicies

class StaticPolicyAgent:
    """
    It’s a well known fact by now that ZT policies contain more data/input than
    the normal legacy network policies.
    Static policies will be the most dominant component in the PE structure as 
    it contains policies configured by security engineers normally this will be 
    used to map a specific organization policy or as a first mitigation technique 
    in case of a zero day attack. 
    """
    def __init__(self, identity=None, name=None, ip=None):
        self.identity = identity
        self.name = name
        self.ip = ip

    def validateFlow(self,flow):
        #return routeing table
        return True
    