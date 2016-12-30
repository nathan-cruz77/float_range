
def float_range(start, stop=None, step=1):
    if stop is None:
        stop, start = start, 0

    while start < stop:
        yield round(start, _precision(step))
        start += step

def _precision(number):
    try:
        res = len(str(number).split('.')[1])
    except IndexError:
        res = 1

    return res
