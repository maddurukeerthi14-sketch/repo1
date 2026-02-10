x=input("Enter a sentence: ")
dup=" "
for ch in x:
    if ch not in dup:
        dup+=ch
print("After removing duplicates ",dup)        
