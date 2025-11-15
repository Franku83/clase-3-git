def print ():
    print("This is a print function from main2.py")
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = suma(a,b)
    print(result)
    
    
def suma (a, b):
    return a + b
        

if __name__ == "__main__":
    print()