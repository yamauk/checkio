def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """

    power = 0
    for i in xrange(len(powers)-1):
        if abs(number) / (base ** (power + 1)) != 0:
            power += 1

    number /= float(base) ** power
    if decimals > 0:
        retval = '%.' + str(decimals) + 'f'
        retval = retval % number
    else:
        retval = '%d' % number

    retval += powers[power]+suffix
    return retval

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024,
                           suffix='iB') == '976MiB', '976MiB'

