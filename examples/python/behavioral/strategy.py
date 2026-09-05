class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy

    def sort(self, values):
        return self.strategy(values)


def bubble_sort(values):
    return sorted(values)


def quick_sort(values):
    return sorted(values)


sorter = Sorter(bubble_sort)
print(sorter.sort([3, 1, 2]))
sorter.strategy = quick_sort
print(sorter.sort([3, 1, 2]))
