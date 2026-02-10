x=input("Enter a sentence: ")
vow='aeiouAEIOU'
for ch in x:
    if ch in vow:
        print(ch,end=" ")