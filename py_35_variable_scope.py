# variable scope = where a variable is visible and accessable 
# scope resolution = (LEGB) Local -> Enloced -> Global -> Built-in

from math import e      # built-in

x = 3       # Global
e = 3.14    # redeclaring as a global variable
print(x)
print(f"e : {e}")

def func1():
    x = 1       # local 
    e = 3.141    # redeclaring as a local variable
    print(x)
    print(f"e : {e}")

    def func2():
        x = 4     # encloced  
        e = 3.1415    # redeclaring as a encloced variable
        print(x)
        print(f"e : {e}")

    func2()

func1()
