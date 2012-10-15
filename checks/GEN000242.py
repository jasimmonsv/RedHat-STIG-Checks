#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000242 of DISA STIG RedHat_5-V1R1
#24 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#A synchronized system clock is critical for the enforcement of time-based policies and the correlation of logs and audit records with other systems.  For redundancy, two time sources are required so synchronization continues to function if one source fails.  
#
#If the system is completely isolated (i.e., it has no connections to networks or other systems), time synchronization is not required as no correlation of events or operation of time-dependent protocols between systems will be necessary.  If the system is completely isolated, this requirement is not applicable.
#
#Note:  For the network time protocol (NTP), the requirement is two servers, but it is recommended to configure at least four distinct time servers which allow NTP to effectively exclude a time source not consistent with the others.  The system's local clock must be excluded from the count of time sources.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Check Content: 
#Check the root crontab (crontab -l) and the global crontabs in /etc/crontab, /etc/cron.d/*, or scripts in the /etc/cron.daily directory for the presence of an "ntpd -qg" job. If the "ntpd -qg" command is not invoked with at least two external NTP servers listed, this is a finding.
#
#Check the NTP daemon configuration for at least two external servers.
## grep ^server /etc/ntp.conf | egrep -v '(127.127.1.0|127.127.1.1)'
#If less than two servers or external reference clocks (127.127.x.x other than 127.127.1.0 or 127.127.1.1) are listed, this is a finding.
#
#Fix Text: 
# If using "ntpd -qg", add additional NTP servers to the cron job running "ntpd -qg".
#
#If using the NTP daemon, add an additional "server" line to /etc/ntp.conf for each additional NTP server.   
#
#IA Controls:ECSC-1
#CCI: CCI-000160
#NIST SP 800-53A :: AU-8 (1).1 (iii)
#NIST SP 800-53 :: AU-8 (1)

import os

def run():
	return -1

run()
