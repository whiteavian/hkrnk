from heapq import heappush, heappop


class MedianList:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.median = None

    def __repr__(self):
        return "Min {}, max {}".format(self.min_heap, self.max_heap)

    def add(self, element):
        element = float(element)

        if self.median:
            if element <= self.median:
                heappush(self.min_heap, -1 * element)
            else:
                heappush(self.max_heap, element)

            self.update_median()
        else:
            self.median = element
            heappush(self.min_heap, -1 * element)

        return self.median

    def update_median(self):
        self.balance()

        if len(self.min_heap) > len(self.max_heap):
            self.median = -1 * heappop(self.min_heap)
            heappush(self.min_heap, self.median * -1)

        elif len(self.max_heap) > len(self.min_heap):
            self.median = heappop(self.max_heap)
            heappush(self.max_heap, self.median)

        else:
            a = -1 * heappop(self.min_heap)
            b = heappop(self.max_heap)
            self.median = (a + b) / 2
            heappush(self.min_heap, -1 * a)
            heappush(self.max_heap, b)

        return self.median

    def balance(self):
        if len(self.min_heap) -1 > len(self.max_heap):
            move = -1 * heappop(self.min_heap)
            heappush(self.max_heap, move)
        elif len(self.min_heap) < len(self.max_heap) - 1:
            move = heappop(self.max_heap)
            heappush(self.min_heap, -1 * move)


ml = MedianList()
a = ml.add(1)
b = ml.add(2)
c = ml.add(3)
d = ml.add(4)
e = ml.add(5)
f = ml.add(6)
g = ml.add(7)
h = ml.add(8)
i = ml.add(9)
j = ml.add(10)

