# This decorator function does nothing.
def do_nothing(function): 
    return function

# This is a function that adds two numbers.
def add(x, y):
	return x + y

# The decorator modifies the add function to... do nothing.
@do_nothing
def add(x, y): 
    return x + y

print('Result of calling the add function with the do nothing decorator: ',
	add(3, 4))

# The trace decorator prints out a trace of which function was called,
# and with which arguments and keyword arguments.
def trace(function):
	def wrapper(*args, **kwargs):
		print('trace: call function {}() with arguments {} and keyword arguments {}'
			.format(function.__name__, args, kwargs))
		result = function(*args, *kwargs)
		print('returned {}'.format(result))
		return result
	return wrapper 

# Now the add function not only adds, but also prints out a trace.
@trace
def add(x, y):
	return x + y

add(3, 4)