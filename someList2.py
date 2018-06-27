from itertools import compress
from operator import itemgetter


def dcmp(k, m):
    return(bool(k ^ m) and (abs(k) > 3))


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


mylist = [1, 4, -5, 10, -7, 2, 3, -1]

pos = [n for n in mylist if n > 0]

print(pos)

pos2 = (n for n in mylist if n > 0)

print(pos2)

# pos3 = {n: val for "positif",n in mylist if n > 0}

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


# Utilisation de la fonction filer() qui passe à travers une lsite
ivals = list(filter(is_int, values))
print(ivals)


# Keeping the items for which satisfy a second list criteria
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

countpos = [0, 3, 10, 4, 1, 7, 6, 1]
countsneg = [-n for n in countpos]

print(countpos)
print(countsneg)

# Now suppose you want to make a list of all addresses
# where the corresponding count
# value was greater than 5. Here’s how you could do it:

more5 = [n > 5 for n in countpos]
more6 = [not n for n in more5]

# more7 = [x[0] for x, y in zip(more5, more6) if x[0] == y[0]]

#  more7 = [True for i, j in zip(countpos, countsneg) if abs(i) == abs(j)]

mymap = zip(countpos, countsneg)
# print(list(mymap))

more7 = [dcmp(i, j) for i, j in zip(countpos, countsneg)]


# more7 = set(map(itemgetter(0), countpos)) & set(map(itemgetter(0), countsneg))

print("More5:", more5)
print("More6:", more6)
print("More7:", more7)

print(more7.count(True) > 4)

myList2 = list(compress(addresses, more5))
print(myList2)
# ['5800 E 58TH', '4801 N BROADWAY', '1039 W GRANVILLE']
