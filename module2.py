import random
import names

def fixDuplicates(data):
    for i in range(1,len(data)):
        # check for duplicate names
        if data[i][14] == data[i][15]:
            data[i][15] = names.get_last_name()

def generateSuffixes(data):
    for i in range(1, len(data)):
        suf = random.randint(1,300)
        
        if suf == 1:
            suf1 = random.randint(1,4)

            if suf1 == 1:
                data[i][15] = data[i][15] + " Jr"
            elif suf1 == 2:
                data[i][15] = data[i][15] + " II"
            elif suf1 == 3:
                data[i][15] = data[i][15] + " III"
            else:
                data[i][15] = data[i][15] + " IV"

def generateHyphens(data):
    for i in range(1, len(data)):
        suf = random.randint(1,300)
        
        if suf == 2:
            secondName = data[i][15]
            while secondName == data[i][15]:
                secondName = names.get_last_name()
            data[i][15] = data[i][15] + "-" + secondName

def awarenessBoost(data):
    for i in range(1, len(data)):
        if data[i][23] == "3":
            awrBoost = random.randint(1,10)
            if awrBoost == 1:
                newAwr = random.randint(0,20)
                data[i][96] = str(int(data[i][96]) + newAwr)
        elif data[i][23] == "4":
            awrBoost = random.randint(1,10)
            if awrBoost <= 5:
                newAwr = random.randint(0,20)
                data[i][96] = str(int(data[i][96]) + newAwr)
        elif data[i][23] == "5" or data[i][8] >= "1":
            newAwr = random.randint(0,20)
            data[i][96] = str(int(data[i][96]) + newAwr)

        if int(data[i][96]) >= 100:
                data[i][96] = "99"

        
