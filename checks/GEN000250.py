#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000250 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems.  If an illicit time source is used for synchronization, the integrity of system logs and the security of the system could be compromised.  If the configuration files controlling time synchronization are not owned by a system account, unauthorized modifications could result in the failure of time synchronization.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check the ownership of the NTP configuration file.
## ls -l /etc/ntp.conf
#If the owner is not root, this is a finding.
#
#Fix Text: 
# Change the owner of the NTP configuration file.
## chown root /etc/ntp.conf
#
#IA Controls:ECLP-1
#CCI: CCI-000225
#NIST SP 800-53A :: AC-6.1
#NIST SP 800-53 :: AC-6

import os

def run():
	f = os.open('ls -l /etc/ntp.conf')
	f = f.read()
	if f[13:19].find('root') > -1:
		return 1
	else: return 0


run()
