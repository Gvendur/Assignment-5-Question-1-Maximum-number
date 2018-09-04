temp_num = 0
while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if(num_int < 0):
        break
    if(temp_num <= num_int):
        temp_num = num_int
    # Fill in the missing code
max_int = temp_num
print("The maximum is", max_int)    # Do not change this line
