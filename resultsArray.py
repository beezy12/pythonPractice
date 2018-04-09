


filename = "failedIDs.txt"                                                                                                                                                                                                                                                                                                      
file = open(filename, "r")                                                                                                                                                                                                                                                                                                         
for line in file:                                                                                                                                                                                                                                                                                                                  
    idList = line.split(',')
    #print(idList)

    #chopped = [k[6:8] for k in idList]
    for contest in idList:
        chopped = contest[6:8]
        #print(contest)
        #print(chopped)

#{:bucket=>"rical-results-dk", :key=>"00/contest-standings-55038700.zip"},
        print('{:bucket=>"rical-results-dk", :key=>"'+ chopped +'"/contest-standings-'+contest+'.zip"},')
