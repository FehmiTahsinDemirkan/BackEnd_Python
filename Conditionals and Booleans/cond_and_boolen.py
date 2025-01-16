# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is (values with same id or same object)


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# condition = False
#
# if condition:
#     print('Evaluated to True')
# else:
#     print('Evaluated to False')

# language = 'python'
# if language == 'java':
#     print('language is python')
# elif language == 'python':
#     print('language is python')
# else:
#     print('language is not python')
#
# user ='admin'
# logged_in = False
# if not logged_in:
#     print('Please login')
# elif user != 'admin':
#     print('You are not admin')

a =[1,2,3]
b =[1,2,3]
b=a
print(id(a))
print(id(b))
print(a is b)