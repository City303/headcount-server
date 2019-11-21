from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator

# Create your models here.
class Classroom(models.Model):

    ''' Classroom fields '''
    department = models.CharField(max_length=4)   # i.e. CSCE, HIST
    number     = models.CharField(max_length=5)   # i.e. 3193, 2074H
    name       = models.CharField(max_length=200) # i.e. "Programming Paradigms"
    professor  = models.CharField(max_length=200) # i.e. "Dr. John Doe", "Dr. Garret Gardenhire, Ph.D."
    class_code = models.CharField(max_length=6, editable=False, unique=True, null=True, default=None) # i.e. "A9BDX3" (randomly generated)
    students   = models.ManyToManyField('Student', blank=True)
    active     = models.BooleanField(default=False) # Class code is generated when class is active


    ''' String representation '''
    def __str__(self):
        if self.class_code is not None:
            return (self.department + " " + self.number + " " + self.name + " " + self.class_code)
        return (self.department + " " + self.number + " " + self.name + " (inactive)")


    ''' Updates the class code upon save / queryset update of active '''
    def update_class_code(self):
        if(self.active == False):
            self.class_code = None

        elif(self.active == True and self.class_code == None):
            self.class_code = get_random_string(6).upper()


    ''' Actions to perform upon saving '''
    def save(self, *args, **kwargs):
        self.update_class_code()
        return super(Classroom, self).save(*args, **kwargs)




class Student(models.Model): 
    YEAR_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'), 
        ('SR', 'Senior'),
        ('GR', 'Graduate')
    ]

    numeric = RegexValidator(r'^[0-9]*$', 'Only numeric student IDs (consisting of 0-9) are allowed.')

    student_id = models.CharField(max_length=9, validators=[numeric]) # Student ID
    name       = models.CharField(max_length=200)                     # First and last name
    year       = models.CharField(max_length=2, choices=YEAR_CHOICES, default='FR')

    def __str__(self):
        return (self.name + " " + str(self.student_id) + " " + self.year)



class AttendanceTransaction(models.Model):
    student = models.OneToOneField('Student', on_delete=models.CASCADE)
    classroom = models.OneToOneField('Classroom', on_delete=models.CASCADE)
    time = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        # On creation, set the time field to current time
        if not self.id:
            self.time = timezone.now()
        return super(AttendanceTransaction, self).save(*args, **kwargs)

    def __str__(self):
        return (str(self.student.name) + " at " + str(self.classroom.name) + " on " + self.time.strftime("%m/%d/%y"))
