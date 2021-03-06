#Bogosort Tester
#Bogosort is a sorting method in which a list is randomized until it is sorted in the correct order.

import random
List=[]
ReferenceList=[]
Tries=0

while True:
    try:
        ElemNum=int(input('Number of entities to sort: '))
    except ValueError:
        print("Enter a valid integer.\n")
    else:
        print('\n')
        break

for i in range(ElemNum):
    List.append(i+1)
    ReferenceList.append(i+1)


while True:
    Tries=Tries+1
    random.shuffle(List)
    print('Attempt No. '+str(Tries)+': '+str(List))
    if List==ReferenceList:
        print('\nComplete after: '+str(Tries)+' Attempts')
        break
    
