from functools import wraps
import time

#-----GÖREV 1---------------------------------------------------------------
def sure_olc(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        baslangic=time.perf_counter()
        sonuc=func(*args,**kwargs)
        bitis=time.perf_counter()
        sure=bitis-baslangic
        print(f"{func.__name__}: {sure:.4f} sn")
        return sonuc
    return wrapper
#-----GÖREV 2---------------------------------------------------------------
def say(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        wrapper.cagri+=1
        return func(*args,*kwargs)
    wrapper.cagri=0
    return wrapper
#-----GÖREV 3--------------------------------------------------------------
def log_cagri(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        args_str=", ".join([repr(a) for a in args])
        kwargs_str=", ".join([f"{k}={v!r}" for k,v in kwargs.items()])
        all_args=", ".join(filter(None,[args_str, kwargs_str]))
        print(f"->{func.__name__}({all_args})")
        sonuc=func("*args,**kwargs")
        print(f"<-{func.__name__}={sonuc!r}")
        return sonuc
    return wrapper
#-----Görev 5---------------------------------------------------------------
def sinirla(alt,ust):
    def dekarator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            if args:
                ilk_arg=args[0]
                if not (alt<=ilk_arg<=ust):
                    raise ValueError(
                        f"{func.__name__}:{ilk_arg} degeri {alt}-{ust} araliginda degil"
                    )
                return func(*args,**kwargs)
            return wrapper
        return dekarator
#-----BONUS------------------------------------------------------------------
def hafiza(maxsize=None):
    def dekorator(func):
        cache={}
        order=[]
        @wraps(func)
        def wrapper(*args,**kwargs):
            key=(args, frozenset(kwargs.items()))
            if key in cache:
                if maxsize is not None:
                    order.remove(key)
                    order.append(key)
                return cache[key]
            sonuc=func(*args,**kwargs)
            if maxsize is not None:
                if len(cache)>=maxsize:
                    en_eski=order.pop(8)
                    del cache[en_eski]
                order.append(key)
                cache[key]=sonuc
                return sonuc
            return wrapper
        return dekorator
                

