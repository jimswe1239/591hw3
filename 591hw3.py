# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:33:51 2019

@author: Jim
"""
import numpy as np

def solveGame(A):# A is a 2d list
    p1len = len(A)
    p2len = len(A[0])
    rowlen = p2len
    collen = p1len
    p1strat = [0 for x in range(p1len)]
    p2strat = [0 for x in range(p2len)]
    value = 0
    for row in range(len(A)):
        if len(A[row]) != p2len:
            print("ERROR: Row lengths not even")
    #check saddle point
    rowmins = []
    colmaxs = []
    for row in range(p1len):
        minVal = A[row][0]
        for x in range(rowlen):
            if A[row][x] < minVal:
                minVal = A[row][x]
        rowmins += [minVal]
    for column in range(p2len):
        maxVal = A[0][column]
        for x in range(collen):
            if A[x][column] > maxVal:
                maxVal = A[x][column]
        colmaxs += [maxVal]
    for x in range(p1len):
        for y in range(p2len):
            if A[x][y] == rowmins[x] == colmaxs[y]:
                value = A[x][y]
                p1strat[x] = 1
                p2strat[y] = 1
                return [p1strat,p2strat,value]
    #check 2x2
    if p1len == p2len == 2:
        return solve2x2(A)
    #check 2xn
    if p1len == 2:
        lines = []
        intersections = []
        for x in range(p2len):
            lines += [[A[1][x],A[0][x]]]
        int0 = [0]+min([[z[0],[z]] for z in lines])
        int1 = [1]+min([[z[1],[z]] for z in lines])
        intersections += [int0]
        intersections += [int1]
        for one in range(p2len):
            for two in range(p2len):
                if one == two:
                    continue
                if lines[one] == lines[two]:
                    continue
                if (lines[one][0] > lines[two][0] and lines[one][1] < lines[two][1]) or (lines[one][0] < lines[two][0] and lines[one][1] > lines[two][1]):
                    #lines intersect between 0 and 1
                    lineoneint = lines[one][0]
                    linetwoint = lines[two][0]
                    lineoneslope = lines[one][1]-lines[one][0]
                    linetwoslope = lines[two][1]-lines[two][0]
                    x = (linetwoint - lineoneint) / (lineoneslope - linetwoslope)
                    y = lineoneint + x*lineoneslope
                    intersections += [[x,y,[lines[one],lines[two]]]]
        intersections = sorted(intersections)
        activeline = intersections[0][2][0]
        intersections2 = []
        intersections2 += [intersections[0]]
        for x in range(len(intersections)):
            if x % 2 == 1:
                intersections2 += [intersections[x]]
        intersections = intersections2
        envelope = []
        for x in range(1,len(intersections)-1):
            if activeline in intersections[x][2]:
                envelope += [intersections[x]]
                if activeline != (intersections[x][2])[0]:
                    activeline = (intersections[x][2])[0]
                else:
                    activeline = (intersections[x][2])[1]
        
        envelope = [intersections[0]] + envelope + [intersections[len(intersections)-1]]
        output = max(envelope, key = lambda t: t[1])
        #print(activeline)
        #print(intersections)
        #print(envelope)
        #print(output)
        line1 = output[2][0]
        line2 = output[2][1]
        col1 = 0
        col2 = 0
        while A[0][col1] != line1[1] and A[1][col1] != line1[0]:
            col1 += 1
        while A[0][col2] != line2[1] and A[1][col2] != line2[0]:
            col2 += 1
        #print(col1,col2)
        newA = [[A[0][col1],A[1][col1]],[A[0][col2],A[1][col2]]]
        newSol = solve2x2(newA)
        p1sol = newSol[1]
        p2sol = []
        for x in range(p2len):
            if x == col1:
                p2sol += [newSol[0][0]]
            elif x == col2:
                p2sol += [newSol[0][1]]
            else:
                p2sol += [0]
        return [p1sol,p2sol,newSol[2]]
    #check mx2
    if p2len == 2:
        lines = []
        intersections = []
        for x in range(p1len):
            lines += [[A[x][1],A[x][0]]]
        int0 = [0]+max([[z[0],[z]] for z in lines])
        int1 = [1]+max([[z[1],[z]] for z in lines])
        intersections += [int0]
        intersections += [int1]
        for one in range(p1len):
            for two in range(p1len):
                if one == two:
                    continue
                if lines[one] == lines[two]:
                    continue
                if (lines[one][0] > lines[two][0] and lines[one][1] < lines[two][1]) or (lines[one][0] < lines[two][0] and lines[one][1] > lines[two][1]):
                    #lines intersect between 0 and 1
                    lineoneint = lines[one][0]
                    linetwoint = lines[two][0]
                    lineoneslope = lines[one][1]-lines[one][0]
                    linetwoslope = lines[two][1]-lines[two][0]
                    x = (linetwoint - lineoneint) / (lineoneslope - linetwoslope)
                    y = lineoneint + x*lineoneslope
                    intersections += [[x,y,[lines[one],lines[two]]]]
        intersections = sorted(intersections)
        activeline = intersections[0][2][0]
        intersections2 = []
        intersections2 += [intersections[0]]
        for x in range(len(intersections)):
            if x % 2 == 1:
                intersections2 += [intersections[x]]
        intersections = intersections2
        envelope = []
        for x in range(1,len(intersections)-1):
            if activeline in intersections[x][2]:
                envelope += [intersections[x]]
                if activeline != (intersections[x][2])[0]:
                    activeline = (intersections[x][2])[0]
                else:
                    activeline = (intersections[x][2])[1]
        
        envelope = [intersections[0]] + envelope + [intersections[len(intersections)-1]]
        output = min(envelope, key = lambda t: t[1])
        #print(activeline)
        #print(intersections)
        #print(envelope)
        #print(output)
        line1 = output[2][0]
        line2 = output[2][1]
        row1 = 0
        row2 = 0
        while A[row1][0] != line1[1] and A[row1][1] != line1[0]:
            row1 += 1
        while A[row2][0] != line2[1] and A[row2][1] != line2[0]:
            row2 += 1
        #print(col1,col2)
        newA = [[A[row1][0],A[row1][1]],[A[row2][0],A[row2][1]]]
        newSol = solve2x2(newA)
        p1sol = []
        p2sol = newSol[1]
        for x in range(p1len):
            if x == row1:
                p1sol += [newSol[0][0]]
            elif x == row2:
                p1sol += [newSol[0][1]]
            else:
                p1sol += [0]
        return [p1sol,p2sol,newSol[2]]
    #check principle of indifference using all active assumption
    if p1len == p2len:
        aArray = np.array(A)
        aDet = np.linalg.det(aArray)
        #print(aDet)
        subTen = False
        if aDet == 0:
            newArray = []
            for x in range(p1len):
                newRow = []
                for y in range(p2len):
                    newRow += [A[x][y]+10]
                newArray += [newRow]
            aArray = np.array(newArray)
            aDet = np.linalg.det(aArray)
            if aDet != 0:
                subTen = True
        if aDet != 0:
            aInv = np.linalg.inv(aArray)
            ones = np.array([[1] for x in range(p2len)])
            onesT = np.array([1 for x in range(p2len)])
            v = np.dot(onesT,aInv)
            dotprod = 0
            for x in range(len(v)):
                dotprod += v[x]
            valMaybe = 1/dotprod
            qMaybe = np.dot(aInv,ones)/dotprod
            print(qMaybe)
            noNeg = True
            for checker in range(len(qMaybe)):
                if qMaybe[checker] < 0:
                    noNeg = False
                    break
            if noNeg:
                pMaybe = np.dot(onesT,aInv)/dotprod
                p = []
                q = []
                for counter in range(len(pMaybe)):
                    p += [pMaybe[counter]]
                    q += [qMaybe[counter][0]]
                if(subTen):
                    toReturn = [p,q,valMaybe-10]
                else:
                    toReturn = [p,q,valMaybe]
                if min(toReturn[0]) < 0 or min(toReturn[1]) < 0:
                
                #solve with linear programming
                    return linprog(A)
                return toReturn
    return linprog(A)



def linprog(A):
    #initialize the simplex method
    minVal = A[0][0]
    for x in range(len(A)):
        for y in range(len(A[0])):
            if A[x][y] < minVal:
                minVal = A[x][y]
    if minVal >= 0:
        minVal = 0
    ys = [("y",y) for y in range(len(A[0]))]
    xs = [("x",x) for x in range(len(A))]

    newA = []
    for x in range(len(A)):
        newRow = []
        for y in range(len(A[0])):
            newRow += [A[x][y] - minVal]
        newRow += [1]
        
        newA += [newRow]
    newA += [[-1 for x in range(len(A[0]))]+[0]]

    #begin simplex method
    while(min(newA[len(newA)-1]) < 0):
        
        col = 0
        minValCol = 0
        for x in range(len(newA[len(newA)-1])):
            if newA[len(newA)-1][x]<minValCol:
                minValCol = newA[len(newA)-1][x]
                col = x
        row = 0
        minValRow = None
        for y in range(len(newA)-1):
            if newA[y][col] > 0 and (minValRow == None or newA[y][len(newA[0])-1]/newA[y][col]<minValRow):
                minValRow = newA[y][len(newA[0])-1]/newA[y][col]
                row = y
        newerA = []
        for x in range(len(newA)):
            newRow = []
            for y in range(len(newA[0])):
                if x == row and y == col:
                    newRow += [1/newA[x][y]]
                elif x == row:
                    newRow += [newA[x][y]/newA[row][col]]
                elif y == col:
                    newRow += [-newA[x][y]/newA[row][col]]
                else:
                    newRow += [newA[x][y] - (newA[row][y] * newA[x][col] / newA[row][col])]
            newerA += [newRow]
        
        newA = newerA
        
        hold = xs[row]
        xs[row] = ys[col]
        ys[col] = hold

    p = [0 for x in range(len(newA)-1)]
    q = [0 for y in range(len(newA[0])-1)]
    for x in range(len(newA[0])-1):
        #print(xs[0][0])
        if ys[x][0] == "x":
            p[ys[x][1]] = newA[len(newA)-1][x] / newA[len(newA)-1][len(newA[0])-1]
    for y in range(len(newA)-1):
        if xs[y][0] == "y":
            q[xs[y][1]] = newA[y][len(newA[0])-1] / newA[len(newA)-1][len(newA[0])-1]
    return [p,q,1/(newA[len(newA)-1][len(newA[0])-1])+minVal]
    


def solve2x2(A):
    a = A[0][0]
    b = A[0][1]
    d = A[1][0]
    c = A[1][1]
    p = (c-d)/((a-d)+(c-b))
    q = (c-b)/((a-d)+(c-b))
    value = p*(A[0][0]) + (1-p)*(A[1][0])
    return [[p,1-p],[q,1-q],value]
    
#print(solveGame([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))
#linprog([[1,2],[3,4],[5,6]])
def runTests():
    file_name = 'nfgsOut.txt'
    nfgs = open(file_name, 'r')
    
    nfgsList = [line.rstrip('\n') for line in nfgs]
    nfgsList = [nfgsList[x] for x in range(1,len(nfgsList)) if nfgsList[x] != "" and nfgsList[x][0] == "N" and nfgsList[x-1][0] != "N"]
    nfgs.close()
    
    file_name = 'results2.txt'
    results = open(file_name, 'a+')
    
    for w in range(100):
        
        nfgVals = nfgsList[w].split(",")[1:]
        newNfgs = []
        for x in nfgVals: 
            try:
                newNfgs += [int(x)]
            except ValueError:
                x = x.split("/")
                newNfgs += [int(x[0])/int(x[1])]
    
        
        
        file_name = 'txts/game' + str(w) + '.txt'
        txt = open(file_name, 'r')
        toRun = [line.rstrip('\n') for line in txt]
        for x in range(len(toRun)):
            toRun[x] = toRun[x].split()
        for x in range(len(toRun)):
            for y in range(len(toRun[0])):
                toRun[x][y] = int(toRun[x][y])
        
        newTxt = solveGame(toRun)
        newNfg = [0,0,0]
        newNfg[0] = newNfgs[0:len(newTxt[0])]
        newNfg[1] = newNfgs[len(newTxt[0]):]
        nfgV = 0
        index = 0
        while newNfg[0][index] == 0:
            index += 1
        for x in range(len(toRun[0])):
            nfgV += toRun[index][x] * newNfg[1][x]
        newNfg[2] = nfgV
        
        sumdiff = 0
        for x in range(len(newNfg[0])):
            sumdiff += abs(newNfg[0][x] - newTxt[0][x])
        for x in range(len(newNfg[1])):
            sumdiff += abs(newNfg[1][x] - newTxt[1][x])
        sumdiff += abs(newNfg[2] - newTxt[2])
        
        results.write("GAME "+str(w)+":\n")
        results.write(str(toRun))
        results.write("\nGambit's p: "+str(newNfg[0])+"\nOur p:      "+str(newTxt[0])+"\nGambit's q: "+str(newNfg[1])+"\nOur q:      "+str(newTxt[1])+"\nGambit's v: "+str(newNfg[2])+"\nOur v:      "+str(newTxt[2])+"\nSum Difference between us and Gambit: "+str(sumdiff)+"\nSum Difference less than 0.0000001: "+str(sumdiff<0.0000001)+"\n\n")
    
        txt.close()















