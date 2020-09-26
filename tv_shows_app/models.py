from django.db import models
import re

# import re
# class BlogManager(models.Manager):
#     def basic_validator(self, postData):    
#         errors = {}
#         EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
#         if not EMAIL_REGEX.match(postData['email']):             
#             errors['email'] = ("Invalid email address!")
#         return errors

class ShowsManager(models.Manager):
    def validation(self, postData):
        errors={}
        if len(postData['title']) < 2:
            errors['title']="Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network']="Network should be at least 3 characters"
        if len(postData['desc']) > 0 and len(postData['desc']) < 10:
            errors['desc']="Description should be at least 10 characters"
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowsManager()