

class Star:
    def __init__(self,n):
        self.n = n

    def __call__(self, fn):
        def wrapper(*args,**kwargs):
            print(self.n*'*')
            print(fn(*args,**kwargs))
            print(self.n*'*')
        return wrapper    

@Star(5)
def add(a,b):
    return a+b

add(10,9)  