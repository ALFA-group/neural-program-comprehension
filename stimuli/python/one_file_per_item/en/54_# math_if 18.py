bears, dogs, wolves = 10, 4, 16

if (bears > dogs) and (bears > wolves):
    print(wolves)
elif (dogs > bears) and (dogs > wolves):
    print(bears)
elif (wolves > bears) and (wolves > dogs):
    print(dogs)

