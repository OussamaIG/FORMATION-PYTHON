group_a = {"Alice", "Bob", "Jack"}
group_b = {"Asma", "Mehdi", "Oussama", "Alice"}


#Union
allgroups = group_a | group_b

#Union using union()
allgroups = group_a.union(group_b)

#Union without new variable
group_a |= group_b


#intersection using sign
inter = group_a & group_b

#intersection using method
inter = group_a.intersection(group_b)

#difference using sign
diff = group_a - group_b

#difference using method
diff = group_b.difference(group_a)
print(diff)

