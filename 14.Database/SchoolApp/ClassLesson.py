class ClassLesson:

    def __init__(self,classname,lessonname,teachername,teachersurname):

        self.classname = classname
        self.lessonname = lessonname
        self.teachername = teachername
        self.teachersurname= teachersurname

    @staticmethod
    def CreateClassLesson(obj):
        list=[]
        for i in obj:
            list.append(ClassLesson(i[0],i[1],i[2],i[3]))
        return list
