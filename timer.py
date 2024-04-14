import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        print("Execution time of \"{0}\" was {1} seconds".format(func.__name__, end - start))
        return value

    return wrapper

