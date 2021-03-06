#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 19:34:20 2020

@author: zoro
"""

#Missing Data

#Libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#import data set

dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

#remove nan data from dataset
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(x[:, 1:3])

x[:, 1:3] = imputer.transform(x[:, 1:3])
