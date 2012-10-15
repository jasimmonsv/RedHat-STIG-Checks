#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000380 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#If a user is assigned the GID of a group not existing on the system, and a group with the GID is subsequently created, the user may have unintended rights to the group.
#
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Perform the following to ensure there are no GIDs referenced in /etc/passwd not defined in /etc/group:
## pwck -r
#If GIDs referenced in /etc/passwd are not defined in /etc/group are returned, this is a finding.
#
#Fix Text: 
#Add a group to the system for each GID referenced without a corresponding group.   
#
#IA Controls:ECSC-1
#CCI: CCI-000366
#NIST SP 800-53A :: CM-6.1 (iv)
#NIST SP 800-53 :: CM-6 b

import os

def run():
	return -1

run()
