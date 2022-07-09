import mysql.connector as conn
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
from ClassLesson import ClassLesson

# MySql Join İşlemleri - Model Tasarımı
# ALTER TABLE class
# ADD CONSTRAINT fk_teacher_class
# FOREIGN KEY (TeacherId) REFERENCES teacher(Id)

# ALTER TABLE student
# ADD CONSTRAINT fk_student_class
# FOREIGN KEY (ClassId) REFERENCES class(Id)

# ALTER TABLE classlesson
# ADD CONSTRAINT fk_classlesson_class
# FOREIGN KEY (ClassId) REFERENCES class(Id)

# ALTER TABLE classlesson
# ADD CONSTRAINT fk_classlesson_lesson
# FOREIGN KEY (LessonId) REFERENCES lesson(Id)

# ALTER TABLE classlesson
# ADD CONSTRAINT fk_classlesson_teacher
# FOREIGN KEY (TeacherId) REFERENCES teacher(Id)

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "select * from student where id = %s"
        value= (id,)
        self.cursor.execute(sql,value)
        try:
            result = self.cursor.fetchone()
            return Student.CreateStudent(result)
        except conn.Error as err:
            print(f"Hata : {err}")
    
    def getClasses(self):
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            result = self.cursor.fetchall()
            return Class.CreateClass(result)
        except conn.Error as err:
            print(f"Hata : {err}")
        

    def getStudentsByClassId(self,classid):
        sql = "select * from student where classid = %s"
        value= (classid,)
        self.cursor.execute(sql,value)
        try:
            result = self.cursor.fetchall()
            return Student.CreateStudent(result)
        except conn.Error as err:
            print(f"Hata : {err}")
    
    # def addOrEditStudent(self,student:Student):
    #     pass
    
    def addStudent(self,student:Student):
        sql = "INSERT INTO Student (StudentNumber,Name,Surname,Birthdate,Gender,ClassId) values (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt eklendi.")
        except conn.Error as err:
            print(f"Hata : {err}")

    def editStudent(self,student:Student):
        sql = "update student set studentnumber=%s, name=%s, surname=%s, birthdate=%s, gender=%s,classid=%s where id=%s"
        value = (student.studentNumber,student.name,student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt güncellendi.")
        except conn.Error as err:
            print(f"Hata : {err}")
    
    def deleteStudent(self,studentid):
        sql = "delete from student where id = %s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt silindi.")
        except conn.Error as err:
            print(f"Hata : {err}")

    def getTeachers(self):
        sql = "select * from teacher"
        self.cursor.execute(sql)
        try:
            result = self.cursor.fetchall()
            return Teacher.CreateTeacher(result)
        except conn.Error as err:
            print(f"Hata : {err}")
    
    def getTeacherById(self,id):
        sql = "select * from teacher where id = %s"
        value= (id,)
        self.cursor.execute(sql,value)
        try:
            result = self.cursor.fetchone()
            return Teacher.CreateTeacher(result)
        except conn.Error as err:
            print(f"Hata : {err}")

    def addTeacher(self,teacher:Teacher):
        sql = "INSERT INTO Teacher (Branch,Name,Surname,Birthdate,Gender) values (%s,%s,%s,%s,%s)"
        value = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt eklendi.")
        except conn.Error as err:
            print(f"Hata : {err}")

    def editTeacher(self,teacher:Teacher):
        sql = "update teacher set Branch=%s, Name=%s, Surname=%s, BirthDate=%s, Gender=%s where id=%s"
        value = (teacher.branch,teacher.name,teacher.surname,teacher.birthdate,teacher.gender,teacher.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} adet kayıt güncellendi.")
        except conn.Error as err:
            print(f"Hata : {err}")
    
    def getClassLessons(self):
        sql = "SELECT c.name,l.name,t.name,t.surname FROM (((classlesson as cl inner join class as c on cl.classid = c.id) inner join lesson as l on l.id=cl.lessonid)inner join teacher as t on t.id=cl.teacherid)"
        self.cursor.execute(sql)

        try:
            result = self.cursor.fetchall()
            return ClassLesson.CreateClassLesson(result)
        except conn.Error as err:
            print(f"Hata : {err}")

    def __del__(self):
        self.connection.close()
        print("Veritabanı kapatıldı")

# db = DbManager()
# student = db.getStudentById(3)
# print(student[0].name)
# print(student[0].surname)

# students = db.getStudentsByClassId(1)
# print(students[4].name)

# student = db.getStudentById(2)
# student[0].name = "Fatih"
# student[0].surname = "Candan"
# student[0].studentNumber = "321"
# db.addStudent(student[0])

# student = db.getStudentById(2)
# student[0].name = "Ali"
# db.editStudent(student[0])