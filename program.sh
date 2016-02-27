#!/bin/bash

cd pro
source bin/activate
echo `./manage.py runserver`
