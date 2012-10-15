#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN00002 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#GEN000020
#Discussion: 
#If the system does not require valid root authentication before it boots into single-user or maintenance mode, anyone who invokes #single-user or maintenance mode is granted privileged access to all files on the system.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check if the system requires a password for entering single-user mode.
## grep ':S:' /etc/inittab
#If /sbin/sulogin is not listed, this is a finding.
#
#Fix Text: 
#Edit /etc/inittab and set sulogin to run in single-user mode.
#Example line in /etc/inittab:
#~:S:wait:/sbin/sulogin
#
#IA Controls:IAIA-1, IAIA-2
#CCI: CCI-000213
#NIST SP 800-53A :: AC-3.1
#NIST SP 800-53 :: AC-3
import os

def run():
	result = os.popen("grep ':S:' /etc/inittab)
	if result.read().find(':S:') =-1:return False
	else: return True
	
run()
