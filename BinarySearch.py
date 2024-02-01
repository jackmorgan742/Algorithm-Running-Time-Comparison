import time

def binary_search_sum_exists(nums, target_sum):
    """
    Passes the sorted list of numbers into the binary search algorithm, 
    along with a complement number which would be the number
    that sums up to the target sum, O(nlogn)
    """
    nums.sort()
    for num in nums:
        complement = target_sum - num
        if binary_search(nums, complement):
            return True
    return False

def binary_search(nums, target_sum):
    """
    Binary search algortihm
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target_sum:
            return True
        elif nums[mid] < target_sum:
            low = mid + 1
        else:
            high = mid - 1
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
        if binary_search_sum_exists(numbers, target_sum):
            print(f"{target_sum} can be expressed as the sum of two numbers from the list.")
        else:
            print(f"{target_sum} cannot be expressed as the sum of two numbers.")

    end_time = time.time()
    time_taken = end_time - start_time

    print(f'This algorithm took {time_taken} seconds to run.')
