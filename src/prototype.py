import types

class NotFunctionException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr("NotFunctionException")

class NotMonadException(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr("NotMonadException:" + self.value)

class Monad:
    def bind(self,f,arg):
        ## -- Type Check
        if not isMonad(arg):raise NotMonadException(arg)
        if (    (type(f) is not types.FunctionType) 
            and (type(f) is types.InstanceType) 
            and (type(f) is not types.MethodType)):
            raise NotFunctionException(f) 
        
        return self.do_bind(f,arg)

    def do_bind(self,f,arg):
        pass

    def just(self,arg):
        return ("Just",arg)

    def JT___(self,arg):
        """
        JT___(arg) is "=<< (return arg)".
        """
        self.just(arg)


    def BD___(self,f,arg):
        """
        BD___(f,arg) is "f =<< arg".

        """
        self.bind(f,arg)

    def getValue(self,arg):
        if not isMonad(arg):raise NotMonadException(arg)
        return arg[1]

def isMonad(arg):
    if not isinstance(arg,tuple):return False
    if not isinstance(arg[0],str):return False
    return True
