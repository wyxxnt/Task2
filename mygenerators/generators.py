import time
import random

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def random_numbers():
    while True:
        yield random.randint(1, 100)

def days_cycle():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    i = 0
    while True:
        yield days[i % len(days)]
        i += 1
def iterate_with_timeout(iterator, timeout):
    start = time.time()
    count = 0
    total = 0

    for value in iterator:
        count += 1

        if type(value) in [int, float]:
            total += value
            print(f"{value} | sum={total} avg={total/count:.2f}")
        else:
            print(value)

        if time.time() - start >= timeout:
            break

    print(f"done, {count} iterations")

print("— Fibonacci -")
iterate_with_timeout(fibonacci(), 2)

print("\n— Random numbers —")
iterate_with_timeout(random_numbers(), 2)

print("\n— Days —")
iterate_with_timeout(days_cycle(), 2)
