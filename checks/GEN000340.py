#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000340 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Reserved UIDs are typically used by system software packages.  If non-system accounts have UIDs in this range, they may conflict with system software, possibly leading to the user having permissions to modify system files.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check the UID assignments for all accounts.
#
## cut -d: -f 1,3 /etc/passwd | egrep ":[1-4][0-9]{2}$|:[0-9]{1,2}$"
#
#Confirm all accounts with a UID of 499 and below are used by a system account. If a UID reserved for system accounts (0 - 499) is used by a non-system account, then this is a finding.
#
#Fix Text: 
#Change the UID numbers for non-system accounts with reserved UIDs (those less or equal to 499).   
#
#IA Controls:ECSC-1
#CCI: CCI-000366
#NIST SP 800-53A :: CM-6.1 (iv)
#NIST SP 800-53 :: CM-6 b

import os

def run():
	return -1

run()
