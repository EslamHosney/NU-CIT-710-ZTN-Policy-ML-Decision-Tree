# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:44:19 2021

@author: eslam
"""
import netaddr
from DAAS import DAAS

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

    def __eq__(self, other):
        if (self.UserID == other.UserID and self.AppID == other.AppID and self.ContentID == other.ContentID and self.When == other.When and self.Where == other.Where):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

if __name__ == "__main__":
    eslam = DAAS(identity="Exchange", ip='1.1.1.1/32')
    ahmed = DAAS(identity="Exchange", ip='1.1.1.2/32')    
    eslamFlow = KiplingTrafficFlow(UserID=eslam, AppID="SSH", ContentID="Content", When="Noon", Where="Cairo")
    ahmedFlow = KiplingTrafficFlow(UserID=ahmed, AppID="SSH", ContentID="Content", When="Noon", Where="Cairo")
    print(eslamFlow != ahmedFlow)