#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000360 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Reserved GIDs are typically used by system software packages.  If non-system groups have GIDs in this range, they may conflict with system software, possibly leading to the group having permissions to modify system files.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Confirm all accounts with a GID of 499 and below are used by a system account. 
#
#Procedure:
#List all the users with a GID of 0-499.
## cut -d: -f 1,4 /etc/passwd|egrep ":[1-4][0-9]{2}$|:[0-9]{1,2}$"
#
#If a GID reserved for system accounts (0 - 499) is used by a non-system account, this is a finding.
#
#Fix Text: 
#Change the primary group GID numbers for non-system accounts with reserved primary group GIDs (those less or equal to 499). 
#
#IA Controls:ECSC-1
#CCI: CCI-000366
#NIST SP 800-53A :: CM-6.1 (iv)
#NIST SP 800-53 :: CM-6 b

import os

def run():
	return -1

run()
