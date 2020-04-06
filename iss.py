#!/usr/bin/env python

import time
import turtle 
import urllib
import requests

__author__ = 'Sasha Lukas + demo'


"""gobal scopes"""
base_url = 'http://api.open-notify.org'
iss_icon = 'iss.gif'
world_map = 'map.gif'


def get_astronauts():
    """return dictionary of current astronauts and their spacecrafts"""
    r = requests.get(base_url + '/astros.json')
    r.raise_for_status()
    return r.json()['people']

def get_iss_location():
    """returns the current location (lat, lon) if iss as a float tuple"""
    r = requests.get(base_url + '/iss-now.json')
    r.raise_for_status()
    position = r.json()['iss_position']
    lat = float(position['latitude'])
    lon = float(position['longitude'])
    return lat, lon

def map_iss(lat, lon):
    """draw a world map and place iss icon at lat, lon"""
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.bgpic(world_map)
    screen.setworldcoordinates(-180, -90, 180, 90)

    screen.register_shape(iss_icon)
    iss = turtle.Turtle()
    iss.shape(iss_icon)
    iss.setheading(90)
    iss.penup()
    iss.goto(lon, lat)
    return screen



def main(args):
    # Part A: Name of astronauts and crafts
    nauts_dict = get_astronauts()
    print('\nCurrent people in Space: {}'.format(len(nauts_dict)))
    for naut in nauts_dict:
        print(' - {}'.fomat(naut['name'], naut['craft']))
    
    #Part B: current positionof iss
    lat, lon = get_iss_location()
    print('\nCurrent iss coordinates: lat={:.02f} lon={:.02f}'.format(lat, lon))

#Part C: render current iss on world map
    screen = None
    try:
        screen = map_iss(lat, lon)


if __name__ == '__main__':
    main()
