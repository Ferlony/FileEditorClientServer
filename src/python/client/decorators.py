def simple_exception_decorator(fun):
    def inner_fun(*args):
        try:
            fun(*args)
        except Exception as e:
            print(e)
    return inner_fun
