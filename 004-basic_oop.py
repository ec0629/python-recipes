# Data Science from Scratch by Joel Grus

class CountingClicker:
    def __init__(self, count=0):
        self.count = count

    def __repr__(self) -> str:
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"


class NoResetClicker(CountingClicker):
    # This class has all the same methods as CountingClicker
    # Except that it has a reset method that does nothing.
    def reset(self):
        pass


clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"
