# The Big Man, aka our Chief Historian is missing!
# 
# Each location has a unique number that is LOCATION_ID
# You are given two lists and must reconcile the ordering of LOCATION_IDs
# You must:
#   Pair up the numbers and measure the distance between the two numbers
#   Order the list of LCOATION_IDs in right list (RL) and left list (LL):
#   where the smallest number in RL is first paired with the smallest number
#   in the LL and iterate until traversing both lists.  We can call this 
#   the location_Shuffle(list)
#   
#   After we have all the LOCATION_IDs rearranged in the correct order 
#   iterate through and calculate difference between all the locations.
#   

LOCATION_ID_DATA = "Data/day1-1.data"


def read_file_into_lists(file_path):
    list1, list2 = [], []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if not line.strip():
                    continue  # Skip empty lines
                try:
                    # Split the line into two numbers
                    num1, num2 = map(int, line.split())
                    list1.append(num1)
                    list2.append(num2)
                except ValueError:
                    print(f"Skipping invalid line: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return list1, list2
  


def combine_sorted_lists(list1, list2):
    # Sort both lists
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    # Combine the lists into tuples
    paired_list = list(zip(sorted_list1, sorted_list2))
    return paired_list


def calculate_deltas(paired_list):
	deltas = [abs(a-b) for a, b in paired_list]
	return sum(deltas)
	

# Input the file path
file_path = input("Enter the path to the file: ")

# Read the file into two lists
list1, list2 = read_file_into_lists(file_path)

# Combine the sorted lists into a list of tuples
paired_list = combine_sorted_lists(list1, list2)

deltas = calculate_deltas(paired_list)

# Print the result
print("Total distance between lists: ", deltas)
