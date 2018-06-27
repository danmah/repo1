import re
import string
import sys


line = 'asdf fjdk; afed, fjek,asdf, foo'
myList = re.split(r'(?:,|;|\s)\s*', line)
print(myList)

# And now for something really different
# i.e. sans le ? qui consomme l'extrat
myList = re.split(r'(:,|;|\s)\s*', line)
print(myList)

mySlice = slice(0, 15, 2)

txt = "Les gens ont beaucoup de choses à dire"

# print(txt[mySlice])

userStr = input('Entrez une chaîne SVP: ')
revStr = userStr[::-1]  # str(reversed(userStr))
revStr2 = ''.join(list(reversed(userStr)))

if userStr == revStr:
    print("Hourra!, " + userStr + " est un palindrome.")
else:
    print("Câlisse, force-toé un peu pour entrer un palindrome!")
    print(userStr)
    print(revStr)
    print(revStr2)


