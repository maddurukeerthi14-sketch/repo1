n=[10,15,23,34,56,36]
even=0
odd=0
for num in n:
    if num%2==0:
        even+=1
    else:
        odd+=1       
print("Even numbers ",even)        
print("Odd numbers ",odd)