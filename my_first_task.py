# a function to find how many prime numbers are in a list
def task_1(
        nums):
    # an empty list to add prime numbers to it
    prime_number = []
    # check if the index in the list is prime
    for the_index in nums:
        is_prime = True
        # if the number is less than 2 its not gonna be prime
        if the_index < 2:
            is_prime = False
        # loop for checking if the number is prime
        for counter in range(2, the_index):

            if (the_index % counter) == 0:
                is_prime = False
                break
        # Creating a list with just prime numbers
        if is_prime:
            prime_number.append(the_index)
    # Returning the count of the prime numbers
    return prime_number.count

