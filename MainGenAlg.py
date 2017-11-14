from NCM import *
import random as r
ProbabilityMutation = 0.001
ProbabilityCrossover = 1
cityMatrix = []

def getCityMatrix():
    f = open('text.txt')
    global cityMatrix
    for line in f:
       row = [float(i) for i in line.split()]
       cityMatrix.append(row)


def GetStartPopulation():
    Populations = []
    for i in range(10):
        Populations.append(NCM())
    return Populations

def ComputerFit(Individual):
    global cityMatrix
    fit = 0
    for i in range(0, len(Individual)-2):
        fit = fit + cityMatrix[Individual[i]][Individual[i+1]]
    return fit

def Mutation(individual):
    rand1 = r.randint(0,len(individual)-1)
    print(rand1)
    rand2 = 0
    while(True):
        rand2 = r.randint(0, len(individual)-1)
        if(rand2!=rand1):
            break
    print(rand2)
    buf = individual[rand1]
    individual[rand1] = individual[rand2]
    individual[rand2] = buf
    return individual



def CycleCrossover(ind1,ind2):
    childe = [0 for i in range(len(ind1))]
    deletes = []
    while(len(deletes)!=len(childe)):
        i = r.randint(0,1)
        inserts = []
        parent1 = []
        parent2 = []
        if(i==0):
            parent1 = ind1
            parent2 = ind2
        else:
            parent1 = ind2
            parent2 = ind1
        while(True):
            k = r.randint(0,len(parent1)-1)
            if (not deletes.__contains__(k)):
                break
        deletes.append(k)
        inserts.append([k,parent1[k]])
        startPos = parent1[k]
        while(startPos!=parent2[k]):
            #находим позицию в первом родители значения второго родителя
            for i in range(len(parent1)):
                if(parent1[i]==parent2[k]):
                    k = i
                    inserts.append([k, parent1[k]])
                    deletes.append(k)
                    break
        for i in inserts:
            childe[i[0]] = i[1]
    return childe



def SelectParentPair(population):
    a = r.choice(population)
    while True:
        b = r.choice(population)
        if(a != b):
            break
    return a,b


def PartiallyMappedCrossover(parent1,parent2):
    childe = [0 for i in range(len(parent1))]
    #Задаем границы разбиения а1, а2
    a1 = r.randint(1, len(parent1)-2)
    while (True):
        a2 = r.randint(1, len(parent1) - 2)
        if (a1!=a2):
            break
    #Обрабатываем условия
    if a1>a2:
        temp = a1
        a1 = a2
        a2 = temp
    for i in range(a1,a2):
        childe[i] = parent1[i]
    #
    temp = []
    for i in range(a1,a2):
        if (not parent1[a1:a2].__contains__(parent2[i])):
            temp.append([i,parent2[i]])
    for i in temp:
        key = i[0]
        while True:
            position = parent2.index(parent1[key])
            if (not parent2[position] in parent2[a1:a2]):
                break
            key = parent2.index(parent2[position])
        childe[position] = i[1]
    for i in range(len(childe)):
        if (childe[i]==0):
            childe[i] = parent2[i]
        print(childe)
    return parent1,parent2,a1,a2,childe

def Selection(Population):
    return