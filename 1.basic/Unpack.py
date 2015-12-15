date, name, price = ['December 23, 2015', 'Jack', 1.234]


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([1, 2, 3, 4])
