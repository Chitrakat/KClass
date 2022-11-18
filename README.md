# KClass

File main.py is the file where all actions must take place ( ie creating new students, majors, professors and classes)
Only create all objects there otherwise the program will not work as intended.

This program is able to create students, classes, majors and professors. It is able to simulate most needs of colleges except for more complex searches.

# Class Student

Class student has variables like name, ID number, year of graduation, a list of classes, a counter for number of classes they are taking, credits and major.
When instantiating a student it is not required to add classes, numclass, credits and majors as it will break the program unless if you add a class along with all other correct information like numclass credits and major.
 
**Adding classes**

Adding classes require a class to me made. The method takes in a class as kClass. A student can only take a class if they have lesser than 3.5 credits or if the class is not full yet. Succesfully adding a student to a class decreses the available seats in the class and also adds credit worth the class in the students data, works with 1 and 0.5 credit classes.
If classes are full or if student has maximum number of credits the program denies adding the class and throws an error (_just prints stuff_).

**Drop Course**

Dropping courses takes in parameter Class as kClass. The method searches if the student is taking the course or not. If they are not taking the course the program outputs that the class was not found. If the class was found the method removes the class from student and also reduces credits that the class was worth, thus it works with 1 and 0.5 credit classes.
 
**Declare** 

This method takes in parameter major and simply declares the students major

**isGraduateMajor**
This method takes in a major as a parameter and checks if the student is able to graduate with the major OR if the student will have to take additional classes to graduate with major.

# KClass
Kclass has parameters course code, title, professor, maximum students, credits and num students. Thus each class has all of those and is able to have dynamic credits (ie 1 , 0.5 1.5 etc), maximum students and current number of students enrolled in class to check available seats. 
A class has 1 credits unless specified like:
```
mus100 = KClass("MUS100", "Choir", meep, max_students=2, credit=0.5)
```

# Majors
Class major only takes in name and a list of classes which constitute the major. This class is relatively barebones as all the logic required is in class student.

# Prof
Class Prof only takes in the name of the professor. A professor is required for a class to be made, thus is an integral part of the program.


