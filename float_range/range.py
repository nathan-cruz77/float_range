def range(start, stop=None, step=1):
    if stop is None:
        stop, start = start, 0

    if step < 0:
        while start > stop:
            yield round(start, _precision(step))
            start += step
    else:
        while start < stop:
            yield round(start, _precision(step))
            start += step

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
