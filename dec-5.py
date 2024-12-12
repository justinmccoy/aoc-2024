import sys


def read_file_into_two_formats(file_path):
		format1, format2 = [],[]
		current_format = format1
		try:
				with open(file_path, 'r') as file:
					for line in file:
							if line.strip() == "":
								current_format = format2
								continue
							current_format.append(line.strip())
		except FileNotFoundError:
				print(f"Error: The file at '{file_path}' was not found.")
				sys.exit(1)
		except Exception as e:
				print(f"An error occurred while reading the file: {e}")
				sys.exit(1)
		return format1, format2

def extract_page_ordering_rules(rules=[]):
	tuple_list = []
	for rule in rules:
		parts  = rule.split('|')
		tuple_list.append((int(parts[0]), int(parts[1])))
	return tuple_list

def extract_page_edits(page_updates=[]):
	result = []
	for sublist in page_updates:
		int_list = []
		for num in sublist.split(","):
			try:
				int_list.append(int(num))
			except ValueError:
				print(f"Skipping invalid entry: {num}")
		result.append(int_list)
	
	return result

	

class PageBreaksPrintingRule(Exception):
     def __init__(self, value):
        super().__init__(f"Page not in rules: {value}")
        self.value = value  # Store the integer input as an attribute

def find_midpoint(lst):
    """
    Finds the midpoint value in a list.

    Parameters:
        lst (list): The input list.

    Returns:
        The midpoint value (or average of two middle values if the list length is even).
    """
    n = len(lst)
    if n == 0:
        raise ValueError("List is empty")
    
    mid_index = n // 2
    
    if n % 2 == 1:  # Odd-length list
        return lst[mid_index]
    else:  # Even-length list
        return (lst[mid_index - 1] + lst[mid_index]) / 2 if isinstance(lst[mid_index], (int, float)) else lst[mid_index - 1]


# Given a set of data and two list of rules, validate returning true/false 
def validate(edits, rules):
	for index, page in enumerate(edits):
		try:
			#find rules that match currnet edit
			matching_rules = []
			for tup in rules:
				if tup[0] == page:
					matching_rules.append(tup)

			# In the matching rules check to see if any of the pages are at a later postion 
			# in the edits.  This would break the rule
			for _, second_value in matching_rules:
				try: 
					if edits.index(second_value) < index:
						raise PageBreaksPrintingRule(int(page))
				except ValueError as ve:
					# It's ok if value isn't found, continue to read through rules
					continue
				
		except PageBreaksPrintingRule as pbpr:
				#print(f"page {page} breaks printing rule")
				return False
		except ValueError as ve:
				#print(f"Page not found in printing rules, ignore and continue: {ve}")
				continue
	return True
			
	





def main():
		default_file_path = 'Data/dec-5.test.data'

		if len(sys.argv) > 1:
				file_path = sys.argv[1]
		else:
				file_path = default_file_path

		format1, format2 = read_file_into_two_formats(file_path)
		
		page_edits = extract_page_edits(format2)
		rules = extract_page_ordering_rules(format1)

		midpoints = []

		for edits in page_edits:
			if validate(edits, rules):
				midpoints.append(find_midpoint(edits))
		

		print(sum(midpoints))

if __name__ == '__main__':
		main()
