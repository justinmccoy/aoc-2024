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
	list1, list2 = [], []
	for rule in rules:
		try:
			num1, num2 = map(int, rule.split('|'))
			list1.append(num1)
			list2.append(num2)
		except ValueError:
			print(f"Skipping invalid line: {rule.strip('|')}")
		except Exception as e:
			print(f"An error occurred: {e}")
	return list1, list2

# Given a set of data and two list of rules, validate and return middle or -1
def validate(edits, list1=[], list2=[]):
	printed = []

	for page in edits:
		print(page)
	return -1




def main():
		default_file_path = 'Data/dec-5.test.data'

		if len(sys.argv) > 1:
				file_path = sys.argv[1]
		else:
				file_path = default_file_path

		rules, updates = read_file_into_two_formats(file_path)
		list1, list2 = extract_page_ordering_rules(rules)

		for update in updates:
			update_list = update.split(',')
			middle = validate(update_list, list1, list2)

		print(updates)
		print(list1)
		print(list2)


if __name__ == '__main__':
		main()
