#! /bin/bash

# Description   : Foot Traffic installation script.
# Author        : ANU B NAIR
# Email         : anubnair90@gmail.com
# Date          : 08-02-2015
# (c) 2015

echo "###################################################"
echo "#          Foot Traffic           Installation    #"
echo "###################################################"

if [[ $EUID -ne 0 ]]; then
  echo "This script must be run as root! Exiting." 1>&2
  exit 1
fi

apt-get update

# Python dev files are needed.
sudo apt-get update
apt-get install python-dev python-pip python2.7

echo "###########################################################                       "
echo "                          Done!                                                   "
echo "                                                                                  "
echo "                                                                                  "
echo " Usage:                                                                           "
echo " foottraffic.py -f filename_with_path                                             "
echo " options:                                                                         "
echo "        -h --help                                                                 "
echo "        -f --file                                                                 "
echo " Example: python foottraffic.py -f=logfile.txt                                 "
echo "###########################################################                       "


