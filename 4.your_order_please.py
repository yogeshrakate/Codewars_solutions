'''
Your task is to sort a given string. Each word in the string
will contain a single number. This number is the position the
word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words
in the input String will only contain valid consecutive numbers.

EXAMPLES-
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
'''

def order(sentence):
    return(' '.join([i[0] for i in (sorted([[i,j] for i in sentence.split() for j in i if j.isdigit()],key=lambda x:x[1]))]))


##def order(sentence):
##    l1=[[i,j] for i in sentence.split() for j in i if j.isdigit()]
##    l1.sort(key=lambda x:x[1])
##    return(' '.join([i[0] for i in l1]))
##
##
##
##def order(sentence):
##    l=sentence.split()
##    l1=[[i,j] for i in l for j in i if j.isdigit()]
##    l1.sort(key=lambda x:x[1])
##    l2=[i[0] for i in l1]
##    return(' '.join(l2))


print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
