from django.db import models

class Submission(models.Model):
    GENDER = [('m','Male'),('f','Female'),('o','Other')]

    name = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    dob = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    age = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)
    aadhaar = models.FileField(upload_to='uploads/docs/', null=True, blank=True)
    tenth = models.FileField(upload_to='uploads/docs/', null=True, blank=True)
    country = models.CharField(max_length=50, blank=True)
    hobbies = models.CharField(max_length=200, blank=True)  # comma-separated
    color = models.CharField(max_length=7, blank=True)      # #RRGGBB
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
