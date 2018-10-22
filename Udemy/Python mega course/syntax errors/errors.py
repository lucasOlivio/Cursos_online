#syntax errors
'''
print(1)
int(9)
int 9
print(2)
print 2
'''

#runtime errors
'''
a = 1
b = "2"
print(int(2.5)
print(a+b)
'''

#Fix dificult errors GOOGLE IT!
'''
a = 1
b = "2"
c = 3
print(int(2.5))
print(c/0)
'''

'''
Asking a good programming question:

- Detailed title for the question, including error message
- Include the code
- Describre what you where expecting

ex: "Hi, in the last exercice i got an error message while trying to divide in the code:"
*includes the code*
*includes all the the error message*

- Highlight code and error
'''

#Handling errors - Exceptions
def divide(a,b):
    try:
        return a/b
    except:
        return "Numbers not accepted!"

print(divide(1,0))
