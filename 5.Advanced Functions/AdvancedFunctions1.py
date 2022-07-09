def greeting(name):
    print(f"Hello {name}")


print(greeting) # Fonksyonun bellekteki adresini gösterir
sayHello= greeting

# print(sayHello)
# print(greeting)

del sayHello
print(greeting)