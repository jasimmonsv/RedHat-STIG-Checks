#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000220 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#Changes in system libraries, binaries and other critical system files can indicate compromise or significant system events such as patching needing to be checked by automated processes and the results reviewed by the SA.
#
#NOTE: For MAC I systems, increase the frequency to daily.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Determine if there is an automated job, scheduled to run weekly or more frequently, to run the file integrity tool to check for unauthorized additions to system libraries. The check can be done using Advanced Intrusion Detection Environment (AIDE) which is part of the Red Hat Enterprise Linux (RHEL)  distribution. Other file integrity software may be used but must be checked manually. 
#
#Procedure:
#Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/* for the presence of an "aide" job to run at least weekly, which should have asterisks (*) in columns 3, 4, and 5.
#
#Check the weekly cron directory (/etc/cron.weekly) for any script running "aide --check" or "aide -C" or simply "aide". If there is not, this is a finding.
#
#NOTE: For MAC I systems, increase the frequency to daily.
#
#
#Fix Text: 
#Establish an automated job, scheduled to run weekly or more frequently, to run "aide --check" which is the file integrity tool to check for unauthorized system libraries or binaries.
#
#NOTE: For MAC I systems, increase the frequency to daily.
#
#IA Controls:DCSL-1
#CCI: CCI-001069
#NIST SP 800-53A :: RA-5 (7).1 (ii)
#NIST SP 800-53 :: RA-5 (7)


import os

def run():return -1

run()
