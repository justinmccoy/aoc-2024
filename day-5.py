import sys


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

		for line in lines:
				print(line.strip())


if __name__ == '__main__':
		main()
