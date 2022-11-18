from Classes_2 import KClass
from Student import Student
from Professor import Prof
from majors import Major

# Creating Professors
bose = Prof("Bose")
steven = Prof("Steven")
meep = Prof("Meep")

# Creating Courses
cs208 = KClass("CS208", "Programming Languages", bose, max_students=3)
cs310 = KClass("CS310", "HARD CS CLASS", bose, max_students=5)
math200 = KClass("Math200", "MATHS", bose, max_students=3)
phil219 = KClass("PHIL219", "Global Aesthetics", steven, max_students=2)
mus100 = KClass("MUS100", "Choir", meep, max_students=2, credit=0.5)

# creating majors
undecided = Major("Undecided Major", None)
BscCS = Major("Bsc in Computer Science", kClass=[cs208, cs310, math200])

# Creating Students
suyash = Student("Suyash Chitrakar", 761185, 2025)
ari = Student("Ari Zona", 131241, 2023)
lateBird = Student("Late Bird", 889455, 2025)

# # # ------ Test Cases ------

# Test cases for adding classes
suyash.add_class(cs208)
suyash.add_class(phil219)
suyash.add_class(math200)
suyash.add_class(mus100)

# demonstrating max credits student can take (3.5)
suyash.add_class(cs310)
ari.add_class(phil219)

# demonstrating max students a class can have
lateBird.add_class(phil219)

# test cases for removing a class
print("\n", suyash)
suyash.drop_course(mus100)
suyash.drop_course(phil219)
print(f"After dropping:"
      f"{suyash.classes} "
      f"credits: {suyash.credits}")
suyash.add_class(cs310)

# # tests for majors
# print(suyash.major)
suyash.declare(BscCS)
print(suyash.classes)
suyash.isGraduateMajor(BscCS)
ari.isGraduateMajor(BscCS)
