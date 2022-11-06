rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):                  #Upper head H
    for space in range(1, (rows-i)+1):
        print(end= "  ")
   
    while k!=(2*i-1):
        print("H ", end="")
        k += 1
   
    k = 0
    print()

                   
for i in range(rows +1):                                #middle upper part
    print((rows-2)*" ",rows*'H ',(rows*3)*" ",rows*'H ')
    
for j in range(rows-2):                                 #middle middle
    print((rows-2)*" ",((rows)+(rows*3))*'H ')
        
for i in range(rows +1):                                #middle lower part
    print((rows-2)*" ",rows*'H ',(rows*3)*" ",rows*'H ')



for i in range(rows+1, 1, -1):                            #lower head H
    print((rows-4)*" ",rows*"  ",(rows*3)*" ",end="")
    for space in range(0,1+rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("H ", end="")
    for j in range(1, i-1):
        print("H ", end="")
    print()
    
    
    
    
    
    
    
    
    