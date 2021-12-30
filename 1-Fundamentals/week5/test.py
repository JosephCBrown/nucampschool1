import random
def binarySearch(alist, item):
        first = 0
        last = len(alist) - 1
        found = False

        while first<=last and not found:
            midpoint = (first + last)//2            
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1  
        return found

def findThisNum(mynum):

    testlist = [x for x in range(listlength)]

    print("testlist = ", testlist)
    print("finding number ", mynum)

    if (binarySearch(testlist, findnum)) == True:
        print("found %d" %mynum)
    else:
        print("Not found %d" %mynum)




#### Main_Function ####

if __name__ == "__main__":
    #

    #Search 1 [ Even numbered list ]
    listlength = 10    
    findnum = random.randrange(0,listlength)
    findThisNum(findnum)     

    #Search 2 [ [ Odd numbered list ]
    listlength = 13    
    findnum = random.randrange(0,listlength)
    findThisNum(findnum)

    #search 3  [ find item not in the list ]

    listlength = 13    
    findnum = random.randrange(0,listlength) + listlength
    findThisNum(findnum)