import numbers

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
        if (self._is_empty() or item >= self.major
                or item < self.minor):
            return False

        # the result should be true if res*step = item*min(start,stop)
        res = (item - self.minor) / self.step
        return res == round(res)

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
        increasing_case = self.start >= self.stop and self.step > 0
        decreasing_case = self.start <= self.stop and self.step < 0

        return any([increasing_case, decreasing_case])


def range(start, stop=None, step=1):
    return FloatRange(start, stop, step)
