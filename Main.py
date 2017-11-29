from MainGenAlg import *
import numpy as np

print("Введите размер популяции: ")
populationSize = int(input())
setPopulationSize(populationSize)
print(
    "Выберите метод выбора родительской пары:\n1 - Рандомом\n2 - Положительной ассортативностью\n3 - Отрицательной ассортативностью")
parentPair = input()
print("Выберите кроссовер:\n1 - Частичного отображения\n2 - Циклический")
crossover = input()
print("Выберите мутацию:\n1 - Меняем два города местами\n2 - Делаем реверс части пути")
mutation = input()
print("Выберите вероятность мутации, введя число от 0 100:")
probMutation = input()
print("Выберите метод селекции: \n1 - Ранговая селекция\n2 - Турнир")
selection = input()
# Получаем матрицу городов из файла
getCityMatrix()
Population = []
PopulationFit = []
print("-" * 100)
# Отбираем начальную популяцию
for i in range(getPopulationSize()):
    population, fit = randomIndividual()
    Population.append(population)
    PopulationFit.append(fit)
# Выводим на экран начальную популяцию
print("-" * 100)
for j in range(2000):
# Формируем потомков
    Children = []
    ChildrenFit = []
    for i in range(ChildrenSize):
# Выбор пары

        parents = parentPairs[parentPair](Population, PopulationFit)
# Кроссовер
        Children.append(crossovers[crossover](parents[0], parents[1]))
        ChildrenFit.append(ComputerFit(Children[i]))
# Объединение
    Population = Population + Children
    PopulationFit = PopulationFit + ChildrenFit
# Мутация
    print("Mutation:")
    for i in range(len(Population)):
        rand = r.randint(0, 100)
        if rand in range(1, int(probMutation)):
            m = mutations[mutation](Population[i])
            PopulationFit[i] = ComputerFit(m)
# Селекция
    Population, PopulationFit = selections[selection](Population, PopulationFit)
#         Children, ChildrenFit = selections[selection](Children, PopulationFit)
#         Population = Population[:10] + Children[:10]
#         PopulationFit = PopulationFit[:10] + ChildrenFit[:10]
# Вывод популяции
    print("Selection:")
    print(j, "- population")
    _max = max(PopulationFit)
    print(Population[PopulationFit.index(_max)],round(_max,2))
    # for i in range(len(Population)):
    #     print(Population[i], PopulationFit[i])
    if checkFlag() or j == 2000:
        for i in range(len(Population)):
            print(Population[i], round(PopulationFit[i],2))
        break
    if j == 0:
        for i in range(len(Population)):
            print(Population[i], round(PopulationFit[i], 2))

