import pandas as pd

def element_inside(data, element):
    for i in data:
        if i[0] == element: 
            return True
    return False

processesSheet = pd.read_excel('22new.xlsx', sheet_name='N1')

idA = processesSheet['idA'].tolist()
idB = processesSheet['idB'].tolist()
time = processesSheet['Time'].tolist()

#conversing columns into lists

fullList = []

for i in range(len(idB)):
    idA[i] = list(map(int, str(idA[i]).split(';'))) #in excel sheet parent processes are divided by ';' and if there are only one parent process, panda interprets it as 'int'
    fullList.append([idB[i], time[i], idA[i]])

#making list of all processes including ids, time for running and parent processes [[idA, time, [parentprocess1, parentprocess2, ...]], ...]

finishedProcesses = [[0]] #skill issue(bad design): element with id == 0 must be in already finished because it is 'no parents' sign
                            #it is inside another list because element_inside can only find elements inside 2 dimensional massives

timeElapsed = 0 #milliseconds

while len(fullList) != 0:
    #print(finishedProcesses, fullList, '', sep='\n')
    
    maxTime = 0
    for process in fullList:
        
        isProcessable = True
        parents = process[2]
        
        for parent in parents:
            
            if not element_inside(finishedProcesses, parent):
                isProcessable = False                           #trying to find parents inside of finished processes
        
        if isProcessable:
            time = process[1]
            
            if time > maxTime:
                maxTime = time                  #check maxTime for parallel processes
            
            finishedProcesses.append(process)
            fullList.remove(process)
            
    timeElapsed += maxTime

print(timeElapsed)
                
            
                
        
    