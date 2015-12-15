def func(*args, **kwargs):
    for arg in args:
        print(arg)

    for item in kwargs.items():
        print(item)


if __name__ == '__main__':
    func(x=1, y=2, z=3)
