from functools import wraps

def repeat(times):
    """_summary_

    Args:
        times (_type_): _description_
    """    
    def decorate(fn):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                fn(*args, **kwargs)
        return wrapper
    return decorate        

# @repeat(10)
def say(message):
    ''' print the message 
    Arguments
        message: the message to show
    '''
    print(message)
    
say('Hi')   


repeat(10)(say)('Hi')
