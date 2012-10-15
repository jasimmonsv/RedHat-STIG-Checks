#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000300 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#A unique user name is the first part of the identification and authentication process.  If user names are not unique, there can be no accountability on the system for auditing purposes.  Multiple accounts sharing the same name could result in the denial of service to one or both of the accounts or unauthorized access to files or privileges.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check the system for duplicate account names.
#
#Example:
## pwck -r
#
#If any duplicate account names are found, this is a finding.
#
#Fix Text: 
#Change user account names, or delete accounts, so each account has a unique name.     
#
#IA Controls:IAIA-1, IAIA-2
#CCI: CCI-000764
#NIST SP 800-53A :: IA-2.1
#NIST SP 800-53 :: IA-2

import os

def run():
	f = os.popen("pwck")
	if f.read() == '':
		return 1
	else: return 0

run()
