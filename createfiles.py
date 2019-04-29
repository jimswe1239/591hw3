# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:59:38 2019

@author: Jim
"""
import random
dontrun!!
for w in range(100):
    file_name = 'txts/game' + str(w) + '.txt'
    txt = open(file_name, 'w+')
    file_name = 'nfgs/game' + str(w) + '.nfg'
    nfg = open(file_name, 'w+')
    
    collen = random.randint(1,11)
    rowlen = random.randint(1,11)
    nfg.write('NFG 1 R "game"\n{ "Player 1" "Player 2" } { ' + str(collen) + " " + str(rowlen) +' }\n\n')
    
    array = []
    for y in range(collen):
        newRow = []
        for x in range(rowlen):
            newRow += [(random.randint(-1000,1001))]
        array += [newRow]

    for y in range(collen):
        for x in range(rowlen):
            txt.write(str(array[y][x]) + " ")
        txt.write('\n')
        
    
    for y in range(rowlen):
        for x in range(collen):
            nfg.write(str(array[x][y]) + " " + str(array[x][y] * -1) + " ")
    txt.close()
    nfg.close()