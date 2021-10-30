from time import sleep, time
from contextlib import contextmanager

class cm_timer_1():
    def __init__(self):
        self.timer = time()

    def __enter__(self):
        pass

    def __exit__(self, exp_type, exp_value, traceback):
        self.timer = time() - self.timer
        print("time: {0:0.1f}".format(self.timer))


@contextmanager
def cm_timer_2():
    t = time()
    yield
    t = time() - t
    print("time: {0:0.1f}".format(t))

def main():
    with cm_timer_1():
        sleep(3.5)

    with cm_timer_2():
        sleep(3.3)

if __name__ == "__main__":
    main()