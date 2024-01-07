def my_decorator(func):# the decorator function that takes a function as argument 
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator#decoratior function with@
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()


