from django.db import models

class Month_saving(models.Model):
    name = models.CharField( max_length=50, blank=True)

    def __str__(self):
        return self.name
    
class Accounts(models.Model):
    account_number = models.CharField(max_length=100, blank=True)
    account_name = models.CharField(max_length=100, blank=True)
    accounty_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.account_name  + '-' + ' ' + self.account_number


class Savings(models.Model):

    amount = models.IntegerField()
    today_date = models.DateTimeField()
    month = models.ForeignKey(Month_saving, on_delete=models.CASCADE, blank=True)
    accounts = models.ForeignKey(Accounts, on_delete=models.CASCADE ,blank=True)
    #month = models.CharField(max_length=50)
    description = models.TextField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.amount}   ({self.accounts})"
