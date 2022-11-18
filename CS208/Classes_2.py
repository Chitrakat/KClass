from Professor import Prof


class KClass:
    def __init__(self, course_code, title, prof,
                 max_students, credit=None, num_students=0):
        # store as instance variables
        self.course_code = course_code
        self.title = title
        self.prof = prof
        self.max_students = max_students
        self.num_students = num_students
        # credit is 1 unless specified
        if credit is None:
            self.credit = 1
        else:
            self.credit = credit

    def __repr__(self):
        return f"{self.course_code}, {self.title}, {self.prof} , CR:{self.credit}\n"

    # What does @property do???
    # @property
    # def size(self):
    #     if self.max_students < 10:
    #         return "Small"
    #     if self.max_students < 15:
    #         return "Medium"
    #     else:
    #         return "LARGE"
