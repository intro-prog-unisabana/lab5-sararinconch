some_int = None
some_str = None

def set_globals(entero, texto):
    global some_int, some_str
    some_int = entero
    some_str = texto
    
def get_globals():
    return some_int, some_str

