from functools import wraps


def catslog(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        try:
            func_name = f.__name__
            print("Executing function {} with args: {} and kwargs: {}".format(func_name, args, kwargs))
            f(*args, **kwargs)
        except Exception as e:
            print("An error occurred while executing function '{}'. The error is {}".format(func_name, str(e)))
    return wrapped