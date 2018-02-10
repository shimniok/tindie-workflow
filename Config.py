#!/usr/bin/python

from __future__ import print_function


class Config:
    def __init__(self):
        self.user = ''
        self.key = ''
        with open('config.txt', 'r') as f:
            for line in f:
                line = ''.join(line.split())
                if not line.startswith('#'):
                    ent = line.split('=')
                    if ent[0] == 'user':
                        self.user = ent[1]
                    if ent[0] == 'key':
                        self.key = ent[1]
                    if ent[0] == 'dir':
                        self.dir = ent[1]
                    if ent[0] == 'weight':
                        self.weight = ent[1]
                    if ent[0] == 'height':
                        self.height = ent[1]
                    if ent[0] == 'length':
                        self.length = ent[1]
                    if ent[0] == 'width':
                        self.width = ent[1]
