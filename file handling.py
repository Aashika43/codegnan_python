#file handling
#write()
'''a=open("aashika.txt","w")
a.write("python")
a.close()'''

'''a=open("aashika.txt","w")
a.write("java")
a.close()'''

#append()
'''a=open("aashika.txt","a")
a.write("\taashika")
a.close()'''

'''a=open("aashika.txt","w")
a.write(input("data"))
a.close()'''

'''a=open("aashika.txt","a")
a.write(input("data"))
a.close()'''

#readlines()
'''a=open("aashika.txt")
#print(a.read())#it will display entire content
#print(a.readline())#it will display first line
#print(a.readlines())#it will display with \n
print(a.read(8))#it will display with no.of charectors'''

#writelines()->it makes every object side by side
'''a=open("aashika.txt","w")
b=["python","java","c","c++","html"]
a.writelines("\n".join(b))
a.close()'''

'''a=open("file handling.py")
print(a.read())'''

'''a=open("C:\\Users\\lenovo\\OneDrive\\Desktop\\python 127\\aashika.txt")
print(a.read())'''

#Task
#Student Profile
stu_id=input('Enter your ID: ')
name=input('Enter your name: ')
phno=int(input('Enter your phno: '))
mail=input('Enter your mailID: ')
clg=input('Enter your college name: ')
branch=input('Enter your branch: ')
print('\n\tStudent Details')
print(f'Student ID: {stu_id}')
print(f'Student Name: {name}')
print(f'Student Phone number: {phno}')
print(f'Student Mail ID: {mail}\n')
print(f'Student College Name: {clg}')
print(f'Student Branch: {branch}')

