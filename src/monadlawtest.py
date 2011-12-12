def MonadLawTest(test_target):
    """
    //////////////
    Monad Law Test
    /////////////
    """
    maybe = test_target()
    BD___ = maybe.bind
    JT___ = maybe.just
    MonadTest  = lambda x:("Just",x + 1)
    MonadTest2 = lambda x:("Just",x * 2)

    print """
    1.(return x) >>= f == f x

    Rewrite:Python

    BD___(f,JT___(x)) == f(x)

    Test :: 
    """
    print BD___(MonadTest,JT___(5)) == MonadTest(5)

    print """
    2. m >>= return == m

    Rewrite:Python

    BD___(JT___,m) == m

    Test ::
    """

    print BD___(JT___,("Just",5)) == ("Just",5)

    print """
    3. (m >>= f ) >>= g == m >>= (\\x -> f x >>= g)
    
    Rewrite.Python

    (\\x -> f x >>= g) --> (lambda x:("Just",BD___(g,f(x))))
    
    m >>= \\x ..       --> BD___(\\x,m)

    ----> BD___((lambda x:BD___(g,f(x))),m)
    
    BD___(g,BD___(f,m)) == BD___((lambda x:BD___(g,f(x))),m)

    Test::
    """
    test = BD___(MonadTest2,BD___(MonadTest,("Just",5)))
    test2 = BD___((lambda x:BD___(MonadTest2,MonadTest(x))),
                        ("Just",5))
    print test == test2
