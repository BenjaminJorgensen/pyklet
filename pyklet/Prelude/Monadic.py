from typing import Callable
from inspect import signature

def binds(binding_param: str) -> Callable[..., Callable]:
    def bindable_func(func: Callable) -> Callable:
        sig = signature(func)
        param_names = sig.parameters.copy()
        if not binding_param in param_names.keys():
            raise ValueError(f"Parameter \"{binding_param}\" not found in function \"{func.__name__}\"")
        def wrapper(*args, **kwargs) -> Callable:
            if param_names.get(binding_param): param_names.pop(binding_param)
            if kwargs.get(binding_param): kwargs.pop(binding_param)
            bound_args = dict(zip(param_names, args))
            bound_args |= kwargs
            if len(args) + len(kwargs) != len(param_names):
                return func(*args, **kwargs)
            return lambda a: func(**bound_args, **{binding_param: a})
        return wrapper
    return bindable_func
