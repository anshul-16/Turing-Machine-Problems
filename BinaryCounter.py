from tabulate import tabulate

print("State Table for 3-State Binary counter Problem is: \n\n")
print (tabulate({"State":["State0","","","State1","","","State2""","",],\
                 "Symbol Read":["Blank","0","1","Blank","0","1","Blank","0","1"],\
                 "Write Instruction":["Write Blank","Write 0","Write 1","Write 1","Write 1","Write 0","Write Blank","Write 0","Write 1"],\
                 "MoveInstruction":["Move Tape Right","Move Tape Left","Move Tape Left","Move Tape Left","Move Tape Right","Move Tape Right","Move Tape Right","Move Tape Left","Move Tape Left"],\
                 "Next State":["State 1","State 0","State 0","State 2","State 2","State 1","Stop State","State 2","State 2"]},headers="keys"))
print("\nTape Size=10\n")
arr=['B']*10
print(arr)
print("Enter your input")
string=input()
l=len(string)
p=10
k=p-l
j=0
arr=['','','','','','','','','','']
for i in range(0,10):
    if(i<k):
        arr[i]='B'
    else:
        arr[i]=string[j]
        j=j+1
print("Step by step process is as shown: \n")
def state0(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i-=1
        print(arr)
        state1(i)
    elif(arr[i]=='0'):
        arr[i]='0'
        print(arr)
        i+=1
        state0(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state0(i)

def state1(i):
    if(arr[i]=='B'):
        arr[i]='1'
        i+=1
        print(arr)
        state2(i)
    elif(arr[i]=='0'):
        arr[i]='1'
        i-=1
        print(arr)
        state2(i)
    elif(arr[i]=='1'):
        arr[i]='0'
        i-=1
        print(arr)
        state1(i)

def state2(i):
    if(arr[i]=='B'):
        arr[i]='B'
        i-=1
        print(arr)
    elif(arr[i]=='0'):
        arr[i]='0'
        i+=1
        print(arr)
        state2(i)
    elif(arr[i]=='1'):
        arr[i]='1'
        i+=1
        print(arr)
        state2(i)
state0(0)



    
