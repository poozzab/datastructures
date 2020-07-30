#!/usr/bin/env python3

from Permutations import permGen
from Permutations import addToEachGroupEnd
from Permutations import insertToEachGroupForAllGroups
from Permutations import duplicateAndInsertAtPosn

cats = [1,2,3]

result = permGen(cats)

print(result)

print("///////////duplicateAndInsertAtPosn////////////")
cats = [[[0],[1]],[[0,1]]]
print(cats)
print(duplicateAndInsertAtPosn(2,cats[0],1))

print("///////////insertToEachGroupForAllGroups////////////")

cats = [[[0],[1]],[[0,1]]]

print( cats )

result = insertToEachGroupForAllGroups(2, cats)

print(result)

result = insertToEachGroupForAllGroups(3, result)

print(result)

print("///////////addToEachGroupEnd////////////")

cats = [[[0],[1]],[[0,1]]]

result = addToEachGroupEnd(2, cats)

print(cats)
print( result )

result = addToEachGroupEnd(3, result)

print(result)