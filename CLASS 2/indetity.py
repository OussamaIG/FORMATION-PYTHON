#create a array called tab
Tab = [1,2,3,4,5,6,7,8,9]

# create a new variable that points to the same array
newTab = Tab

# create a new variable that is a copy of the array
TAB2 = Tab[:]

# check if the two variables point to the same array
print(Tab is newTab)

print(Tab is TAB2)

print(Tab == TAB2)


