"""Find Max and Min
Ask the user for numbers separated by spaces. Convert them into a list of integers and print the largest and smallest numbers."""
def prompt_numbers():
    return input('Enter your numbers separated by spaces: ')
def find_max_min():
    numbers_str = input('Enter your numbers separated by spaces: ')
    num_list = numbers_str.split()
    nums = [int(i) for i in num_list]
    return f"Largest: {max(nums)}, Smallest: {min(nums)}"

print(find_max_min())