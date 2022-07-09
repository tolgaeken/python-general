# Regular Expression Modülü
import re
# print(dir(re))

metin = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# print(re.findall("Python",metin)) # metin içinde yazılan ifadeyi arar
# print(len(re.findall("Python",metin))) # metin içinde yazılan ifadeden kaç tane olduğunu belirtir
# print(re.split(" ",metin)) # metin içinde verilen ifadeye göre bölme yapar
# print(re.sub(" ","-",metin)) # metin içinde " " karakterini "-" olarak değiştirir
# print(re.sub("\s","-",metin)) # " " yerine "\s" kullanılabilir
# print(re.search("Python",metin)) # metin içinde girilen değerin konumunu gösterir
# print(re.search("Python",metin).span())
# print(re.search("Python",metin).start())
# print(re.search("Python",metin).end())
# print(re.search("Python",metin).string()) # İfadeyi tam olarak nerede aradığını gösterir



"""

    [] - Köşeli parantezler arasına yazılan bütün karakterler
         aranır.

         [abc] => a      : 1 match
                  ac     : 2 match 
                  Python : No matches

         [a-e]  => [abcde]
         [1-5]  => [12345]
         [0-39] => [01239]   

         [^abc] => abc dışındaki karakterler.
         [^0-9] => rakam olmayan karakterler.

"""
# print(re.findall("[abc]",metin)) # metin içinde köşeli parantezin içerisinde verilen karakterleri arar
# print(re.findall("[sat]",metin))
# print(re.findall("[a-e]",metin)) # a b c d e karakterlerini arar
# print(re.findall("[1-5]",metin)) # 1 2 3 4 5 karakterlerini arar
# print(re.findall("[0-39]",metin)) # 0 1 2 3 9 karakterlerini arar
# print(re.findall("[^abc]",metin)) # a b c dışındaki karakterleri arar

"""
    . - Her hangi bir tek karakteri belirtir.

        .. => a    : No match
              ab   : 1 match
              abc  : 1 match
              abcd : 2 matches

    
"""

# print(re.findall("...",metin)) # metinleri 3 er basamak olarak gösterir
# print(re.findall("Py..on",metin))


"""
    ^ - Belirtilen string karakterlerle başlıyor mu ?

    ^a => a:    1 match
          abc:  1 match
          bac:  No match

"""

# print(re.findall("^P",metin)) # metin girilen karakterle başlayıp başlamadığını kontrol eder


"""
    $ - Belirtilen karakterle bitiyor mu ?

    a$ => a      : 1 match
          lamba  : 1 match
          Python : No match 

"""

# print(re.findall("t$",metin))  # metin girilen karakterle bitip bitmediğini kontrol eder
# print(re.findall("saat$",metin)) 
# print(re.findall("saatt$",metin)) 


"""
     * - Bir karakterin sıfır ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma*n => mn     : 1 match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

# print(re.findall("sa*t",metin))


"""
     + - Bir karakterin bir ya da daha fazla sayıda olmasını 
         kontrol eder.

         ma+n => mn     : No match
                 man    : 1 match
                 maaan  : 1 match
                 main   : No match (a' nın arkasına n gelmiyor.) 
"""

# print(re.findall("sa+t",metin))


"""
    ? - Bir karakterin sıfır ya da bir kez olmasını 
        kontrol eder.

        ma+n => mn     : No match
                man    : 1 match
                maaan  : 1 match
                main   : No match (a' nın arkasına n gelmiyor.) 
"""

# print(re.findall("sa?t",metin))


"""
    {} - Karakter sayısını kontrol eder.

        al{2}   => a karakterinin arkasına l karakteri 2 kez tekrarlamalı.
        al{2,3} => a karakterinin arkasına l karakteri en az 2 en fazla 3 kez tekrarlamalı.
        [0-9]{2,4} => en az 2 en çok 4 basamaklı sayılar.
"""
# print(re.findall("a{2}", metin)) 
# print(re.findall("[0-9]{2}", metin)) 


"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde =>    no match
            ade =>    1 match
            acdbea => 3 match 
"""

"""
    () - gruplamak için kullanılır.

         (a|b|c)xz => a,b,c karakterlerinin arkasına xz gelmelidir.
"""



"""
    \ - Özel karakterleri aramamızı sağlar.
        \$a => $ karakterinin arkasına a karakterinin arar. Yani
               $ regular exp. engine tarafından yorumlanmaz.

    \A - Belirtilen karakter string in başında mı ?
         \Athe => the string in başındamı

        result = re.findall("\APython", str)
        result = re.findall("saat\Z", str)

    \Z - Belirtilen karakter string in sonunda mı ?
         the\Z => the string in sonunda mı

    \b - Belirtilen karakter kelimenin in başında ya da sonunda mı ?
         \bthe => the kelimenin in başında mı?
         the\b => the kelimenin in sonunda mı?

    \B - Belirtilen karakter kelimenin in başında ya da sonunda değil mı ?
         \Bthe => the kelimenin in başında değil mi?
         the\B => the kelimenin in sonunda değil mi?
    
    \d - [0-9] ile aynı anlama gelir yani rakamları arar.
         \d => 12abc34

    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
         \D => 1ab44_50

    \s - Boşluk karakterlerini arar.  
    \S - Boşluk karakterleri dışındakiler.
    \w - Alfabetik karakterler, rakamlar ve alt çizgi karakteri.
    \W - \w nin tam tersi
    
"""