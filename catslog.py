"""A decorator which handles a function's basic logging
and basic exception handling"""
from functools import wraps


def catslog(f):
    """Given a function f, run it, log the execution and
    handle any potential exceptions"""
    @wraps(f)
    def wrapped(*args, **kwargs):
        """The extended version of the function f"""
        try:
            func_name = f.__name__
            print('Executing function {} with args: {} and kwargs: {}'
                  .format(func_name, args, kwargs))
            f(*args, **kwargs)
        except Exception as e:
            print("""An error occurred while executing function "{}".
            The error is {}""".format(func_name, str(e)))
    return wrapped
