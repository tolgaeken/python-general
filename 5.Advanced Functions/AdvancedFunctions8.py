# Fonksiyonlarda Decorator

def myDecorator(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

@myDecorator # sayHello fonksiyonunu myDecorator fonksiyonuna gönderir
def sayHello(name):
    print(f"Hello {name}")

# sayHello = myDecorator(sayHello) # @myDecorator ile yapılan işlemin aynısı
# sayHello()

sayHello("Ali")