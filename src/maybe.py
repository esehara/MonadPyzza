from monad import * 

class Maybe(Monad):
    def do_bind(self,f,arg): 
        MonadType,MonadValue = arg
        if MonadType == "Nothing":
            return ("Nothing",None)
        elif MonadType == "Just":   
            result = f(MonadValue)
            # print result
            if not isMonad(result):
                raise NotMonadLawError
            else:return result 
        else:
            raise NotMonadException(arg)

    def fail(self,arg):
        return ("Nothing",None)
