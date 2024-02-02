from main import time_it, items, test_


@time_it(items)
def synced():
    nonlocal items
    return sum(items)


if __name__ == '__main__':
    synced()
