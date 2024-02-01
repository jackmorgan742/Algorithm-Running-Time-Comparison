import time

def brute_force_sum_exists(nums, target_sum):
    """
    Brute force algorithm that takes a list of integers and a sum integer, x
    returns a print statement if x can or cannot be expressed as the sum of 2 numbers in nums
    """

    for i in range(len(nums)):             
        for j in range(len(nums)):                       
            if nums[i] + nums[j] == target_sum:         #tests the sum of every combination in the list and compares it with the target sum O(n^2)
                return True
    return False



if __name__ == '__main__':

    #opens the .txt file and puts the numbers from it into a list
    with open(r"C:\Users\patri\Downloads\CSE 3500\hw2\CollectionNumbers\listNumbers-10000.txt", 'r') as file:
        numbers = [int(line.strip()) for line in file]

    #opens the sums .txt file and puts the numbers from it into a list
    with open(r"C:\Users\patri\Downloads\CSE 3500\hw2\CollectionNumbers\listNumbers-10000-nsol.txt", 'r') as file:
        sums = [int(line.strip()) for line in file]

    start_time = time.time()

    #checks each sum in the file
    for target_sum in sums:
        if brute_force_sum_exists(numbers, target_sum):
            print(f"{target_sum} can be expressed as the sum of two numbers from the list.")
        else:
            print(f"{target_sum} cannot be expressed as the sum of two numbers.")

    end_time = time.time()
    time_taken = end_time - start_time

    print(f'This algorithm took {time_taken} seconds to run.')
