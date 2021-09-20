import random

def playerProgression(data):

    numWorse = 0
    numBetter = 0
    print("\n\n\n******** PROGRESSION/REGRESSION MODULE ********")
    
    for i in range(1,len(data)):
        dn = random.randint(1,100) #stands for dice number, 1 to 3 is a rating change, 4 or 5 is no change
        pf=0 #stands for progress factor, only matters if player actually progresses/regresses

        if dn >= 1 and dn <= 50:
            pf = random.randint(1,49)

            dig1 = int(pf / 10) #this is the first digit for position-specific attributes    
            dig2 = pf % 10 #this is the second digit of pf number, it's how much injury and fatigue change
            
            # change injury and fatigue up or down
            if dn <=40:
                numWorse = numWorse + 1
                
                dig1 = dig1 * -1
                dig2 = dig2 * -2

                print("Player " + data[i][15] + " " + data[i][16] +
                      " getting worse.")

                if data[i][15] != "0" or data[i][16] != "0":
                    data[i][20] = str(int(data[i][20]) + dig2)
                    data[i][56] = str(int(data[i][56]) + dig2)
                else:
                    break
            else:
                numBetter = numBetter + 1
                print("Player " + data[i][15] + " " + data[i][16] +
                      " improving.")
                
                if data[i][15] != "0" or data[i][16] != "0":
                    data[i][20] = str(int(data[i][20]) + dig2)
                    data[i][56] = str(int(data[i][56]) + dig2)
                else:
                    break

        # now, change position specific attributes
            if data[i][114] == "0": #quarterbacks
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][54] = str(int(data[i][54]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][87] = str(int(data[i][87]) + dig1)
                data[i][14] = str(int(data[i][14]) + dig1)
            elif data[i][114] == "1": #halfbacks
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + 2 * dig1)
                data[i][54] = str(int(data[i][54]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][65] = str(int(data[i][65]) + 2 * dig1)
                data[i][140] = str(int(data[i][140]) + dig1)
            elif data[i][114] == "2": #fullbacks
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][102] = str(int(data[i][102]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][65] = str(int(data[i][65]) + dig1)
                data[i][60] = str(int(data[i][60]) + 2 * dig1)
            elif data[i][114] == "3": #wide receiver
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][54] = str(int(data[i][54]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][51] = str(int(data[i][51]) + 2 * dig1)
                data[i][101] = str(int(data[i][101]) + dig1)
            elif data[i][114] == "4": #tight end
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][51] = str(int(data[i][51]) + dig1)
                data[i][54] = str(int(data[i][54]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][101] = str(int(data[i][101]) + dig1)
                data[i][60] = str(int(data[i][60]) + 2 * dig1)
            elif data[i][114] >= "5" and data[i][114] <= "9": #offensive line
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][102] = str(int(data[i][102]) + dig1)
                data[i][60] = str(int(data[i][60]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][59] = str(int(data[i][59]) + dig1)
                data[i][67] = str(int(data[i][67]) + dig1)
            elif data[i][114] == "12": #defensive tackle
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][102] = str(int(data[i][102]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][58] = str(int(data[i][58]) + 2 * dig1)
                data[i][48] = str(int(data[i][48]) + dig1)
            elif data[i][114] >= "10" and data[i][114] <= "11": #defensive end
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][102] = str(int(data[i][102]) + 2 * dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][58] = str(int(data[i][58]) + dig1)
                data[i][48] = str(int(data[i][48]) + 2 * dig1)
            elif data[i][114] == "13" or data[i][114] == "15": #OLB
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][102] = str(int(data[i][102]) + 2 * dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][58] = str(int(data[i][58]) + dig1)
                data[i][32] = str(int(data[i][32]) + 2 * dig1)
            elif data[i][114] == "14": #MLB
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][102] = str(int(data[i][102]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][58] = str(int(data[i][58]) + 2 * dig1)
                data[i][32] = str(int(data[i][32]) + dig1)
            elif data[i][114] == "16": #corners
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][54] = str(int(data[i][54]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][134] = str(int(data[i][134]) + 2 * dig1)
                data[i][135] = str(int(data[i][135]) + dig1)
            elif data[i][114] == "17" or data[i][114] == "18": #safeties
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][58] = str(int(data[i][58]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][134] = str(int(data[i][134]) + 2 * dig1)
                data[i][135] = str(int(data[i][135]) + 2 * dig1)
            elif data[i][114] >= "19": #kickers/punters
                data[i][39] = str(int(data[i][39]) + dig1)
                data[i][29] = str(int(data[i][29]) + dig1)
                data[i][54] = str(int(data[i][54]) + dig1)
                data[i][104] = str(int(data[i][104]) + dig1)
                data[i][98] = str(int(data[i][98]) + dig1)
                data[i][28] = str(int(data[i][28]) + dig1)

        # the following code makes sure no values exceed 99
            validFields = [20,56,39,29,54,104,102,87,14,58,65,140,59,60,101,51,67,48,32,134,135,98,28]
        
            for j in range(len(data[i])):
                if (j in validFields) and int(data[i][j]) >= 100:
                    data[i][j] = "99"
                if (j in validFields) and int(data[i][j]) <= 40:
                    data[i][j] = "40"
            
        else:
            pass

        print(numWorse)
        print(numBetter)

def freshmanNums(data):
    posO=[0,1,2,3,4,5,6,7,8,9,19,20]
    posD=[10,11,12,13,14,15,16,17,18,19,20]

    numQB=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    numHB=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,10,10,10,11,11,11,12,12,12,13,13,13,14,14,14,15,15,15,20,20,20,20,20,21,21,21,21,21,22,22,22,23,23,23,23,23,23,24,24,24,24,24,25,25,25,25,26,26,26,27,27,27,28,28,28,28,28,32,32,32,32,32,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,40,41,42,43,44,45]
    numWR=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,80,81,82,83,84,85,86,87,88,89,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,4,5,5,5,5,6,6,6,6,6,7,7,8,8,8,9,9,10,10,10,10,11,11,11,12,12,12,13,13,13,13,14,14,14,14,15,15,15,15,16,16,16,17,17,17,17,17,18,18,18,18,18,18,81,81,82,82,83,83,84,84,85,85,86,86,87,87,88,88,89,89,80,80]
    numTE=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30,31,32,33,40,41,42,43,44,45,46,48,49,80,81,82,83,84,85,86,87,88,89,80,81,82,83,84,85,86,87,88,89,80,81,82,83,84,85,86,87,88,89]
    numDL=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30,31,32,33,34,35,40,41,42,43,44,45,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,70,71,72,73,74,75,76,77,78,79,70,71,72,73,74,75,76,77,78,79,90,91,92,93,94,95,96,97,98,99,90,91,92,93,94,95,96,97,98,99,90,91,92,93,94,95,96,97,98,99,90,91,92,93,94,95,96,97,98,99]
    numLB=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
    numDB=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
    numK=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,69,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]
    

    #jersey num: 79
    #team id: 35
    #position: 114
    
    # first, check if player is freshman
    for i in range(1, len(data)):
        if data[i][8] == "0" and data[i][40] == "0":
            validNum = False

            if data[i][114] == "0":
                while validNum == False:
                    newNum = numQB[random.randint(0,len(numQB)-1)]
                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posO and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            #change jersey nums for freshman HBs
            elif data[i][114] == "1":
                while validNum == False:
                    newNum = numHB[random.randint(0,len(numHB)-1)]
                    #with the above line, we can now add a number to numHB multiple times
                    # to make it appear more often in the position group numbering.

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posO and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            #change jersey nums for freshman WRs
            elif data[i][114] == "3":
                while validNum == False:
                    newNum = numWR[random.randint(0,len(numWR)-1)]

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posO and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            #change jersey nums for freshman TEs
            elif data[i][114] == "4":
                while validNum == False:
                    newNum = numTE[random.randint(0,len(numTE)-1)]

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posO and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            #change jersey nums for freshman DLs
            elif data[i][114] == "10" or data[i][114] == "11" or data[i][114] == "12":
                while validNum == False:
                    newNum = numDL[random.randint(0,len(numDL)-1)]

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posD and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            #change jersey nums for freshman LBs
            elif data[i][114] == "13" or data[i][114] == "14" or data[i][114] == "15":
                while validNum == False:
                    newNum = numLB[random.randint(0,len(numLB)-1)]

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posD and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            #change jersey nums for freshman DBs
            elif data[i][114] == "16" or data[i][114] == "17" or data[i][114] == "18":
                while validNum == False:
                    newNum = numDB[random.randint(0,len(numDB)-1)]

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posD and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            elif data[i][114] == "19" or data[i][114] == "20":
                while validNum == False:
                    newNum = numK[random.randint(0,len(numK)-1)]

                    validNum = True
                    
                    #must make sure the number is available: else, do it again
                    for j in range(len(data)):
                        if (data[j][35] == data[i][35] and
                            int(data[j][114]) in posO and
                            int(data[j][114]) in posD and
                            int(data[j][79]) == newNum):
                            validNum = False
                            break
                    if validNum == True:
                        data[i][79] = str(newNum).strip()
            else:
                pass

def qbAwareness(data):

    print("\n\n\n******** QB AWARENESS MODULE ********")
    
    tier1 = [3,21,70,71]
    tier2 = [68,27,45,30,102,92,74]

    for i in range(1, len(data)):
        #tier 1 teams
        if (int(data[i][35]) in tier1 and
            data[i][114] == "0" and
            int(data[i][104]) <= 70):
            data[i][104] = str(int(data[i][104]) + random.randint(5,20))

            print("Player " + data[i][15] + " " + data[i][16] +
                      " improving.")
        #tier 2 teams
        elif (int(data[i][35]) in tier2 and
            data[i][114] == "0" and
            int(data[i][104]) <= 70):
            data[i][104] = str(int(data[i][104]) + random.randint(5,10))

            print("Player " + data[i][15] + " " + data[i][16] +
                      " improving.")
            
        validFields = [20,56,39,29,54,104,102,87,14,58,65,140,59,60,101,51,67,48,32,134,135,98,28]
            
        for j in range(len(data[i])):
            if (j in validFields) and int(data[i][j]) >= 100:
                data[i][j] = "99"

