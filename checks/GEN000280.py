#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000280 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Shared accounts (accounts where two or more people log in with the same user identification) do not provide identification and authentication.  There is no way to provide for non-repudiation or individual accountability.
#
#Documentable: Yes
#
#Responsibility: 
#Information Assurance Officer
#
#Check Content: 
#Use the last command to check for multiple accesses to an account from different workstations/IP addresses.
#
## last -R
#
#If users log directly onto accounts, rather than using the switch user (su) command from their own named account to access them, this is a finding (such as logging directly on to oracle).
#
#Verify with the SA or the IAO on documentation for users/administrators to log into their own accounts first and then switch user (su) to the account to be shared has been maintained including requirements and procedures. If no such documentation exists, this is a finding. 
#
#Fix Text: 
#Use the switch user (su) command from a named account login to access shared accounts. Document requirements and procedures for users/administrators to log into their own accounts first and then switch user (su) to the account to be shared.     
#
#IA Controls:ECSC-1, IAIA-1
#CCI: CCI-000770
#NIST SP 800-53A :: IA-2 (5).2 (ii)
#NIST SP 800-53 :: IA-2 (5) (b)

import os

def run():
	return -1

run()
