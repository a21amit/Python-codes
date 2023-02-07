file=open('<file_path>','r')
f=file.read()
vowel=0
consonant=0
upper=0
lower=0


for a in f:
        if a.isalpha():
            if a == "a" or a == "A" or a == "e" or a == "E" or a == "i" or a == "I" or a =="u" or a == "U" or a=="o" or a ==" O":
                vowel+=1
            else:
                consonant+=1
        if a.isupper():
            upper+=1
        elif a.islower():
            lower+=1
file.close()

#printing messages
print(vowel, 'are total vowel in file.')
print(consonant, 'are total consonant in file.')
print(upper, 'are total uppercase in file.')
print(lower, 'are total lowercase in file.')
