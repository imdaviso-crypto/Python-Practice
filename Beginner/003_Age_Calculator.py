from operator import add


print ("How old are you?")
run = input()
print ("Next year you'll be " + str(add(int(run), 1)) + " years old!")
