def my_generator(x):
	while x>0:
		x -= 1
		yield 1

gen_iter = my_generator(5)

print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
