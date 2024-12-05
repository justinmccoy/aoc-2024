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
				#print(f"An error occurred: {e}")
        return []


def get_reports(reports, saftey_threashold=3, window_size=2):
		try:
				if window_size < 2:
						raise ValueError("Window size must be at least 2 to detect changes.")

				safe = []
				unsafe = []

				for report in reports:
						diffs = calculate_diffs(report)

						if safe_report(report, diffs):
								safe.append(report)
						else:
								unsafe.append(report)
					
			#	if any(abs(diff) > saftey_threashold for diff in diffs):
			#		unsafe.append(report)
			#	elif all(diff > 0 for diff in diffs):
			#		safe.append(report)
			#	elif all(diff < 0 for diff in diffs):
			#		safe.append(report)
			#	else:
			#		unsafe.append(report)
		
		except Exception as e:
				print(f"An error occurred: {e}")

		return safe, unsafe



#def safe_report(report_and_deltas):
#		
#		for index, (element, diff) in enumerate(report_and_deltas):
#				print("report[{}]: {}, diff[{}]: {}".format(index, element, index, diff))
#
#		return True		


def is_increasing(a, b):
		return a < b

def is_decreasing(a, b):
		return b < a

def is_delta_above_threashold(a, b, threashold=3):
		return abs(a-b) > threashold

def safe_report(report, deltas):
		
		is_increasing=is_increasing(deltas[0])
		is_decreasing=is_decreasing(deltas[0])

		i = 0
		print(report)
		print(deltas)
		
		while i < len(deltas):
				print("{},{} diff: {}".format(report[i], report[i+1], deltas[i]))			
				i += 1
			
				if is_increasing == deltas[i]				


		return True;	

 
def sliding_window_remove(lst, condition):
		i = 0

		while i < len(lst) - 1:					#Iterate with a sliding window
				a, b = lst[i], lst[i+1]			#Pairing in Window
				if not condition(a, b):			#Check if the pair meets the condition
						lst.pop(i)							#Remove first element not conforming
						break										#Break out of loop as element removed
				else:
						i += 1									#Move to next window


def calculate_diffs(report):
		diffs = []
		for a, b in zip(report, report[1:]):
				diffs.append(b-a)
				#print("Diff {},{} = {}".format(a,b,b-a))
		return diffs



# Input the file path                                                           
file_path = input("Enter the path to the file: ")                               
                                                                                
# Read the file into two lists                                                  
lists = read_file_as_lists(file_path)

safe, unsafe = get_reports(lists)
print(len(safe))
#print(safe)
#print(unsafe)
