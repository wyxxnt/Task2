import random

def fibonacci():
    a = 0
    b = 1
    while True:
        yield a
        temp = a + b
        a = b
        b = temp

def random_numbers():
    while True:
        num = random.randint(1, 100)
        yield num

def days_cycle():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    index = 0
    while True:
        yield days[index]
        index = index + 1
        if index >= len(days):
            index = 0
