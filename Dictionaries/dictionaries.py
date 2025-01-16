
student ={'name':'jhon','age':20,'courses':['python','java']}
# student.update({'name':'jane','age':24,'phone':'112321321'})# print(student.get('number','not found')) #icinde yoksa not found yaz key value hatasi almak yerine
# age =student.pop('age')
# print(age)
print(student)


for key,value in student.items():
    print(key,value)