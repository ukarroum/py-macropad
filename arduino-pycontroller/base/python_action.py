import functools


def python_action(pattern):
    def action_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func.pattern = pattern
            return func(*args, **kwargs)
        return wrapper
    return action_decorator
