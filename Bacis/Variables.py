# first_name="Hemanth"
# last_name="A.K"
# age=23
# DOB="18-10-2003"
# email="akhemanth18@gmail.com"
# salary=100000.50
# is_present=True
# company=input("enter company name:")
# print(f"company:{company}")
# print(f"name:{first_name}.{last_name}")
# print(f"Date of birth is {DOB} and age is {age}")
# print(f"email id is:{email}")
# print(f"is he is present {is_present}")
# print(f"salary of the person is {salary}")


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


x = 5
y = "John"
print(x , y)
# print(x+y) here error occur


x = "awesome"

def myfunc():
  x = "fantastic"

myfunc()

print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
