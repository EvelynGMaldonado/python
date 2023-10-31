# LOOPS --> ability in python to do something again and again ~ a cycle of sorts

# Print "meow" three times
print("meow")
print("meow")
print("meow")

    #OR
print("meow\n" * 7, end="")

    #OR
#LOOP: While loop
i = 3
while i != 0:
    print("meow")
    i = i - 1

    #OR
#LOOP: While loop
i = 1
while i <= 3:
    print("meow")
    i = i + 1

    #OR
#LOOP: While loop
i = 0
while i < 3:
    print("meow")
    i = i + 1

    #OR
#LOOP: While loop
i = 0
while i < 3:
    print("meow")
    i += 1

#OR
#LOOP: For loop USING: list []
for i in [0, 1, 2]:
    print("meoow")

#OR
#LOOP: For loop USING: range()
for i in range(3):
    print("meow")

#OR
#LOOP: For loop USING: range() and underscore variable (_)
for _ in range(3):
    print("meooow")