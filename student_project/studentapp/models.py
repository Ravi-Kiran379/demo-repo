# from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    STUDENT_ID = models.AutoField(primary_key=True)
    NAME = models.CharField(max_length=45, default='Doctor')
    COUNTRY_CODE = models.IntegerField()
    MOBILE_NO = models.CharField(max_length=16)
    EMAIL = models.CharField(max_length=63)
    EMAIL_VERIFIED = models.BooleanField(default=False)
    EDUCATION = models.CharField(max_length=30, null=True, blank=True)
    COLLEGE = models.CharField(max_length=255, null=True, blank=True)
    ADDRESS_STATE = models.CharField(max_length=150, null=True, blank=True)
    ADDRESS = models.CharField(max_length=512, null=True, blank=True)
    PROFILE_STATUS = models.CharField(max_length=20)
    PASSWORD = models.CharField(max_length=255)
    DELETED = models.BooleanField(default=False)
    UNIQUE_TOKEN = models.CharField(max_length=255, null=True, blank=True)
    DEVICE_ID = models.CharField(max_length=255, null=True, blank=True)
    OTP = models.CharField(max_length=6, null=True, blank=True)
    OTP_SENT_AT = models.DateTimeField(null=True, blank=True)
    FORGOT_PASSWORD_SENT_AT = models.DateTimeField(null=True, blank=True)
    PASSWORD_UPDATED_AT = models.DateTimeField(null=True, blank=True)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'STUDENT'

    def __str__(self):
        return self.NAME
