'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    return ' '.join([i+'ay' if len(i)==1 and i.isalnum()==True else i[1:]+i[0]+'ay' if len(i)>1 and i.isalnum()==True else i for i in text.split()])

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
