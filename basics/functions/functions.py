PARAMETR = True
VALUE = 100
x = 0

if PARAMETR:
	def get_rect(a, b):
		return f'Периметр: {2 * (a + b)}'
else:
	def get_rect(a, b):
		return f'Площадь: {a * b}'


def fun(fact, *args, formal_arg=False, **kwargs):
	# фактические аргументы должны идти перед *args
	# формальные аргументы должны идти перед **kwargs
	print(args)

def glob_value():
	global VALUE
	VALUE += 10
	print(VALUE)


def outer():
	global x
	x = 1
	def inner():
		# nonlocal x
		x = 2
		print(f'Inner: {x}')

	inner()
	print(f'Outer: {x}')


def say_name(value):
	def say_goodbye():
		print(f'Goodbye: {value}')
	return say_goodbye

if __name__ == '__main__':
	# print(get_rect(5, 6))

	# fun('fact arg', 1, (2, 3, 4), 'str', arg1=[1, 2, 3], arg2={1, 2}, formal_arg=True)

	# glob_value()
	# outer()
	# print(f'Global: {x}')

	f = say_name('Victoria')
	f()
