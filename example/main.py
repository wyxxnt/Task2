import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from mygenerators import fibonacci, random_numbers, days_cycle, iterate_with_timeout


print("Fibonacci numbers")
iterate_with_timeout(fibonacci(), 2)

print()

print("Random numbers")
iterate_with_timeout(random_numbers(), 2)

print()

print("Days of the week")
iterate_with_timeout(days_cycle(), 1)
