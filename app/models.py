from django.db import models

# Create your models here.
from django.db import models



class NameMaster(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class Result(models.Model):
    voter_name = models.ForeignKey("NameMaster", on_delete=models.CASCADE, related_name="voter_name")

    first_vote = models.ForeignKey("NameMaster", on_delete=models.CASCADE, related_name="first_vote")

    second_vote = models.ForeignKey("NameMaster", on_delete=models.CASCADE, related_name="second_vote")

    third_vote = models.ForeignKey("NameMaster", on_delete=models.CASCADE, related_name="third_vote")

    first_reason = models.TextField()

    second_reason = models.TextField()

    third_reason = models.TextField()

    def __str__(self):
        return str(self.voter_name) + " " + str(self.first_vote)
