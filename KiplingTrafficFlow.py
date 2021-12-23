# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:44:19 2021

@author: eslam
"""
import netaddr

from DAAS import DAAS
from KiplingTrafficFlow import KiplingTrafficFlow
from StaticPolicyAgent import StaticPolicyAgent
from SecurityFeeds import SecurityFeeds
from MLPolicies import MLPolicies

class KiplingTrafficFlow:
    """
    Machine learning could be used to discover hidden patterns in data. 

    """
    def __init__(self, UserID=None, AppID=None, ContentID=None, When=None, Where=None):
        self.UserID = UserID
        self.AppID = AppID
        self.ContentID = ContentID
        self.When = When
        self.Where = Where