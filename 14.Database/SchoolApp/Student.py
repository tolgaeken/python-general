class Student:

    def __init__(self,id,studentNumber,name,surname,birthdate,gender,classid):
        
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender
        self.classid = classid
    
    @staticmethod
    def CreateStudent(result):
        list = []

        if isinstance(result,tuple):
            list.append(Student(result[0],result[1],result[2],result[3],result[4],result[5],result[6]))
        else:
            for i in result:
                list.append(Student(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))
        return list