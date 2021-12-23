# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:37:42 2021

@author: eslam
"""
import netaddr

from DAAS import DAAS
from KiplingTrafficFlow import KiplingTrafficFlow
from StaticPolicyAgent import StaticPolicyAgent
from SecurityFeeds import SecurityFeeds
from MLPolicies import MLPolicies

class SecurityFeeds:
    """
    Gather information from different resources Continuous diagnostics and 
    mitigation (CDM) system This gathers information about the enterprise 
    asset’s current state. Threat intelligence feed(s) external sources and 
    provide information about newly discovered attacks or vulnerabilities. 
    SIEM solutions provide log analysis on logs from different sources and 
    alerts based on configured use cases.
    """
    def __init__(self, identity=None, name=None, ip=None):
        self.identity = identity
        self.name = name
        self.ip = ip

    def validateFlow(self,flow):
        #return routeing table
        return True