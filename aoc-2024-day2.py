def read_file_as_lists(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines and split each line into a list of numbers
            lines_as_lists = []
            for line in file:
                if line.strip():  # Skip empty lines
                    try:
                        # Convert each line into a list of floats or integers
                        numbers = list(map(int, line.split()))
                        lines_as_lists.append(numbers)
                    except ValueError:
                        print(f"Skipping invalid line: {line.strip()}")
            return lines_as_lists
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []



def get_reports(reports, saftey_threashold=3, window_size=2, problem_dampener=True):
		
		if window_size < 2:
				raise ValueError("Window size must be at least 2 to detect changes.")

		safe = []
		unsafe = []

		for report in reports:
				if len(report) < window_size:
						unsafe.append(report)  # Treat too-short reports as unsafe
						continue

				diffs = [b - a for a, b in zip(report,report[1:])]
				
				if any(abs(diff) > saftey_threashold for diff in diffs):
					unsafe.append(report)
				elif all(diff > 0 for diff in diffs):
					safe.append({"report": report, "status": "increasing"} if problem_dampener else report)
				elif all(diff < 0 for diff in diffs):
					safe.append({"report": report, "status": "decreasing"} if problem_dampener else report)
				else:
					unsafe.append(report)
		
		return safe, unsafe					


# Input the file path                                                           
file_path = input("Enter the path to the file: ")                               
                                                                                
# Read the file into two lists                                                  
lists = read_file_as_lists(file_path)

safe, unsafe = get_reports(lists)
print(safe)
print(unsafe)
