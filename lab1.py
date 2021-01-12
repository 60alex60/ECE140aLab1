# Dockerized Lab1 python exercises

# print('Hello Docker!')


# Fill out your name, pid and github username and print.

name = 'Alex Wang'
pid = 'A15234161'
gitUserName = '60alex60'

'''
Format as follows:
Name: <name>
PID: <pid>
gitUserName: <gitUserName>
'''

# Continue with exercises below



# variable assignment and syntax
'''
list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [11.0,12.0,13.0,14.0,15.0,16.0,17.0,18.0,19.0,20.0]
list_1[0] = "one"
list_1[1] = "two"
list_1[2] = "three"
print(list_1)
tup = ("eleven","twelve","thirteen")
list_2[0], list_2[1], list_2[2] = tup
print(list_2)

joint_1 = list_1.copy()
joint_1.extend(list_2)
print(joint_1)


joint_2 = list_1 + list_2
print(joint_2)
'''

# loops
'''
actions = ["STOP","LISTEN","SLEEP","GO"]
i = 0
while i < len(actions):
    print(actions[i])
    i+=1

list2 = ["CONNECTION", "FAILURE", "BANANAS", "CONNECTION SUCCESS", "APPLES"]
text = "SUCCESS"

if("SUCCESS" in "SUCCESS"):
    print("1")
if("SUCCESS" in "ijoisafjoijiojSUCCESS"):
    print("2")
if("SUCCESS" == "ijoisafjoijiojSUCCESS"):
    print("3")
if("SUCCESS" == text):
    print("4")

i = 0
while i < len(list2):
    if(text in list2[i]):
        print("This worked!")
        break 
    else:
        print(list2[i])
        i+=1
'''
# error catching
'''
name = "alex"
byte_name = name.encode('utf-8')
byte_name_bad = byte_name + b'\xef'
# byte_name_bad.decode('utf-8')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xef in position 4: unexpected end of data

try:
    print(byte_name.decode('utf-8'))
except UnicodeDecodeError:
    print()


try:
    print(byte_name_bad.decode('utf-8'))
except UnicodeDecodeError:
    print()
'''

# functions
'''
def list_shift(base_list, new_data):
    templist = []
    if(len(new_data) > len(base_list)):
        print("new_data exceeds length of the base_list")
        return base_list
    else:
        base_list = base_list[len(new_data):len(base_list)]
        base_list += new_data
    return base_list


fixed_length_list = [1,2,3,4]
new_data = [5,6,7]
fixed_length_list = list_shift(fixed_length_list, new_data)

i=0
while i<len(fixed_length_list):
    print(fixed_length_list[i])
    i+=1

'''
# final exercise

import time
def timer():
    userInput = input("Enter a number of seconds: ")
    try: 
        userInput = int(userInput)
        i = userInput
        while i >= 0:
            time.sleep(1)
            print(i)
            i-=1
        time.sleep(1)
    except ValueError:
        print("Input must be an int")

timer()


print(name)
print(pid)
print(gitUserName)
