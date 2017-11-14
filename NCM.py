import random as r
def NCM():
    #cityMatrix = [[r.randrange(1, 100, 1) for j in range(5)] for i in range(5)]
    f = open('text.txt')
    cityMatrix = []
    for line in f:
       row = [float(i) for i in line.split()]
       cityMatrix.append(row)
    # for i in range(5):
    #     for j in range(5):
    #         if i == j:
    #             cityMatrix[i][j] = 0
    #         if j > i:
    #             cityMatrix[j][i] = cityMatrix[i][j]
    #for i in cityMatrix:
    #   print(i)
    # print("---" * 20)
    # for i in range(6):
    # X = [0, 1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14]
    X = [x for x in range(len(cityMatrix))]
    tempS = r.choice(X)
    #print("City: ", tempS, "\n", "---" * 20)
    X.remove(tempS)
    Distance = 0
    S = []
    Z = []
    CityMin = []
    S.append(tempS)
    while X:
        Z.clear()
        CityMin.clear()
        for i in S:
            Min = max(cityMatrix[i])
            for j in X:
                if cityMatrix[i][j] < Min:
                    Min = cityMatrix[i][j]
                    indexMin = j
            Z.append(Min)
            CityMin.append(indexMin)
        #for i in range(len(S)): print(S[i]," - (",Z[i],") - ",CityMin[i])
        #print("City: ",S[Z.index(min(Z))],"->", CityMin[Z.index(min(Z))], "\n", "Distance: ",
        #      min(Z), "\n", "---" * 20)
        S.insert(Z.index(min(Z))+1, CityMin[Z.index(min(Z))])
        Distance = Distance + min(Z)
        X.remove(CityMin[Z.index(min(Z))])
    #print("---" * 20, "\nPath: ", S,"\nDistance: ",Distance)
    return(S,Distance)