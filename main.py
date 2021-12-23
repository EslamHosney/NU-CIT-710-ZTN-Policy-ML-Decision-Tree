# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:24:18 2021

@author: eslam
"""
import netaddr

from DAAS import DAAS
from KiplingTrafficFlow import KiplingTrafficFlow
from StaticPolicyAgent import StaticPolicyAgent
from SecurityFeeds import SecurityFeeds
from MLPolicies import MLPolicies



if __name__ == "__main__":
    
    ip = netaddr.IPNetwork('10.230.99.172')
    user = DAAS(identity="Eslam",name="EslamSamy",ip=ip)
    flow = KiplingTrafficFlow(UserID=user, AppID="SSH", ContentID=None, When="Daytime", Where="Local")
    static = StaticPolicyAgent().validateFlow(flow)
    feeds = SecurityFeeds().validateFlow(flow)
    ml = MLPolicies().validateFlow(flow)
    
    
    
    
#    print (str(ip))
#    f = SRX("","","","",ReadFile('SF.txt'),ReadFile('SF_routes.txt'))