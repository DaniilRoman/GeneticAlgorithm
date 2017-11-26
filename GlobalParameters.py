import MainGenAlg as m

ProbabilityMutation = 0.001
ProbabilityCrossover = 1
PopulationSize = 20
BigNumber = 100000
ChildrenSize = 50
cityMatrix = []
flag = False
parentPairs = {"1": lambda Population, PopulationFit: m.SelectParentPair(Population, PopulationFit),
               "2": lambda Population, PopulationFit: m.PositivelyAsortotative(Population, PopulationFit),
               "3": lambda Population, PopulationFit: m.NegativelyAsortotative(Population, PopulationFit)}
crossovers = {"1": lambda parent1,parent2: m.PartiallyMappedCrossover(parent1,parent2),
               "2": lambda parent1, parent2: m.CycleCrossover(parent1, parent2)}
mutations = {"1": lambda population : m.Mutation(population), "2" : lambda population : m.Mutation2(population)}
selections = {"1": lambda Population, PopulationFit : m.SelectionRang(Population,PopulationFit),
              "2":lambda Population, PopulationFit : m.SelectionTournament(Population,PopulationFit)}
def cityMatrixAppend(row):
    global cityMatrix
    cityMatrix.append(row)
def setPopulationSize(populationSize):
    global PopulationSize
    PopulationSize = populationSize


def getPopulationSize():
    return PopulationSize


def doFlagTrue():
    global flag
    flag = True


def checkFlag():
    global flag
    if flag:
        return True
    else:
        return False
