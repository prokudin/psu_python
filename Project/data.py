#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:53:24 2019

@author: avp5627
"""

import pandas as pd

class DATA:
    def __init__(self,list={}):
        self.frames = [pd.read_excel("./data/"+file) for file in list]
        self.data = pd.concat(self.frames,sort=True)


if __name__ == '__main__':
    hermes = DATA({"1000.xlsx","1001.xlsx"})
