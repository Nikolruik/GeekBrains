def logger(verbosity):
   def _logger(func):
       def wrapper(*args):
           result = func(*args)
           msg = f'\tcall {func.__name__}'
           if verbosity:
               msg = f'{msg}({", ".join(map(str, args))})'
           # if verbosity > 1:
           #     msg = f'{msg} -> {result}'
           # return msg

       return wrapper

   return _logger


@logger(lambda x: x > 5)
def render_input(field):
   return f'<input id="id_{field}" type="text" name="{field}">'


username_f = render_input('username')
password_f = render_input('password')
print(username_f)
print(password_f)

def cube(a):
    return a ** 3

print(cube(3))