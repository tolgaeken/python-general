#Encapsulation

def outer(num1):
    print("Outer")
    def innerIncrement(num1):
        print("Inner")
        return num1 +1
    
    num2 = innerIncrement(num1) # İç fonksiyon çağırılmadığı sürece çalışmaz ve dışarıdan çağırılamaz
    print(num1,num2)

outer(10)
