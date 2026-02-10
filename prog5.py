x=input("Enter a sentence: ")
vow='aeiouAEIOU'
vow_c=0
con_c=0
for ch in x:
    if ch in vow:
        vow_c+=1
    elif ch!=" ":
        con_c+=1
print("Number of vowels are ",vow_c)            
print("Number of consonants are ",con_c)