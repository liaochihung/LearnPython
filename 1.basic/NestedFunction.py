def addone(myfunc):
    '''
    function is just an object, so we can use this for less code and more lightweight
    :param myfunc:
    :return:
    '''

    def addoneinside():
        return myfunc() + 1

    # can use condition to return different result
    return addoneinside


# decorator
@addone
def oldfunc():
    return 3


if __name__ == '__main__':
    '''
    # can use decorator instead
    newFunc = addone(oldfunc)
    '''
    print(oldfunc())
