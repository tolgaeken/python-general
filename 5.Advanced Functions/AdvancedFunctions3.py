# Hata Yönetimi kullanmadan değer kontrolü yapma

def factorial(number):
    if not isinstance(number,int):
        print("Değer sayısal değildir")
        return None
    
    if number<=0:
        number *= -1

    def innerFactorial(number):
        if number<=1:
            return 1
        
        return number * innerFactorial(number-1)
    
    return innerFactorial(number)


print(factorial(-4))