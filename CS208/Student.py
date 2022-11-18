class Student:
    def __init__(self, name, id_num, yog, classes=None,
                 numclass=0, credits=0, major=None):
        self.name = name
        self.id_num = id_num
        self.doa = yog
        self.credits = credits

        if classes is None:
            self.classes = []
        else:
            self.classes = classes
        self.numclass = numclass

        if major is None:
            self.major = "Undecided"
        else:
            self.major = major

    def __repr__(self):
        return f"Name: {self.name} \n ID: {self.id_num} \n " \
               f"Courses:{self.classes} \n"

    def add_class(self, kClass):
        if (kClass.num_students != kClass.max_students) and (self.credits < 3.5):
            self.classes.append(kClass)
            kClass.num_students += 1
            self.numclass += 1
            self.credits += kClass.credit
        elif kClass.num_students == kClass.max_students:
            print(f"Class is full! Can't add {self.name} to {kClass.title}")
        elif self.credits <= 3.5:
            print(f"{self.name} can't take more courses, max credit limit reached.")

    def drop_course(self, kClass):
        found = False
        for i in self.classes:
            if i == kClass:
                found = True
                print(f"removing {kClass.course_code}")
                self.classes.remove(kClass)
                self.credits -= kClass.credit
            else:
                print("working...")
        if found is False:
            print("class could not be found... :(")

    def num_class(self):
        return self.numclass

    def declare(self, major):
        self.major = major

    '''
    checks if student has taken enough classes 
    to graduate with selected major
    '''

    def isGraduateMajor(self, major):
        if all(value in self.classes for value in major.kClass):
            print(f'{self.name} will graduate with major')
        else:
            print(f'{self.name} needs to take more classes')
