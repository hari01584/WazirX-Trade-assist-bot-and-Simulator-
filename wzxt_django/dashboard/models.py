from django.db import models

class Economy(models.Model):
    instance_id = models.IntegerField(default=0)
    currencyBase = models.CharField(max_length=20)
    amount = models.DecimalField(default=0,max_digits=7, decimal_places=3)

    def __str__(self):
        return "Economy:" + self.instance_id+"%"+ self.currencyBase +"%"+ self.amount

# Create your models here.
class Transaction(models.Model):
    instance_id = models.IntegerField(default=0)
    transationType = models.CharField(max_length=10)
    currency = models.CharField(max_length=20)
    time = models.DateTimeField('Time')
    money = models.DecimalField(default=0,max_digits=7, decimal_places=4)
    rate = models.DecimalField(max_digits=7, decimal_places=7, blank=True, null=True)

    def __str__(self):
        return self.currency+"%"+ time +"%"+ money +"%"+ rate +"%"

#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
