#! /usr/bin/python
#Python Version 2.1
#
#This script checks for compliance with GEN000100 of DISA STIG RedHat_5-V1R1
#20 September 2012
#Author: J.A. Simmons V
#
#Discussion: 
#An operating system release is considered "supported" if the vendor continues to provide security patches for the product.  With #an unsupported release, it will not be possible to resolve security issues discovered in the system software.
#
#Documentable: No
#
#Responsibility: 
#System Administrator
#
#Severity Override Guidance: 
#If an extended support agreement provides security patches for the unsupported product is procured from the vendor, this finding #may be downgraded to a CAT III.
#
#Check Content: 
#Check the version of the operating system.
#
#Example:
## cat /etc/redhat-release
#
#Vendor End-of-Support Information:
#Red Hat Enterprise 5: 31 Mar 2014
#
#Check with the vendor for additional information.
#
#If the version installed is not supported, this is a finding.
#
#Fix Text: 
#Upgrade to a supported version of the operating system.
#
#IA Controls:VIVM-1
#CCI: CCI-001230
#NIST SP 800-53 :: SI-2 c
#NIST SP 800-53A :: SI-2.1 (iv)
#

import os

def run():return False

run()
