from NCM import *
from GlobalParameters import *
import random as r
import numpy as np


def getCityMatrix():
    f = open('text.txt')
    global cityMatrix
    for line in f:
        row = [float(i) for i in line.split()]
        cityMatrix.append(row)


def GetStartPopulation():
    Populations = []
    for i in range(getPopulationSize()):
        Populations.append(NCM())
    return Populations


def PositivelyAsortotative(Population, PopulationFit):
    probability = []
    population, populationFit = Bubble_sort(Population, PopulationFit)
    _sum = sum(populationFit)
    for i in populationFit:
        probability.append(round(i / _sum, 10))
    indexies = []
    for i in range(len(Population)):
        indexies.append(i)
    a = np.int(np.random.choice(a=indexies, size=1, p=probability))
    b = np.int(np.random.choice(a=indexies, size=1, p=probability))
    return Population[a], Population[b]


def NegativelyAsortotative(Population, PopulationFit):
    probability = []
    population, populationFit = Bubble_sort(Population, PopulationFit)
    _sum = sum(populationFit)
    for i in populationFit:
        probability.append(round(i / _sum, 10))
    indexies = []
    for i in range(len(Population)):
        indexies.append(i)
    a = np.int(np.random.choice(a=indexies, size=1, p=probability))
    b = np.int(np.random.choice(a=indexies, size=1, p=probability))
    return Population[a], Population[-b - 1]


def ComputerFit(Individual):
    global cityMatrix
    fit = 0
    for i in range(0, len(Individual) - 2):
        fit = fit + cityMatrix[Individual[i]][Individual[i + 1]]
    fit = fit + cityMatrix[Individual[len(Individual) - 1]][Individual[0]]
    return fit


def Mutation(individual):
    rand1 = r.randint(0, len(individual) - 1)
    # print(rand1)
    rand2 = 0
    while (True):
        rand2 = r.randint(0, len(individual) - 1)
        if (rand2 != rand1):
            break
    # print(rand2)
    buf = individual[rand1]
    individual[rand1] = individual[rand2]
    individual[rand2] = buf
    return individual


def Mutation2(individual):
    sub = 0
    while sub < 3:
        rand1 = r.randint(0, len(individual) - 1)
        rand2 = r.randint(0, len(individual) - 1)
        sub = abs(rand1 - rand2)
    if rand1 > rand2:
        temp = rand1
        rand1 = rand2
        rand2 = temp
    temp = list(reversed(individual[rand1:rand2+1]))
    j = 0
    for i in range(rand1, rand2+1):
        individual[i] = temp[j]
        j = j + 1
    return individual


def CycleCrossover(ind1, ind2):
    childe = [0 for i in range(len(ind1))]
    deletes = []
    while (len(deletes) != len(childe)):
        i = r.randint(0, 1)
        inserts = []
        parent1 = []
        parent2 = []
        if (i == 0):
            parent1 = ind1
            parent2 = ind2
        else:
            parent1 = ind2
            parent2 = ind1
        while (True):
            k = r.randint(0, len(parent1) - 1)
            if (not deletes.__contains__(k)):
                break
        deletes.append(k)
        inserts.append([k, parent1[k]])
        startPos = parent1[k]
        while (startPos != parent2[k]):
            # находим позицию в первом родители значения второго родителя
            for i in range(len(parent1)):
                if (parent1[i] == parent2[k]):
                    k = i
                    inserts.append([k, parent1[k]])
                    deletes.append(k)
                    break
        for i in inserts:
            childe[i[0]] = i[1]
    return childe


def SelectParentPair(population, populationFit):
    a = r.choice(population)
    while True:
        b = r.choice(population)
        if (a != b):
            break
    return a, b


def PartiallyMappedCrossover(parent1, parent2):
    childe = [-1 for i in range(len(parent1))]
    # Задаем границы разбиения а1, а2
    a1 = r.randint(1, len(parent1) - 2)
    while (True):
        a2 = r.randint(1, len(parent1) - 2)
        if (a1 != a2):
            break
    # Обрабатываем условия
    if a1 > a2:
        temp = a1
        a1 = a2
        a2 = temp
    # a1 = 5
    # a2 = 13
    for i in range(a1, a2):
        childe[i] = parent1[i]
    temp = []
    for i in range(a1, a2):
        if (not parent1[a1:a2].__contains__(parent2[i])):
            temp.append([i, parent2[i]])
    for i in temp:
        key = i[0]
        while True:
            position = parent2.index(parent1[key])
            if (not parent2[position] in parent2[a1:a2]):
                break
            key = parent2.index(parent2[position])
            # print(key)
        childe[position] = i[1]
    for i in range(len(childe)):
        if (childe[i] == -1):
            childe[i] = parent2[i]
    return childe


