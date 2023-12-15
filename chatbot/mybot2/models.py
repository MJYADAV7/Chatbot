from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    age = models.IntegerField()
    def __str__(self):
        return self.name


class Questions(models.Model):
    ques_id = models.IntegerField()
    ques = models.CharField(max_length = 300)
    def __str__(self):
        return self.ques

class Sub_questions(models.Model):
    sub_ques_id = models.IntegerField()
    sub_ques = models.CharField(max_length = 300)
    ques_id = models.IntegerField()
    def __str__(self):
        return self.sub_ques

class Responses(models.Model):
    user_id = models.IntegerField()
    ques_id = models.IntegerField()
    sub_ques_id = models.IntegerField()
    answer = models.CharField(max_length = 300)

class Conversation(models.Model):
    ques = models.CharField(max_length = 300)
    answer = models.CharField(max_length = 300)
    def __str__(self):
        return self.ques
