!! MONAD PYZZA !!
=================

##What is "MONAD PYZZA"?

It is be able to "Monad" in Python.

## What is Monad?

Please see `src/use_monad.py` :)

```python
def not_monad_test(test_str):
    if not people_data.has_key(test_str):
        print "Not Find"
        return
    else:
        result = people_data[result]
    
    print("Not Find" if not language_data.has_key(result) else "Find :" + language_data[result])
```

```python
def monad_test(test_str):
    result = B_____(do_find_language,B_____(do_find_people,maybe.just(test_str)))
    print("Not Find" if not result[1] else "Find :" + result[1])
```

##Usage?
###Example Maybe Monad:
####Initialize
```
maybe = Maybe()
```
####Use "Just"
```python
maybe.just(5)  #("Just",5)
maybe.JT___(5) #Also
```
####Use "Bind"
```python
test = lambda x:("Just",x + 1)
maybe.bind(test,("Just",5))
maybe.BD___(test,("Just",5))
```

##License?

MIT :)
