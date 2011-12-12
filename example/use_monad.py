from monad import *

people_data = {"esehara":"Python"
              ,"Robot"  :"Haskell"
              ,"Someone":"Clojure"}

language_data = {"Python" : "Python is Very Cool"
                ,"Haskell": "Haskell is Functional"}


#If use Monad
maybe   = Maybe()
B_____  = maybe.bind

find_data        = lambda x,target_data: maybe.just(target_data[x]) if target_data.has_key(x) else maybe.fail(x)

do_find_people   = lambda             x: find_data(x,people_data)
do_find_language = lambda             x: find_data(x,language_data)

def monad_test(test_str):
    result = B_____(do_find_language,B_____(do_find_people,maybe.just(test_str)))
    print("Not Find" if not result[1] else "Find :" + result[1])

#If not Monad

def not_monad_test(test_str):
    if not people_data.has_key(test_str):
        print "Not Find"
        return
    else:
        result = people_data[result]
    
    print("Not Find" if not language_data.has_key(result) else "Find :" + language_data[result])

def main():
    print "### do monad"
    monad_test("esehara")
    monad_test("Oresama")
    monad_test("Someone")

    print "### not do monad"
    not_monad_test("esehara")
    not_monad_test("Oresama")
    not_monad_test("Someone")

if __name__ == "__main__":main()
