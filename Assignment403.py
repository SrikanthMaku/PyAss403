# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list: [16, 25, 4, 81]



number = [4,5,2,9]
def square(x):
   return x*x 

square_num = map(square, number)
print(list(square_num))








