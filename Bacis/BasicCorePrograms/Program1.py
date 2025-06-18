# message="Hello <<username>>,How r you!"
# name=input("Enter user name:")
# if len(name)<3:
#     name="A.K.Hemanth"

# msg=message.replace("<<username>>",name)
# print(msg)

username=input("Enter username:")
if len(username)<3:
    username="Hemanth"
message="Hello <<username>> ,How r you"
msg=message.replace("<<username>>",username)
print(msg)