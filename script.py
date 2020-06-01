""" File IO means we want to input something from the outside world
and output something to the outside world.

- The most common way IO is used is through reading files."""

my_file = open('test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(2)
# print(my_file.readline())
# print(my_file.readline())
# print(my_file.readline())
print(my_file.readlines())

my_file.close()
