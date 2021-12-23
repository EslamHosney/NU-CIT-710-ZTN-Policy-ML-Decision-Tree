# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:35:12 2021

@author: eslam
"""
import netaddr

from DAAS import DAAS
from KiplingTrafficFlow import KiplingTrafficFlow
from StaticPolicyAgent import StaticPolicyAgent
from SecurityFeeds import SecurityFeeds
from MLPolicies import MLPolicies

class DAAS:
    """
    Palo Alto Networks | Simplify Zero Trust Implementation with a Five-Step Methodology | White Paper 1
    
    When defining the protect surface, you need to consider all
    critical data, application, assets, and services (DAAS). This
    could include:
    • Data—payment card information (PCI), protected health
    information (PHI), personally identifiable information
    (PII), and intellectual property (IP)
    • Applications—off-the-shelf or custom software
    • Assets—SCADA controls, point-of-sale terminals, medical
    equipment, manufacturing assets, and internet of things
    (IoT) devices
    • Services—DNS, DHCP, and Active Directory®
    """
    def __init__(self, identity=None, name=None, ip=None):
        self.identity = identity
        self.name = name
        self.ip = ip

    def getRouteTable(self):
        #return routeing table
        pass
    
    
eslam = DAAS(identity="Exchange")
print(eslam.identity, eslam.ip, eslam.name)