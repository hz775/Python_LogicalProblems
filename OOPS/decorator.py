def add_sprinkles(func):
    def wrapper():
        print("Add sprinkles")
        func()
    return wrapper

@add_sprinkles
def get_icecream():
    print("Here 's your icecream")

get_icecream()
# without wrapper 
def add_sprinkles(func):
        print("Add sprinkles")
        func()

@add_sprinkles
def get_icecream():
    print("Here 's your icecream")

