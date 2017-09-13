from __future__ import unicode_literals
from django.contrib import messages

from django.db import models
import re, bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Model):
    def register(self, postData, request):
        if User.objects.filter(email = postData['email']).exists():
            messages.error(request, "Someone is already registerd with this email address. If it is you, then login instead.")
        else:
            if len(postData['fname']) >=2 :
                if len(postData['lname']) >=2 :
                    if re.match('^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
                        if len(postData['pword']) >= 8:
                            if postData['cpword'] == postData['pword']:
                                hashedpword = bcrypt.hashpw(str(postData['pword']),bcrypt.gensalt())
                                User.objects.create(first_name=postData['fname'], last_name=postData['lname'], email=postData['email'], password=hashedpword)
                                request.session['id']=
                                User.objects.only('id').get(email = postData['email']).id
                                request.session['first_name']= postData['fname']
                                return True
                            else:
                                messages.error(request, "Your confirmation and password do not match")
                                return False
                        else:
                            messages.error(request, "Your password must be at least 8 characters.")
                            return False
                    else:
                        messages.error(request, "Your email must be in proper format- Ex.'JohnDoe@email.com'")
                        return False
                else:
                    messages.error(request, "Your last name must have at least 2 characters")
                    return False
            else:
                messages.error(request, "Your first name must have at least 2 characters")
                return False
    def login(self, postData, request):
        if User.objects.filter(email = postData['email']).exists()
            print "#"*50
            print postData['email']
            print "#"*50
            hashedpword = str(User.objects.only('password').get(email=postData["login_email"]).password)
            if hashedpword == bcrypt.hashpw(str(postData['login_pword']), hashedpword):
                request.session['id'] = User.objects.only('id').get(email=postData["login_email"]).id
                request.session['first_name'] = User.objects.only('first_name').get(email=postData["email"]).first_name
                return True
            else:
                messages.warning(request, 'The password you entered does not match the one we have saved for this email address.')
                return False
        else:
            messages.warning(request, "We do not have anyone registered with this email address.")
            return False




class User(models.Model):
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    email = models.CharField(max_length=44)
    password = models.CharField(max_length=44)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Secret(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

class Like(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    secret = models.ForeignKey(Secret)
