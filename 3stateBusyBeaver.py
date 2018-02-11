from tabulate import tabulate

print("State Table for 3-State Busy Beaver Problem is: \n\n")
print (tabulate({"State":["State0","","","State1","","","State2""","",],\
                 "Symbol Read":["Blank","0","1","Blank","0","1","Blank","0","1"],\
                 "Write Instruction":["Write 1","Write Blank","Write 1","Write Blank","Write Blank","Write 1","Write 1","Write Blank","Write 1"],\
                 "MoveInstruction":["Move Tape Left","None","None","Move Tape Left","None","Move Tape Left","Move Tape Right","None","Move Tape Right"],\
                 "Next State":["State 1","State 0","Stop State","State 2","State 0","State 1","State 2","State 0","State 0"]},headers="keys"))
print("\nTape Size=10\n")

arr=['B']*10
print(arr)
print("Step by step process is as shown: \n")

def state0(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i+=1
        print(arr)
        state1(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        print(arr)

def state1(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i+=1
        print(arr)
        state2(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state1(i)

def state2(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i-=1
        print(arr)
        state2(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i-=1
        print(arr)
        state0(i)

        
state0(2)
print("\nThe following 3-state Busy Beaver Problem Takes '14 steps' and prints 'six 1s' before it haults.")
