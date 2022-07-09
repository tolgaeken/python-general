# BeautifulSoup eklentisini kurmak gerekir
# Aşağıdaki kod ile otomatik kurulur
# import os
# os.system('cmd /c "py -m pip install beautifulsoup4"')

htmlDoc = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk web sayfam</title>
</head>
<body>

<h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
    <h2>
        Programlama
    </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup2">
    <h2>
        Modüller
    </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <div class="grup3">
    <h2>
        Django
    </h2>
        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="fred.jpg" alt="">

    <a href="http://example1.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example2.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example3.com/elsie" class="sister" id="link1">Elsie</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(htmlDoc,"html.parser")

result = soup.prettify() # Html dökümanı okunacak şekilde düzenler
result = soup.title
result = soup.head
result = soup.body
result = soup.title.name # Html başlığının adını getirir
result = soup.title.string # Html başlığının metnini getirir
result = soup.h1
result = soup.h2
result = soup.find_all("h2") # Verillen html içeriğini liste olarak getirir
result = soup.find_all("h2")[0] # Getirilen listenin ilk elemanını getirir
result = soup.div
result = soup.find_all("div")
result = soup.find_all("div")[1]
result = soup.find_all("div")[1].ul
result = soup.find_all("div")[1].ul.li
result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren()
result = soup.div.findNextSibling().findNextSibling()
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
result = soup.find_all("a")
for link in result:
    # print(link)
    print(link.get("href"))


print(result)