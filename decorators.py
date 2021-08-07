def dec_1(func):
    print("Inside decorator 1")
    return func


@dec_1
def fun():
    print("Inside Fun")


# simple use of decorators are illustrated
fun()


# here additional functionality is added by the wrapper function and doesn't effect the function name as well
# This method of nesting a function within another is called closure in functional programming.
# This is used middlewares as functions in django


def add_things(func):
    def wrapper():
        title = func()
        return title + "!!!"
    return wrapper


@add_things
def get_title():
    return "Some Outlandish Title"


print(get_title())
# Some Outlandish Title!!!


# method 2 : Using Multiple Decorators
# the order is important while using multiple decorators for the same function


def add_things(func):
    def wrapper():
        title = func()
        return title + "!!!"
    return wrapper


def add_additional_things(func):
    def wrapper():
        title = func()
        return title + "##### "
    return wrapper


@add_additional_things
@add_things
def get_title():
    return "Some Outlandish Title"


print(get_title())
# Some Outlandish Title!!!#####


@add_things
@add_additional_things
def get_title():
    return "Some Outlandish Title"


print(get_title())
# Some Outlandish Title##### !!!
