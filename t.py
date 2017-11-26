from MainGenAlg import *
from GlobalParameters import *
import numpy as np
#Получаем матрицу городов из файла
f = open('text.txt')
for line in f:
    row = [float(i) for i in line.split()]
    cityMatrixAppend(row)
a,b = randomIndividual()
print(a)
print()
print(b)