from tabulate import tabulate

print("State Table for 7-state Unary Subtractor Problem is: \n\n")
print (tabulate({"State":["State0","","","State1","","","State2","","","State3","","","State4","","","State5","","","State6","","","State7"],\
                 "Symbol Read":["Blank","0","1","Blank","0","1","Blank","0","1","Blank","0","1","Blank","0","1","Blank","0","1","Blank","0","1","Blank","0","1"],\
                 "Write Instruction":["Write Blank","Write 0","Write 1","Write Blank","Write 0","Write 1","Write Blank","Write 0","Write 0","Write Blank","Write 0","Write 1","Write Blank","Write 0","Write 1","Write Blank","Write Blank","Write 1","Write Blank","Write Blank","Write 1","Write Blank","Write 0","Write 0"],\
                 "MoveInstruction":["Move Tape Left","Move Tape Left","Move Tape Left","Move Tape Right","Move Tape Left","Move Tape Left","Move Tape Left","Move Tape Right","Move Tape Right","Move Tape Right","Move Tape Right","Move Tape Right","Move Tape Right","Move Tape Left","Move Tape Left","Move Tape Right","Move Tape Right","Move Tape Right","Move Tape Left","Move Tape Right","Move Tape Right","Move Tape Left","Move Tape Right","Move Tape Left"],\
                 "Next State":["State 1","State 0","State 0","State 2","State 1","State 1","State 4","State 2","State 3","State 7","State 3","State 3","State 5","State 4","State 4","State 6","State 5","State 5","Stop State","State 6","State 6","Stop State","State 7","State 0"]},headers="keys"))
print("\nTape Size=10\n")

arr=['B']*10
print(arr)
print("Step by step process is as shown: \n")
def state0(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i+=1
        print(arr)
        state1(i)
    elif(arr[i]=='0'):
        arr[i]='0'
        i+=1
        print(arr)
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state0(i)

def state1(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i-=1
        print(arr)
        state2(i)
    elif(arr[i]=='0'):
        arr[i]='0'
        print(arr)
        i+=1
        state1(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state1(i)

def state2(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i+=1
        print(arr)
        state4(i)
    elif(arr[i]=='0'):
        arr[i]='0'
        print(arr)
        i-=1
        state2(i)
    elif(arr[i]=='1'):
        arr[i]='0'
        i-=1
        print(arr)
        state3(i)

def state3(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i-=1
        print(arr)
        state7(i)
    elif(arr[i]=='0'):
        arr[i]='0'
        print(arr)
        i-=1
        state3(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i-=1
        print(arr)
        state3(i)

def state4(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i-=1
        print(arr)
        state5(i)
    elif(arr[i]=='0'):
        arr[i]='0'
        print(arr)
        i+=1
        state4(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state4(i)


def state5(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i-=1
        print(arr)
        state6(i)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        i-=1
        state5(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i-=1
        print(arr)
        state5(i)

def state6(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i+=1
        print(arr)
    elif(arr[i]=='0'):
        arr[i]='B'
        print(arr)
        i-=1
        state6(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i-=1
        print(arr)
        state6(i)

def state7(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i+=1
        print(arr)
    elif(arr[i]=='0'):
        arr[i]='0'
        print(arr)
        i-=1
        state7(i)
    elif(arr[i]=='1'):
        arr[i]='0'
        i+=1
        print(arr)
        state0(i)

print("Enter the smaller number in unary format:  ")
n1=list(input())
print("Enter the larger number in unary format:  ")
n2=list(input())
for i in range (len(n2)):
    arr[i]='1'
for j in range(i+2,len(n1)+i+2):
    arr[j]='1'

print(arr)
state0(0)

print("The answer is: ",arr.count('1'))



