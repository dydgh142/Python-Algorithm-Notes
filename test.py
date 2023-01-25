
input = [2,2,2,5,5,5,7,7,7,7,7,7,9,9,11,11,11,11,11,11]
 
max_input = max(input)
my_list = [0] * max_input

for i in input:
  my_list[i-1] += 1

max1 = max(my_list)



print(max1)
