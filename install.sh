#!/bin/bash

yum install -y ssh
yum install -y git
yum install -y nano vim vi

yum install -y python3 python3-pip python3-devel
yum install -y gcc
#yum install -y 

pip3 install virtualenv

git config --global user.email "ec2-docker-`cat /etc/hostname`@ba"
git config --global user.name "ec2-docker-`cat /etc/hostname`"
