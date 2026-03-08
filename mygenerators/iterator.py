import time

def iterate_with_timeout(iterator, timeout):
    start_time = time.time()
    count = 0
    total = 0

    for value in iterator:
        count = count + 1

        if type(value) in [int, float]:
            total = total + value
            try:
                avg = total / count
                print(f"{value} | sum={total} avg={avg:.2f}")
            except OverflowError:
                print(f"{value} | sum={total} avg=too big to show")
        else:
            print(value)

        elapsed = time.time() - start_time
        if elapsed >= timeout:
            break

    print(f"finished after {count} iterations")
