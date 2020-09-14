from functools import wraps,update_wrapper
def check(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        ret = fn(*args, **kwargs)
        return ret
    return wrapper
#@check
def add(x, y):
    return x+y
add(4,5) = wrappper(4,5) = partial(update_wrapper,wrappper,元组，字典)＝update_wrapper(fn)
wraps(wrapper,
          assigned = WRAPPER_ASSIGNMENTS,
          updated = WRAPPER_UPDATES)
partial(update_wrapper, wrapped=wrapped,
                   assigned=assigned, updated=updated)
add(4,5)