def SelectionTournament(Population, PopulationFit):
    NewPopulation = []
    NewPopulationFit = []
    MinPopulationFit = min(PopulationFit)
    NewPopulation.append(Population[PopulationFit.index(MinPopulationFit)])
    NewPopulationFit.append(MinPopulationFit)
    count = 1
    italon = NewPopulationFit[0]
    for i in range(getPopulationSize() - 1):
        Tournament = []
        TournamentFit = []
        for x in range(4):
            Individual = r.choice(Population)
            Tournament.append(Individual)
            TournamentFit.append(ComputerFit(Individual))
        IndividualToNextPopulation = Tournament[TournamentFit.index(min(TournamentFit))]
        IndividualIndex = Population.index(
            IndividualToNextPopulation)  # МОЖНО ОПТИМИЗИРОВАТЬ, ЕСЛИ ХРАНИТЬ ЛИСТ ИНДЕКСОВ ИНДИВИДОВ КОТ ПОПАЛИ В ТУРНИР
        NewPopulation.append(IndividualToNextPopulation)
        NewPopulationFit.append(PopulationFit[IndividualIndex])
        if NewPopulationFit[i] == italon: count = count + 1
    if count >= getPopulationSize()-1:
        doFlagTrue()
        print("count: ", count)
    return NewPopulation, NewPopulationFit


def SelectionRang(Population, PopulationFit):
    NewPopulation = []
    NewPopulationFit = []
    MinPopulationFit = min(PopulationFit)
    NewPopulation.append(Population[PopulationFit.index(MinPopulationFit)])
    NewPopulationFit.append(MinPopulationFit)
    count = 1
    italon = NewPopulationFit[0]
    # print("Italon:", italon)
    Population, PopulationFit = Bubble_sort(Population, PopulationFit)
    Population = list(reversed(Population))
    PopulationFit = list(reversed(PopulationFit))
    indexies = [x for x in range(len(Population))]
    probability = computerProbability(Population)
    # print("indexes:", indexies)
    # print("prob:", probability)
    # print("ind:",len(indexies),"prob:",len(probability))
    try:
        for i in range(getPopulationSize() - 1):
            x = np.int(np.random.choice(indexies, 1, probability))
            NewPopulation.append(Population[x])
            NewPopulationFit.append(PopulationFit[x])
            if NewPopulationFit[i] == italon:
                count = count + 1
                # print("PochtiI0talon: ",NewPopulation[i])
    except:
        print(".")
    if count >= getPopulationSize():
        doFlagTrue()
    print("count: ", count)
    return NewPopulation, NewPopulationFit


def computerProbability(Population):
    probability = []
    nPositive = round(r.uniform(1.5, 2.0), 2)
    nNegative = round(2 - nPositive, 2)
    posSubNeg = round(nPositive - nNegative, 2)
    # print(nPositive,nNegative,posSubNeg)
    lenPopulation = len(Population)
    for i in range(lenPopulation):
        probability.append(float(round((nNegative + (posSubNeg * i / (lenPopulation - 1))) / lenPopulation, 10)))
    sum1 = 0
    for i in range(lenPopulation):
        sum1 = round(sum1 + probability[i], 10)
    # print("sum:",sum1)
    return probability


def doSort(Population, PopulationFit, start, end):
    if (start >= end):
        return Population, PopulationFit
    i = start
    j = end
    cur = round(i - (i - j) / 2)
    while (i < j):
        while ((i < cur) and (PopulationFit[i] <= PopulationFit[cur])):
            i = i + 1
        while (j > cur and (PopulationFit[cur] <= PopulationFit[j])):
            j = j - 1
        if (i < j):
            temp = PopulationFit[i]
            tempP = Population[i]
            PopulationFit[i] = PopulationFit[j]
            Population[i] = Population[j]
            PopulationFit[j] = temp
            Population[j] = tempP
            if (i == cur):
                cur = j
            else:
                if (j == cur):
                    cur = i
    doSort(Population, PopulationFit, start, cur)
    doSort(Population, PopulationFit, cur + 1, end)


def Bubble_sort(Population, PopulationFit):
    for i in range(len(Population)):
        for j in range(len(Population) - 1, i, -1):
            if PopulationFit[j] > PopulationFit[j - 1]:
                PopulationFit[j], PopulationFit[j - 1] = \
                    PopulationFit[j - 1], PopulationFit[j]
                Population[j], Population[j - 1] = \
                    Population[j - 1], Population[j]
    return Population, PopulationFit

def randomIndividual():
    individual = []
    buf = []
    temp = -1
    _len = len(cityMatrix)
    for i in range(_len):
        buf.append(i)
    for i in range(_len):
        rand = r.choice(buf)
        individual.append(rand)
        buf.remove(rand)
    individualFit = ComputerFit(individual)
    return individual, individualFit
