try:
    print (x)
except NameError:
    print("Variable 'x' is not defined. Please define it")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")
x=10 
try:
    print(x)
except NameError:
    print("Variable 'x' is now defined. The result is", x)
finally:
    print ("Now x is defined and the block executed successfully.")