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



def get_reports(reports, saftey_threashold=3, window_size=2):
		safe = []
		unsafe = []
		
		if window_size < 2:
				print("Window size must be at least 2 to detect changes.")
				return safe, unsafe

		for report in reports:
				diffs = []	
				for i in range(len(report) - window_size + 1):
						window = report[i:i + window_size]
						for j in range(len(window) - 1):
								diffs.append(window[j + 1] - window[j])
								#print("Report {}, window[{},{}], diff {}".format(report, window[j+1], window[j], window[j+1] - window[j]))	
				if any(abs(diff) > saftey_threashold for diff in diffs):
						unsafe.append(report)
				elif all(diff > 0 for diff in diffs):
						safe.append(report)
				elif all(diff < 0 for diff in diffs):
						safe.append(report)
				else:
						unsafe.append(report)	
			
		return safe, unsafe					


# Input the file path                                                           
file_path = input("Enter the path to the file: ")                               
                                                                                
# Read the file into two lists                                                  
lists = read_file_as_lists(file_path)

safe, unsafe = get_reports(lists)
print(len(safe))
