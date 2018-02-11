from tabulate import tabulate

print("State Table for 5-State Busy Beaver Problem is: \n\n")
print (tabulate({"State":["State0","","State1","","State2","","State3","","State4",""],\
                 "Symbol Read":["0","1","0","1","0","1","0","1","0","1"],\
                 "Write Instruction":["Write 1","Write 1","Write 0","Write 0","Write 1","Write 1","Write 1","Write 1","Write 0","Write 0"],\
                 "MoveInstruction":["Move Tape Right","Move tape left","Move tape left","Move Tape Left","Move tape left","Move Tape Left","Move Tape Right","Move tape right","Move Tape Right"],\
                 "Next State":["State 1","State 2","State 0","State 3","State 0","Stop State","State 1","State 4","State 3","State 1"]},headers="keys"))
print("\nTape Size=6000\n")

arr=['0']*6000
print(arr)
print("Step by step process is as shown: \n")

def state0(i):
    if(arr[i]=='0'):
        arr[i]='1'
        i+=1
        print(arr)
        state1(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i-=1;
        print(arr)
        state2(i)
    

def state1(i):
    if(arr[i]=='0'):
        arr[i]='0'
        i-=1
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='0'
        i-=1;
        print(arr)
        state3(i)
    

def state2(i):
    if(arr[i]=='0'):
        arr[i]='1'
        i-=1
        print(arr)
        state1(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i-=1;
        print(arr)
        state0(i)
def state3(i):
    if(arr[i]=='0'):
        arr[i]='1'
        i-=1
        print(arr)
        state1(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1;
        print(arr)
        state4(i)
    

def state4(i):
    if(arr[i]=='0'):
        arr[i]='0'
        i+=1
        print(arr)
        state3(i)
    elif(arr[i]=='1'):
        arr[i]='0'
        i+=1;
        print(arr)
        state1(i)
    

        
state0(2)
print("\nThe following 5-state Busy Beaver Problem Takes '47,176,870 steps' and prints '4098 1s' before it haults.")
