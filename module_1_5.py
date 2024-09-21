immutable_var = (1, 2, True, 'warrior')
print(immutable_var)
immutable_var[0] = 13 #кортежи неизменяемы, их нельзя модифицировать.
birds = [1, "cиница", "ворон", "сова", False]
birds[2] = "ястреб"
print(birds)