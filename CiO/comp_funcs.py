def checkio(f,g):
    def h(*args,**kwargs):
        try:
            result = f(*args,**kwargs)
            if result is None:
                raise Exception
            try:
                b = g(*args,**kwargs)
                if b is None:
                    raise Exception
                status = ['different', 'same'][result == b]
            except:
                status = 'g_error'
        except:
            try:
                result = g(*args,**kwargs)
                if result is None:
                    raise Exception
                status = 'f_error'
            except:
                result = None
                status = 'both_error'
        return (result, status)     
    return h
