
final_ones = 42
final_zeros = 131
total_symbols = 900

left_ones = final_ones - 1 
left_zeros = final_zeros 
processed_length = left_ones + left_zeros + 1 
erased_ones = total_symbols - processed_length
initial_ones = left_ones + erased_ones

print(initial_ones)
