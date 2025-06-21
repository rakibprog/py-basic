# Multiline string
from idlelib.colorizer import prog_group_name_to_tag

story = """My name is a rocky, i am 27 , I have a son ,
  my son name is Ebaad Ahmehd,
  he is a good boy, her age is 8 months, 
  he eats milk, vegetable, khicuri and banana"""

print(story)

#String are arrays

a = "Hello, World"
print(a[7])

#Looping through a string

for x in "banana":
 print(x)
for x in 'Tomato':
    print(x)

#string length

data = 'my name is rocky'
print(len(data))

#Check a word in phrase

name = "my name is rocky"
print('rocky' in name )


#print only if rocky is present

name = "my name is rocky"

if "rocky" in name:
    print('yes rocky is present')

