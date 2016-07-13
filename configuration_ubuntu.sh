#!/bin/bash

sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib
sudo pip install virtualenv==15.0.2
sudo pip install django==1.9.1
sudo pip install psycopg2==2.6


