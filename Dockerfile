FROM python:3.6.1

# curl and wget are pre-installed

###########
# Python Modules
##########
# certifi       - Certifi is a collection of Root Certificates for validating SSL certificates and verifying identity of TLS hosts.
# click         - A simple wrapper around optparse for powerful command line utilities.
# elasticsearch - module for interacting with elasticsearch
# requests      - Python HTTP for Humans.
# virtualenv    - virtual environments for python

RUN pip install certifi click elasticsearch requests virtualenv

###########
# Utilities
##########
# jq - formats and processes json.
# vim - text editor

RUN apt-get update \
 && apt-get upgrade -y \
 && apt-get install -y jq vim
