def find_average(nums):
    # Check if the list is empty to avoid division by zero
    if not nums:
        return 0
    
    # Calculate the sum of the numbers
    total_sum = sum(nums)
    
    # Count the number of values in the list
    count = len(nums)
    
    # Calculate the mean
    average = total_sum / count
    
    return average