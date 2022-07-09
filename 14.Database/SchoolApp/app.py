from dbmanager import DbManager
import datetime
from Student import Student
from Teacher import Teacher

class App:
    def __init__(self):
        self.db = DbManager()
    
    def initApp(self):
        
        while True:
            msg = input("""
*******
1 - Öğrenci Listesi
2 - Öğrenci Ekle
3 - Öğrenci Güncelle
4 - Öğrenci Sil
5 - Öğretmen Listesi
6 - Öğretmen Ekle
7 - Öğretmen Güncelle
8 - Sınıflara Göre Dersler
9 - Çıkış
*******
""")
            try:
                msg = int(msg)
            except ValueError:
                print("Hatalı Giriş")
                continue

            match msg:
                case 1:
                    self.displayStudents()
                case 2:
                    self.addStudent()
                case 3:
                    self.editStudent()
                case 4:
                    self.deleteStudent()
                case 5:
                    self.displayTeachers()
                case 6:
                    self.addTeacher()
                case 7:
                    self.editTeacher()
                case 8:
                    self.getClassLessons()
                case 9:
                    break
                case _:
                    print("Hatalı Giriş")
    
    def displayClasses(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")

    def displayStudents(self):
        classes = self.db.getClasses()
        for i in classes:
            print(f"{i.id}: {i.name}")
        classid = int(input("Sınıf Seçiniz\n"))

        students = self.db.getStudentsByClassId(classid)
        print("Öğrenci Listesi\n")
        for std in students:
            print(f"{std.id} - {std.name} {std.surname}")
        
        return classid

    def addStudent(self):
        self.displayClasses()

        classid = int(input("Sınıf Seçiniz\n"))
        number = input("Öğrenci Numarası Giriniz\n")
        name = input("Öğrenci Adı Giriniz\n")
        surname = input("Öğrenci Soyadı Giriniz\n")
        year = int(input("Öğrenci Doğum Yılı Giriniz\n"))
        month = int(input("Öğrenci Ay Giriniz\n"))
        day = int(input("Öğrenci gün Giriniz\n"))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyet Giriniz (E/K)\n")

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)
    
    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id Giriniz\n"))
        student = self.db.getStudentById(studentid)
        student[0].name = input("Adı : ") or student[0].name
        student[0].surname = input("Soyadı : ") or student[0].surname
        student[0].gender = input("Cinsiyet : (E/K)") or student[0].gender
        student[0].classid = input("Sınıfı : ") or student[0].classid
        
        year = input("Yıl : ") or student[0].birthdate.year
        month = input("Ay : ") or student[0].birthdate.month
        day = input("Gün : ") or student[0].birthdate.day
        student[0].birthdate = datetime.date(int(year),int(month),int(day))
        self.db.editStudent(student[0])
    
    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id Giriniz\n"))
        self.db.deleteStudent(studentid)

    def displayTeachers(self):
        teachers = self.db.getTeachers()
        for i in teachers:
            print(f"{i.id}: {i.name} {i.surname} - {i.branch}")
    
    def addTeacher(self):
        branch = input("Branş Seçiniz\n")
        name = input("Öğretmen Adı Giriniz\n")
        surname = input("Öğretmen Soyadı Giriniz\n")
        year = int(input("Öğretmen Doğum Yılı Giriniz\n"))
        month = int(input("Öğretmen Ay Giriniz\n"))
        day = int(input("Öğretmen gün Giriniz\n"))
        birthdate = datetime.date(year,month,day)
        gender = input("Cinsiyet Giriniz (E/K)\n")

        teacher = Teacher(None,branch,name,surname,birthdate,gender)
        self.db.addTeacher(teacher)
    
    def editTeacher(self):
        teacherids = self.displayTeachers()
        teacherid = int(input("Öğretmen Id Giriniz\n"))
        teacher = self.db.getTeacherById(teacherid)
        teacher[0].branch = input("Branşı : ") or teacher[0].branch
        teacher[0].name = input("Adı : ") or teacher[0].name
        teacher[0].surname = input("Soyadı : ") or teacher[0].surname
        teacher[0].gender = input("Cinsiyet : (E/K)") or teacher[0].gender
        
        year = input("Yıl : ") or teacher[0].birthdate.year
        month = input("Ay : ") or teacher[0].birthdate.month
        day = input("Gün : ") or teacher[0].birthdate.day
        teacher[0].birthdate = datetime.date(int(year),int(month),int(day))
        self.db.editTeacher(teacher[0])

    def getClassLessons(self):
        list = self.db.getClassLessons()
        for i in list:
            print(f"{i.classname} - {i.lessonname} - {i.teachername} {i.teachersurname}")

if __name__ == "__main__":
    app = App()
    app.initApp()