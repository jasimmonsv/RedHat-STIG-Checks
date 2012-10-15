#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000241 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems.  Internal system clocks tend to drift and require periodic resynchronization to ensure their accuracy.  Software, such as ntpd, can be used to continuously synchronize the system clock with authoritative sources.  Alternatively, the system may be synchronized periodically, with a maximum of one day between synchronizations.
#
#If the system is completely isolated (i.e., it has no connections to networks or other systems), time synchronization is not required as no correlation of events or operation of time-dependent protocols between systems will be necessary. If the system is completely isolated, this requirement is not applicable.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/* for the presence of an "ntpd -qg" job to run at least daily, which should have asterisks (*) in columns 3, 4, and 5.
#
#Check the daily cron directory (/etc/cron.daily) for any script running "ntpd -qg".
#
#Check for a running NTP daemon.
## ps ax | grep ntpd
#
#If none of the above checks are successful, this is a finding.
#
#Fix Text: 
#Enable the NTP daemon for continuous synchronization.
## service ntpd start ; chkconfig ntpd on
#
#OR
#
#Add a daily or more frequent cronjob to perform synchronization using ntpdate.
#
#
#IA Controls:ECSC-1
#CCI: CCI-000366
#NIST SP 800-53A :: CM-6.1 (iv)
#NIST SP 800-53 :: CM-6 b

import os

def run():
	return -1

run()
