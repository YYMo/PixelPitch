#!/bin/bash

sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
#for pillow on ubuntu
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk


pip install django==1.9.1
pip install psycopg2==2.6
pip install Pillow
pip install python-resize-image


