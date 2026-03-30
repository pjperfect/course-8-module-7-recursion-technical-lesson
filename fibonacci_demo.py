def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_debug(n, depth = 0):
	print("  " * depth + f"fibonacci({n}) called")
	if n == 0:
		print("  " * depth + "return 0")
		return 0
	elif n == 1:
		print("  " * depth + "return 1")
		return 1
    
	val = fibonacci_debug(n - 1, depth + 1) + fibonacci_debug(n - 2, depth + 1)
	print("  " * depth + f"return {val} for fibonacci({n})")
	return val

if __name__ == "__main__":
	print(fibonacci(0))  # Expected 0
	print(fibonacci(1))  # Expected 1
	print(fibonacci(5))  # Expected 5 (sequence: 0,1,1,2,3,5)
	print(fibonacci(7))  # Expected 13 (sequence: 0,1,1,2,3,5,8,13)
	fibonacci_debug(5)
	