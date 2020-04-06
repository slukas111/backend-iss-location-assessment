#!/usr/bin/env python

import time
import turtle 
import urllib
import requests

__author__ = 'Sasha Lukas + demo'


#gobal scope
base_url = 'http://api.open-notify.org'


def get_astronauts():
    """return dictionary of current astronauts and their spacecrafts"""
    r = requests.get(base_url + '/astros.json')
    r.raise_for_status()
    return r.json()['name']


def main(args):
    #Part A: Name of astronauts and crafts
    nauts_dict = get_astronauts()
    print('\nCurrent people in Space: {}'.format(len(nauts_dict)))
    for naut in nauts_dict:
        print(' - {}'.fomat(naut['name'], naut['craft']))



if __name__ == '__main__':
    main()
