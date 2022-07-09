# MySql Uygulama - Okul
import mysql.connector as conn
from datetime import datetime

# 1- Database bağlantısını oluşturunuz. (connection.py)
from Database3connection import connection,cursor

# 2- Workbench IDE ile schooldb isminde bir database oluşturup Student tablosunu ekleyiniz.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

"""
myConnectionMain= conn.connect(
    host = "localhost",
    user = "root",
    password = "MySql1234",
)

mainCursor = myConnectionMain.cursor()
mainCursor.execute("create database schooldb")


myConnectionSchool = conn.connect(
    host = "localhost",
    user = "root",
    password = "MySql1234",
    database = "schooldb"
)

schoolCursor = myConnectionSchool.cursor()
schoolCursor.execute("create table student (Id INT,StudentNumber INT,Name VARCHAR(255),Surname VARCHAR(255),BirthDate DATETIME,gender CHAR(1))")
"""

ogrenciler = [
    ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
]

class Student:
    connection = connection # Tüm objelerin genel olarak kullanılması için class seviyesinde yazılır
    mycursor = connection.cursor()

    def __init__(self,id,studentNumber,name,surname,birthdate,gender):
        
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
    
    def saveStudent(self):
        sql = "INSERT INTO Student (StudentNumber,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} adet kayıt eklendi.")
        except conn.Error as err:
            print(f"Hata : {err}")
        finally:
            Student.connection.close()
    

    """
    3- Aşağıdaki bilgiler için insert sorguları oluşturup kayıtları ekleyiniz.

    ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
    """
    @staticmethod # Class içinde tanımlanmayan, dışarıdan gelen verilere göre işlem yapılabilmesi için yazılır
    def saveStudents(students):
        sql = "INSERT INTO Student (StudentNumber,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} adet kayıt eklendi.")
        except conn.Error as err:
            print(f"Hata : {err}")
        finally:
            Student.connection.close()
    

    """
    4- Aşağıdaki sorguları yazınız.
      a- Tüm öğrenci kayıtlarını alınız.
      b- Tüm öğrencilerin sadece öğrenci no, ad ve soyad bilgilerini alınız.
      c- Sadece kız öğrencilerin ad ve soyadlarını alınız.
      d- 2003 doğumlu öğrenci bilgilerini alınız. 
      e- İsmi Ali ve doğum tarihi 2005 olan öğrenci bilgilerini alınız.
      f- ad veya soyadı içinde 'an' ifadesi geçen kayıtları alınız. 
      g- Kaç erkek öğrenci vardır ?
      h- Kız öğrencileri harf sırasına göre getiriniz.
    """  
    @staticmethod
    def getStudents():
        a = "select * from student"
        # a = "select * from student limit 5 # ilk 5 kaydı getirir
        b = "select studentnumber,name,surname from student"
        c = "select name,surname from student where gender = 'K'"
        # d = "select * from student where birthdate like '%2003%'" # alternatif kullanım
        d = "select * from student where year(birthdate) = 2003"
        e = "select * from student where name = 'Ali' and year(birthdate) = 2005"
        f = "select * from student where name like '%an%' or surname like '%an%'"
        g = "select count(*) from student where gender = 'E'"
        h = "select * from student where gender = 'K' order by name,surname"   
        Student.mycursor.execute(a)

        try:
            result = Student.mycursor.fetchall()
            for i in result:
                print(i)
        except conn.Error as err:
            print(f"Hata : {err}")
        finally:
            Student.connection.close()
    

    """
    5- Aşağıdaki güncelleme sorularını yapınız.
      a- id' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
      b- cinsiyet' e göre aldığınız bir öğrencinin bilgilerini güncelleyiniz.
    """  
    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id = %s"
        value = (id,)
        
        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchone()
        except conn.Error as err:
            print(f"Hata {err}")
        # finally:
        #     Student.connection.close()
    
    def updateStudent(self): # Üstünde çalışılan bilgi güncellendiği için class parametresini alır ve staticmethod değildir
        sql = "update student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} kayıt güncellendi")
        except conn.Error as err:
            print(f"Hata : {err}")
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)
        
        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except conn.Error as err:
            print(f"Hata {err}")
    
    @staticmethod
    def updateStudents(liste):
        sql = "update student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in liste:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f"{Student.mycursor.rowcount} kayıt güncellendi")
        except conn.Error as err:
            print(f"Hata : {err}")
        finally:
            Student.connection.close()



