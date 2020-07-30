#!/usr/bin/env python3

# consume an array of items
# produce an array of all possible groupings of those items
def permGen(collection):
    if len(collection) == 0:
        return [[[]]]
    result = [[[collection[0]]]]
    for cat in collection[1:]:
        inserts = insertToEachGroupForAllGroups( cat, result )
        result = addToEachGroupEnd( cat, result )
        result.extend(inserts)
        print("res: " + str(result))
    return result

# this method will add the newMember to each group for all the group of groups
# one at a time and return the new groupings
def insertToEachGroupForAllGroups(newMember, perms):
    newPerms = []
    for groupOfGroups in perms:
        # the replicant groupOfGroups to be populated
        newGroupOfGroups = []
        numGroups = len(groupOfGroups)
        currInsertIdx = 0
        while currInsertIdx < numGroups:
            for groupIdx in range(len(groupOfGroups)):
                dupeGroup = list(groupOfGroups[groupIdx])
                if currInsertIdx == groupIdx:
                    dupeGroup.append(newMember)
                newGroupOfGroups.append(dupeGroup)
            newPerms.append(newGroupOfGroups)
            currInsertIdx += 1
            newGroupOfGroups = []
    return newPerms

def duplicateAndInsertAtPosn(newMember, groupOfGroups, posn):
    newGroupOfGroups = []
    for groupIdx in range(len(groupOfGroups)):
        dupe = list(groupOfGroups[groupIdx])
        if groupIdx == posn:
            dupe.append(newMember)
        newGroupOfGroups.append(dupe)
    return newGroupOfGroups


# this method will add the newMember as a new group to the ends of each of
# the group of groups
def addToEachGroupEnd(newMember, perms):
    newPerms = list()
    for groupOfGroups in perms:
        dupes = list()
        for group in groupOfGroups:
            dupes.append(list(group))
        dupes.append([newMember])
        newPerms.append(dupes)
    return newPerms


# do not run on a list containing itself
def duplicateList(originalList):
    if not isinstance(originalList, list):
        raise Exception("Ya done goofed")
    duplicate = list()
    for item in originalList:
        dupe = item
        if isinstance(item,list):
            dupe = duplicateList(item)
        duplicate.append(dupe)
    return list(originalList)
