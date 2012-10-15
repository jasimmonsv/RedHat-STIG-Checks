#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000280 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Accounts providing no operational purpose provide additional opportunities for system compromise.  Unnecessary accounts include user accounts for individuals not requiring access to the system and application accounts for applications not installed on the system.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check the system for unnecessary user accounts. 
#
#Procedure:
#
## more /etc/passwd 
#
#Obtain a list of authorized accounts from the IAO.  If any unnecessary accounts are found on the system, this is a finding.
#
#Fix Text: 
#Remove all unnecessary accounts from the /etc/passwd file before connecting a system to the network. Other accounts that are associated with a service not in use should also be removed.
#
#IA Controls:IAAC-1
#CCI: CCI-000012
#NIST SP 800-53 :: AC-2 j
#NIST SP 800-53A :: AC-2.1 (i)

import os

def run():
	return -1

run()
