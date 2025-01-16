def hello_func(greating,name='you'):
    return '{},{}'.format(greating,name)

# print(hello_func("hi",'fehmi'))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses = ['Math','art']
info ={'name':'fame','age':22}
# student_info('Math','art',name='fame',age=22)
student_info(*courses,**info)