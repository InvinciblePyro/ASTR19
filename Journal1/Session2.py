import random
num_float_1 = round(random.random(), 2)
num_float_2 = round(random.random(), 2)
num_int_1 = random.randint(1, 10)
num_int_2 = random.randint(1, 10)
print(f"{num_float_1} + {num_float_2} = {round((num_float_1 + num_float_2), 2)} {type(round((num_float_1 + num_float_2), 2))}")
print(f"{num_int_1} - {num_int_2} = {round((num_int_1 - num_int_2), 2)} {type(round((num_int_1 - num_int_2), 2))}")
print(f"{num_float_1} + {num_int_1} = {round((num_float_1 + num_int_1), 2)} {type(round((num_float_1 + num_int_1), 2))}")