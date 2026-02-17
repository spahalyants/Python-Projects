number = 1000
name = "Samvel"
fl_num = 7.55
isSmart = True

####################

if isSmart:
    print(name)

elif number > 100:
    print("number")

else:
    print(fl_num)

####################

if not isSmart:
    print(name)

elif number > 100:
    print("number")

else:
    print(fl_num)

####################

if isSmart and number > 100:
    print(fl_num)

print(not isSmart)


