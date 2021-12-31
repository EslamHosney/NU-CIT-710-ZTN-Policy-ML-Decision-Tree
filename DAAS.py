# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:35:12 2021

@author: eslam
"""
import netaddr

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
    def __init__(self, identity=None, ip=None):
        self.identity = identity
        self.ip = ip

    def __eq__(self, other):
        if ((self.identity == other.identity and self.identity != None) or (self.ip == other.ip and self.ip != None)):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    # def getRouteTable(self):
    #     #return routeing table
    #     pass
    
if __name__ == "__main__":    
    eslam = DAAS(identity="Exchange", ip='1.1.1.1/32')
    ahmed = DAAS(identity="Exchange", ip='1.1.1.2/32')
    print(eslam == ahmed)