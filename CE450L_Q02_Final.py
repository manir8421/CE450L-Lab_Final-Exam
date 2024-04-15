def find_prime(number):                                                 # define function find_prime with attribute number                                                                                                                                                        
    if number <= 1:                                                     # if number is less than or equal to 1, return false
        return False
    if number <= 3:                                                     # if number is less than or equal to 3, return true
        return True
    if number % 2 == 0 or number % 3 == 0:                              # if number is divisible by 2 or 3, return false
        return False
    i = 5  
    while i * i <= number:                                              # while i is less than or equal to the square root of number
        if number % i == 0 or number % (i + 2) == 0:                    # if number is divisible by i or i + 2, return false 
            return False
        i += 6
    return True

def find_prime_in_range(calc_limit):                                    # define function find_prime_in_range with attribute calc_limit
    pair = []                                                           # create empty list pair 
    for i in range(2, calc_limit):                                      # for i in range 2 to calc_limit 
        if find_prime(i) and find_prime(i + 2):                         # if i and i + 2 are prime, append i and i + 2 to pair
            pair.append((i, i + 2))                                     # append i and i + 2 to pair 
    return pair                                                         # return pair 

if __name__ == "__main__":
    calc_limit = int(input("Type a number less than 10000: "))          # user to enter a number less than 10000
    if calc_limit >= 10000:     
        print("Please enter a number less than 10000.")                 # if user enters a number greater than 10000, print error message
    else:
        print("All pairs within input range:")                          # print all pairs within input range
        pairs = find_prime_in_range(calc_limit)                         # call function find_prime_in_range with attribute calc_limit
        for pair in pairs:                                              # for pair in pairs 
            print(f"{pair[0]} {pair[1]}")                               # print pair[0] and pair[1]
