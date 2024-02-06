def even_odd_filter(**numbers):
    if 'odd' in numbers:
        numbers['odd'] = [value for value in numbers['odd'] if value % 2 != 0]

    if 'even' in numbers:
        numbers["even"] = [value for value in numbers['even'] if value % 2 == 0]

    return dict(sorted(numbers.items(), key=lambda x: -len(x[-1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
