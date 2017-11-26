import random as r
import MainGenAlg as m
import numpy as np
from GlobalParameters import *
# Population = [3,2,5,32,5,1]
# print(Population)
# Population = m.Mutation(Population)
# print(Population)
# import MainGenAlg as m
# childe = m.CycleCrossover([3,5,2,6,8,7,9],
#                      [2,3,6,5,9,8,7])
# print(childe)
# print("---------")
# population = [[3,5,2,6,8,7,9],
#               [2,3,6,5,9,8,7],
#               [6,5,2,3,7,8,9]]
# print(m.SelectParentPair(population))
# # print("-"*20)
# # for i in range(20):
# #     print(r.randint(0,len(population[0])-1))
# print("-"*50)
# print(m.PartiallyMappedCrossover(population[1],population[0]))
# print(len([2,4,1]))
# print("-"*50)
# m.getCityMatrix()
# print(m.cityMatrix)
# print(m.ComputerFit([0,10,2,3,4,5,8,7,6,9,1,11,12,13,14]))
# print("Mutatuin")
# print(m.Mutation(population[0]))
m.getCityMatrix()
Population = []
PopulationFit = []
for i in range(PopulationSize):
    population, fit = m.NCM()
    Population.append(population)
    PopulationFit.append(fit)
for i in range(len(Population)):
    print(Population[i], PopulationFit[i])
print("="*50)
Population, PopulationFit = m.Bubble_sort(Population,PopulationFit)
for i in range(len(Population)):
    print(Population[i], PopulationFit[i])
print("="*50)
print("="*50)
nPositive = round(r.uniform(1.5, 2.0), 2)
nNegative = round(2 - nPositive,2)
posSubNeg = round(nPositive - nNegative,2)
lenPopulation = len(Population)
probability = []
sum1 = 0
print(nNegative,nPositive,posSubNeg)
for i in range(len(Population)):
    probability.append(round((nNegative + (posSubNeg*i/lenPopulation))/lenPopulation, 2))
    print(probability[i])
print("-"*20)
for i in range(len(probability)):
    sum1 = round(sum1 + probability[i],2)
print(sum1)
pie = round((1 - sum1)/1, 2)
sum1 = 0
for i in range(len(probability)-1, len(probability)):
    probability[i] = round(probability[i] + pie, 2)
# probability[len(probability)-2] = round(probability[len(probability)-2] + pie, 2)
# probability[len(probability)-1] = round(probability[len(probability)-1] + pie, 2)
print("-"*50)
for i in range(len(probability)):
    sum1 = round(sum1 + probability[i], 2)
    print(sum1, probability[i])
print(sum1)
print(pie)
print("="*50)
print("="*50)
print("="*50)
# sum1 = 0
# probability = m.computerProbability(Population)
# for i in range(len(probability)):
#     sum1 = round(sum1 + probability[i],2)
#     print(probability[i])
# print("---")
# print(sum1)
# print("+"*50)
# print(len(Population))
populationFit = []
print(m.PartiallyMappedCrossover(Population[3],Population[12]))
for i in range(len(Population)):
    populationFit.append(m.ComputerFit(Population[i]))
    print(i)
print("---")
for i in range(len(populationFit)):
    print(i)
print(PopulationFit[2])
print(populationFit[2])
print("-"*100)
temp, tempFit = m.Bubble_sort(Population,PopulationFit)
for i in tempFit:
    print(i)

a,b = parentPairs[3](Population, PopulationFit)
print(a)
print(b)

print(parentPairs[2](Population, PopulationFit))

