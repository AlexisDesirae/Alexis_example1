import random

def mean (x:list):
    x_mean = sum(x) / len(x)
    return x_mean

def error (list,y):
   y_errors = [i-y for i in list]
   return y_errors
