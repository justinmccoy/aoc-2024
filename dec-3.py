import sys
import re

def read_file(file_path):
		try:
				with open(file_path, 'r') as file:
						return file.readlines()
		except FileNotFoundError:
				print(f"Error: The file at '{file_path}' was not found.")
				sys.exit(1)
		except Exception as e:
				print(f"An error occurred while reading the file: {e}")
				sys.exit(1)


def main():
		default_file_path = 'Data/day3-1.test.data'

		if len(sys.argv) > 1:
				file_path = sys.argv[1]
		else:
				file_path = default_file_path

		lines = read_file(file_path)

		total = 0
		for line in lines:
				total += sum(mul_pairs(extract_mul_expression(line.strip())))
		
		print(total)

# Requires import re
def extract_mul_expression(input_string):
		pattern = r'mul\((\d{1,3}+),(\d{1,3}+)\)'
		matches = re.findall(pattern, input_string)
		return matches

def mul_pairs(pairs):
		products = [int(a) * int(b) for a, b in pairs]
		return products


if __name__ == '__main__':
		main()