# Student("201","Ahmet","Yılmaz",datetime(2005, 5, 17),"E").saveStudent()
# Student.saveStudents(ogrenciler)
Student.getStudents()

# obj = Student.getStudentById(2)
# student = Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
# student.name = "Ali"
# student.surname = "Can"
# student.updateStudent()

# students = Student.getStudentsGender("E")
# liste = []
# for student in students:
#     student = list(student)
#     student[2] = "Mr " + student[2]
#     liste.append(student)
# Student.updateStudents(liste)



def getStudentsIntro():
    # cursor.execute("Select * from student")
    # result = cursor.fetchall() # Koşula uyan tüm kayıtları getirir
    # for i in result:
    #     # print(i)
    #     print(f"Number : {i[1]} \t Name : {i[2]}")

    # cursor.execute("Select StudentNumber,Name from student")
    # result = cursor.fetchall()
    # for i in result:
    #     print(f"Number : {i[0]} \t Name : {i[1]}")

    # cursor.execute("Select StudentNumber,Name from student")
    # result = cursor.fetchone() # Koşula uyan ilk kaydı getirir
    # print(f"Number : {result[0]} \t Name : {result[1]}")

    sql = "Select * from student where id = 3" # Id si 3 olan kaydı getirir
    sql = "Select * from student where gender = 'E' and id = 2" # And kullanımı
    sql = "Select * from student where gender = 'E' or id = 3" # Or kullanımı
    sql = "Select * from student where gender = 'E' and name like 'Bah%'" # Like kullanımı 1
    sql = "Select * from student where gender = 'E' and name like '%adır'" # Like kullanımı 2
    sql = "Select * from student where gender = 'E' and name like '%aha%'" # Like kullanımı 3
    sql = "Select * from student order by name" # name kolonuna göre artan şekilde sıralar
    sql = "Select * from student order by name desc" # name kolonuna göre azalan şekilde sıralar
    sql = "Select * from student order by name , surname desc" # name kolonuna göre artan, eğer aynısı var ise surname kolonuna göe azalan şekilde sıralar
    cursor.execute(sql)

    try:
        result = cursor.fetchall()
        for i in result:
            print(i)
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
# getStudentsIntro()

def getStudentId(id):
    sql = "Select * from student where id = %s"
    params = (id,) # tek gönderilecek veriler için tuple olması gerekir
    cursor.execute(sql,params)
    
    try:
        result = cursor.fetchone()
        print(result)
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
# getStudentId(4)

def updateStudent():
    sql = "update student set name = 'Ali' where id = 2"
    sql = "update student set name = 'Ali' , surname = 'Can' where id = 2"
    cursor.execute(sql)
    
    try:
        connection.commit()
        print(f"{cursor.rowcount} kayıt düzenlendi.")
    except conn.Error as err:
        print(f"Hata: {err}")
    finally:
        connection.close()
# updateStudent()

def updateInput(prm = None):
    def updateStudentById(id,name,surname):
        sql = "update student set name = %s , surname = %s where id = %s" # Where koşulu verilmediği taktirde set etmek için girilen bütün değerler aynı olur
        values = (name,surname,id)
        cursor.execute(sql,values)

        try:
            connection.commit()
            print(f"{cursor.rowcount} kayıt düzenlendi.")
        except conn.Error as err:
            print(f"Hata: {err}")
        finally:
            connection.close()
            
    updtId = int(input("Id Giriniz\n"))
    updtName = input("Yeni İsim Giriniz\n")
    updtSurname = input("Yeni Soyisim Giriniz\n")
    updateStudentById(updtId,updtName,updtSurname)
# updateInput()

def deleteStudent():
    sql = "delete from student where id = 1" # where ile şart girilmediği taktirde tüm tablo silinir
    sql = "delete from student where name like '%hme%'"
    cursor.execute(sql)

    try:
        connection.commit()
        print(f"{cursor.rowcount} kayıt silindi")
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
# deleteStudent()

def deleteStudentbyId(id):
    sql = "delete from student where id = %s"
    values = (id,)
    cursor.execute(sql,values)

    # sql = "delete from student where id = " + id   # Sql Injection riski taşır
    # cursor.execute(sql)

    try:
        connection.commit()
        print(f"{cursor.rowcount} kayıt silindi")
    except conn.Error as err:
        print(f"Hata : {err}")
    finally:
        connection.close()
# deleteStudentbyId(1)
