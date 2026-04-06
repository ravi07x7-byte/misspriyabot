name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Different formats
print(f"Hello {name}, you are {age} years old.")      # F-string
print("Hello {}, you are {} years old.".format(name, age)) # .format()
print("Hello %s, you are %d years old." % (name, age))    # % operator