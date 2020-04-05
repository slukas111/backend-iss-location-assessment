#!/usr/bin/env python

__author__ = 'Sasha Lukas + demo'


def main(args):
    #Part A: Name of astronauts and crafts
    nauts_dict = get_astronauts()
    print('\nCurrent people in Space: {}'.format(len(nauts_dict)))
    for naut in nauts_dict:
        print(' - {}'.fomat(naut['name'], naut['craft']))



if __name__ == '__main__':
    main()
