# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:44:19 2021

@author: eslam
"""
import netaddr

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

    def match(self):
        flow = KiplingTrafficFlow()
        if (self.UserID == flow.UserID and self.AppID == flow.AppID and self.ContentID == flow.ContentID and self.When == flow.When and self.Where == flow.Where):
            return True
        else:
            return False

