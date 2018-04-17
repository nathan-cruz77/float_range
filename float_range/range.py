import numbers
import math


class FloatRange:

    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.stop = start
            self.start = 0
        else:
            self.start = start
            self.stop = stop

        self.minor = min(self.start, self.stop)
        self.major = max(self.start, self.stop)
        self.step = step
        self.precision = FloatRange._precision(step)

    def __iter__(self):
        return self

    def __next__(self):
        if self._is_empty():
            raise StopIteration

        res = round(self.start, self.precision)
        self.start += self.step
        return res

    def next(self):
        return self.__next__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        aux = ', '.join(str(x) for x in [self.start, self.stop, self.step])
        return '{0}({1})'.format(self.__class__.__name__, aux)

    def __contains__(self, item):
        conditions = [
            self._is_empty(),
            item > self.major,
            item < self.minor,
            item == self.stop
        ]

        if any(conditions):
            return False

        if self.start == item:
            return True

        # the result should be true if res*step = item*min(start,stop)
        res = (item - self.start) / self.step
        return res == round(res)

    def __eq__(self, other):
        attrs = ['start', 'stop', 'step']
        return all(getattr(self, k) == getattr(other, k, None) for k in attrs)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        raw_len = abs((self.major - self.minor) / self.step)

        if self._is_empty() or raw_len < 1:
            return 0

        return int(math.ceil(raw_len))

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('indices should be integers, floats or slices')

        pos_item = self.step * key + self.start
        neg_item = self.step * (len(self) + key) + self.start

        if pos_item in self:
            return pos_item

        if neg_item in self:
            return neg_item

        raise IndexError('index out of range')

    def index(self, item):
        if item in self:
            return abs((item - self.start) / self.step)
        raise ValueError

    def count(self, item):
        if isinstance(item, numbers.Number) and item in self:
            return 1
        return 0

    @staticmethod
    def _precision(number):
        try:
            number = float(number)
            decimal_part = str(number).split('.')[1]
        except (ValueError, TypeError, IndexError):
            msg = 'Cannot determine precision. \"{}\" is not a valid float'
            raise ValueError(msg.format(number))

        if decimal_part == '0':
            return 1
        else:
            return len(decimal_part)

    def _is_empty(self):
        return any([self._is_increasing(), self._is_decreasing()])

    def _is_increasing(self):
        return self.start >= self.stop and self.step > 0

    def _is_decreasing(self):
        return self.start <= self.stop and self.step < 0


def range(start, stop=None, step=1):
    return FloatRange(start, stop, step)
