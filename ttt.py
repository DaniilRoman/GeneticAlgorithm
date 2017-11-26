import random as r
from GlobalParameters import *
from MainGenAlg import *

nPositive = 1.7
nNegative = 0.3
posSubNeg = 1.4
lenPopulation = 70  # len(Population)
probability = []
sum1 = 0
# print(nNegative,nPositive,posSubNeg)
# for i in range(lenPopulation):
#     probability.append(round((nNegative + (posSubNeg*i/(lenPopulation-1)))/lenPopulation, 10))
#     print(probability[i])
# print("-"*20)
# for i in range(len(probability)):
#     sum1 = sum1 + probability[i]
# print(sum1)
import numpy as np

qqq = [3, 4, 5, 2, 2, 5, 3, 5]
print(qqq[7], qqq[-8])
for i in range(1, 2):
    print(i)
print("+" * 50)
print(Mutation2(qqq))
a = input()
print("posmotrim:", a)