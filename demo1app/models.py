from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login_view(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)



class Student_registration(models.Model):
    user = models.OneToOneField(Login_view,on_delete=models.CASCADE,related_name='student',null=True)
    name = models.CharField(max_length=200)
    reg_id = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.IntegerField()
    address = models.CharField(max_length=300)
    stud_image = models.ImageField(upload_to="images")
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Parent_registration(models.Model):
    user = models.OneToOneField(Login_view, on_delete=models.CASCADE,related_name='parent',null=True)
    parent_name = models.CharField(max_length=100)
    student_name = models.ForeignKey(Student_registration,on_delete=models.CASCADE)
    reg_id = models.CharField(max_length=30)
    email = models.EmailField()
    phone_no = models.IntegerField()
    address = models.CharField(max_length=300)
    approval_status = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name

class Hostal(models.Model):
    hostel_name = models.CharField(max_length=250)
    location = models.CharField(max_length=500)
    room_fecilities = models.CharField(max_length=300)
    contact_no = models.IntegerField()
    hostel_image = models.ImageField(upload_to="hostal")

    def __str__(self):
        return self.hostel_name

class Food(models.Model):
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    snacks = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)


    def __str__(self):
        return self.dinner

class Fee(models.Model):
    hostel_name = models.ForeignKey(Hostal, on_delete=models.CASCADE)
    mess_bill = models.IntegerField()
    room_rent = models.IntegerField()
    amount = models.IntegerField()




    def __str__(self):
        return self.amount

class Payment(models.Model):
   studentname = models.ForeignKey(Student_registration,on_delete=models.CASCADE)
   from_date = models.DateField()
   to_date = models.DateField()
   room_rent = models.IntegerField()
   mess_bill = models.IntegerField()
   amount = models.IntegerField()
   paymentstatus = models.IntegerField(default=0)

   def __str__(self):
       return self.amount

class Attendance(models.Model):

   studentname = models.ForeignKey(Student_registration,on_delete=models.CASCADE)
   date = models.DateField()
   status = models.CharField(max_length=100)

   def __str__(self):
        return self.status

class Staff(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contact_no = models.IntegerField()


    def __str__(self):
        return self.contact_no


class Notification(models.Model):
    date= models.DateField()
    message = models.CharField(max_length=300)


    def __str__(self):
        return self.date


class Complaint(models.Model):
    user = models.ForeignKey(Login_view,on_delete=models.CASCADE)
    date = models.DateField()
    complaint = models.CharField(max_length=300)
    replay = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=20)
    date = models.DateField()
    review = models.CharField(max_length=300)


    def __str__(self):
        return self.date

class Booking(models.Model):
    name = models.CharField(max_length=20)
    booking_date = models.DateField()
    date_joining= models.DateField()
    status=models.IntegerField(default=0)


    def __str__(self):
        return self.status
