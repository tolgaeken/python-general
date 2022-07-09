class Teacher:

    def __init__(self,id,branch,name,surname,birthdate,gender):
        
        if id is None:
            self.id = 0
        else:
            self.id = id

        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    @staticmethod
    def CreateTeacher(result):
        list=[]
        if isinstance(result,tuple):
            list.append(Teacher(result[0],result[1],result[2],result[3],result[4],result[5]))
        else:
            for i in result:
                list.append(Teacher(i[0],i[1],i[2],i[3],i[4],i[5]))
        return list