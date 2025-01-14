# courses =['Python','Java','C++','C#']
#
# for index,course in enumerate( courses,start=1):
#     print(index,course)


#append en sonuna butun listeyi tek indexmis gibi ekler
#extend her biri ayri index gibi ekler

courses =['Python','Java','C++','C#']

course_str = ' - '.join(courses)
print(course_str)