#!/bin/bash

# Script for installing all necessary packages
# to use django web app onto ubuntu server 14.04

echo "Begin to setup necessary packages..."
apt-get -y install git
if [[ `echo $?` -eq 0 ]]; then
	echo "Succesfully installed git"
else
	echo "Something went wrong, git not installed, check internet connection, aborting"
    exit 1
fi
# installing pip
apt-get -y install python3-pip
if [[ `echo $?` -eq 0 ]]; then
	echo "Succesfully installed pip3"
else
	echo "Something went wrong, pip3 not installed, check internet connection, aborting"
    exit 1
fi
# now install django
pip3 install Django
if [[ `echo $?` -eq 0 ]]; then
	echo "Succesfully installed django"
else
	echo "Something went wrong, django not intalled, check internet connection, aborting"
    exit 1
fi
# cloning my repo
git clone https://github.com/BronzeCrab/django_task
if [[ `echo $?` -eq 0 ]]; then
	echo "Succesfully cloned repo with project"
else
	echo "Something went wrong, repo not cloned, check internet connection, aborting"
    exit 1
fi
cd django_task
if [[ `echo $?` -eq 0 ]]; then
	echo "Succesfully went to django_task folder"
else
	echo "Something went wrong, aborting"
    exit 1
fi
cd django_task
python3 ./manage.py runserver 0.0.0.0:80