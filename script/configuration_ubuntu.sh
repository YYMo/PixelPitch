#!/bin/bash

sudo apt-get update
sudo apt-get install python-pip python-dev libpq-dev postgresql postgresql-contrib

pip install django==1.9.1
pip install psycopg2==2.6
pip install Pillow
pip install python-resize-image


