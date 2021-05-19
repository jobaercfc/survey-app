from django.db import models

# Create your models here.
from django.db import models



class NameMaster(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Result(models.Model):
    voter_name = models.ForeignKey("NameMaster", on_delete=models.CASCADE)

    first_vote = models.TextField()

    second_vote = models.TextField()

    third_vote = models.TextField()

    first_reason = models.TextField()

    second_reason = models.TextField()

    third_reason = models.TextField()

    def __str__(self):
        return str(self.voter_name) + " " + str(self.first_vote)
