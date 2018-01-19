
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else :
        return 'Hello'

print (greet('en') , 'Glenn')
print (greet('es') , 'Sally')
print (greet('fr') , 'Michael')

big = max('hello world')
print(big)




def addtwo(a , b):
    added = a + b
    return added

x = addtwo(3 , 5)
print (x)

def func(x) :
    print(x)

func(10)
func(20)



def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)
