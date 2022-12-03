from time import time
from colorama import init, Fore, Back, Style
init(convert=True)
  
def timer_func(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        print(f'{Fore.LIGHTBLUE_EX}', end='')
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'{Fore.GREEN}Function {func.__name__!r} executed in {(t2-t1):.4f}s{Style.RESET_ALL}')
        return result
    return wrap_func