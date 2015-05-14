from datetime import date, timedelta


def checkio(from_date, to_date):
    """
        Count the days of rest
    """

    return len([day for day in interval(from_date, to_date) if day.weekday() > 4])


def interval(start, end):
    curr = start
    while curr <= end:
        yield curr
        curr += timedelta(days=1)

# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert checkio(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert checkio(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

