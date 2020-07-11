def ParseBirdId():
    filename = input("")
    fin = open(filename, "r")
    for line in fin:eeeee
        for i in range(len(line)-5):
            testLine = line[i] + line[i+1] + line[i+2] + line[i+3] + line[i+4] 
            if testLine == "\"id\":":
                birdId=""
                k = i+7
                while line[k] != "\"":
                    birdId += line[k]
                    k+=1
                print(birdId)
    fin.close()

ParseBirdId()             
