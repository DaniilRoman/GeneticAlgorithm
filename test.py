import random as r
import MainGenAlg as m
Population = [3,2,5,32,5,1]
print(Population)
Population = m.Mutation(Population)
print(Population)
import MainGenAlg as m
childe = m.CycleCrossover([3,5,2,6,8,7,9],
                     [2,3,6,5,9,8,7])
print(childe)
print("---------")
population = [[3,5,2,6,8,7,9],
              [2,3,6,5,9,8,7],
              [6,5,2,3,7,8,9]]
print(m.SelectParentPair(population))
# print("-"*20)
# for i in range(20):
#     print(r.randint(0,len(population[0])-1))
print("-"*50)
print(m.PartiallyMappedCrossover(population[1],population[0]))
print(len([2,4,1]))
print("-"*50)
m.getCityMatrix()
print(m.cityMatrix)
print(m.ComputerFit([0,10,2,3,4,5,8,7,6,9,1,11,12,13,14]))
