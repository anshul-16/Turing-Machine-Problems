from tabulate import tabulate

print("State Table for 4-State Busy Beaver Problem is: \n\n")
print (tabulate({"State":["State0","","","State1","","","State2","","","State3","","",],\
                 "Symbol Read":["Blank","0","1","Blank","0","1","Blank","0","1","Blank","0","1"],\
                 "Write Instruction":["Write 1","Write Blank","Write 1","Write 1","Write Blank","Write Blank","Write 1","Write Blank","Write 1","Write 1","Write Blank","Write Blank"],\
                 "MoveInstruction":["Move Tape Right","None","Move Tape Left","Move Tape Left","None","Move Tape Left","Move Tape Right","None","Move Tape Left","Move Tape Right","None","Move Tape Right"],\
                 "Next State":["State 1","State 0","State 1","State 0","State 0","State 2","Stop State","State 0","State 3","State 3","State 0","State 0"]},headers="keys"))
print("\nTape Size=18\n")

arr=['B']*18
print(arr)
print("Step by step process is as shown: \n")

def state0(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i-=1
        print(arr)
        state1(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state1(i)

def state1(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i+=1
        print(arr)
        state0(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='B'
        i+=1
        print(arr)
        state2(i)

def state2(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i-=1
        print(arr)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state3(i)

def state3(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i-=1
        print(arr)
        state3(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='B'
        i-=1
        print(arr)
        state0(i)
        
state0(2)
print("\nThe following 4-state Busy Beaver Problem Takes '107 steps' and prints '13 1s' before it haults.")
