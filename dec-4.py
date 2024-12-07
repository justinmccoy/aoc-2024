import sys


def read_file(file_path):
		try:
				matrix = []
				with open(file_path, 'r') as file:
						for line in file:
								matrix.append(list(line.strip()))		

		except FileNotFoundError:
				print(f"Error: The file at '{file_path}' was not found.")
				sys.exit(1)
		except Exception as e:
				print(f"An error occurred while reading the file: {e}")
				sys.exit(1)
		return matrix

def main():
		default_file_path = 'Data/dec-4.test.data'

		if len(sys.argv) > 1:
				file_path = sys.argv[1]
		else:
				file_path = default_file_path

		matrix = read_file(file_path)
		
		# Example 2D Grid                                                               
		grid = [                                                                        
				['a', 'b', 'c'],                                                            
				['d', 'e', 'f'],                                                            
				['g', 'h', 'i']                                                             
		]                                                                               
                                                                                
		# Search for a string                                                           
		target = "bef"                                                                  
		found = search_in_grid(grid, target)                                            
		print(f"'{target}' found: {found}")

def search_in_grid(grid, target):
    rows, cols = len(grid), len(grid[0])
    target_len = len(target)
    
    def search_direction(x, y, dx, dy):
        # Build a string in a specific direction
        result = []
        for _ in range(target_len):
            if 0 <= x < rows and 0 <= y < cols:
                result.append(grid[x][y])
                x, y = x + dx, y + dy
            else:
                return ""
        return ''.join(result)
    
    # Check all directions: right, left, down, up, diagonals
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    for i in range(rows):
        for j in range(cols):
            for dx, dy in directions:
                if search_direction(i, j, dx, dy) == target:
                    return True
    
    return False


if __name__ == '__main__':
		main()
