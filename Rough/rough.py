lis=[0,1]

n=int(input())

if n==1:
    print(lis[0])
elif n==2:
    print(lis[0],lis[1])
elif n>2:
    for i in range(2,n):
        y=lis[i-1]+lis[i-2]
        list.append(y)
    for j in range(n):
        print    
        
        
        
    
    