# Ex02 Django ORM Web Application
## Date: 15-10-2024

## AIM
To develop a Django application to store and retrieve data from a Bank database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
![Screenshot 2024-11-16 213246](https://github.com/user-attachments/assets/c1fe90b7-99fe-44ca-abd7-d5c4b52f677e)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 customers.

## PROGRAM
```


models.py
from django.db import models
from django.contrib import admin 
class BankLoan(models.Model):
  acc=models.IntegerField(primary_key="accno")
  ph=models.IntegerField()
  ifsc=models.CharField(max_length=100)
  loanno=models.IntegerField()
  adress=models.CharField(max_length=100)
  pan=models.IntegerField()
  adhar=models.IntegerField()

class BankLoanAdmin(admin.ModelAdmin):
 list_display=('acc','ph','ifsc','loanno','adress','pan','adhar',)

admin.py
from django.contrib import admin
from .models import BankLoan,BankLoanAdmin
admin.site.register(BankLoan,BankLoanAdmin)



```

## OUTPUT
![Screenshot 2024-11-16 142006](https://github.com/user-attachments/assets/3e2cf28a-d8b7-48c2-9466-d840f5955400)


Include the screenshot of your admin page.


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
