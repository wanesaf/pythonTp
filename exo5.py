print("Runner1:")
runner1Name = input("Name: ")
runner1Time = float(input("Time (in seconds): "))
print("Runner2:")
runner2Name = input("Name: ")
runner2Time = float(input("Time (in seconds): "))

if (runner1Time == runner2Time) : 
    print(runner1Name+" and "+runner2Name+"have the same time")
else: 
  if (runner1Time < runner2Time) : 
     print("the faster runner is ",runner1Name)
  else :
     print("the faster runner is ",runner2Name)       
