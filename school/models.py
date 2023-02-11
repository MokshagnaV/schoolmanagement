from django.db import models

# Create your models here.

class student(models.Model):
    stu_id=models.CharField(max_length=100, primary_key=True)
    stu_name=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    gender=models.CharField(max_length=20)
    email=models.EmailField()
    pwd=models.CharField(max_length=100)
    dob=models.DateField()
    school=models.CharField(max_length=100)
    present_class=models.IntegerField()
    mobile=models.CharField(max_length=10)
    #photo=models.FileField(upload_to="images")

    def __str__(self) :
        return f"{self.stu_id},{self.stu_name},{self.email}"
 
class buddy(models.Model):
    buddy_id = models.CharField(max_length=100, primary_key=True)
    buddy_name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models. EmailField()
    pwd = models.CharField(max_length=100)
    dob = models.DateField()
    designation = models.CharField(max_length=100)
    workplace = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    #photo = models.ImageField()

    def __str__(self) :
        return f"{self.buddy_id},{self.buddy_name},{self.email}"

class school_admin(models.Model):
    school_admin_id = models.CharField(max_length=100, primary_key=True)
    school_admin_name = models.CharField(max_length=100)
    school_id = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models. EmailField()
    pwd = models.CharField(max_length=100)
    dob = models.DateField()
    designation = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    #photo = models.ImageField()

    def __str__(self) :
        return f"{self.school_admin_id},{self.school_admin_name},{self.email}"
