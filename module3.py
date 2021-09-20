import random

def getOvrRank(data, x): #x is the top number of OVRs you want
    # list of used player id's
    players = []
    
    for i in range(x):
        maxOvr = data[1][103]
        plr = 0
        
        for j in range(1,len(data)):
            if data[j][103] > maxOvr and (j not in players):
                maxOvr = data[j][103]
                plr = j
        
        players = players + [plr]
    return players

def betterPlayersLeaving(data):
    print("\n\n\n******** PLAYERS LEAVING MODULE ********")
    
    ovrList = getOvrRank(data, 224)

    for i in range(1,len(data)):
        dn = random.randint(1,100)
        # if player is RS SO, must be top 100 overalls
        if data[i][40] == "2" and data[i][8] == "1":
            if i in ovrList[0:100]:
                if dn <= 60:
                    print("Player " + data[i][15] + " " + data[i][16] +
                      " (" + data[i][8] + ")" + " leaving. OVR: " +
                      data[i][103])
                    data[i][8] = "3"
                    data[i][40] = "2"
                
        # if player is RS JR
        elif data[i][40] == "2" and data[i][8] == "2":
            if i in ovrList[0:224]:
                if dn <= 100:
                    print("Player " + data[i][15] + " " + data[i][16] +
                      " (" + data[i][8] + ")" + " leaving. OVR: " +
                      data[i][103])
                
                    data[i][8] = "3"
                    data[i][40] = "2"
                
        # if player is JR
        elif data[i][8] == "2":
            #check if player's overall is high enough
            if i in ovrList[0:160]:
                if dn <= 80:
                    print("Player " + data[i][15] + " " + data[i][16] +
                      " (" + data[i][8] + ")" + " leaving. OVR: " +
                      data[i][103])
                    data[i][8] = "3"
                    data[i][40] = "2"
                
            
