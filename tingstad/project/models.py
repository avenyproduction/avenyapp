from django.db import models

# Create your models here.
class Projects(models.Model):
    projectID = models.AutoField(primary_key=True)
    #companyID = foreign key
    #customerID = foreign key
    yourProjectNo = models.CharField(max_length=50)
    ourProjectNo = models.CharField(max_length=50)
    yourRefPersonName = models.CharField(max_length=200)
    ourRefPersonName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    # phoneNo
    # cellNo
    # asdress
    # city
    # zipCode
    # country
    #addion in percent to add to the price for the material cost
    addForMaterial = models.FloatField(default=1)
    #addition in percent to add to the price for the subcontractor
    addForSubCon = models.FloatField(default=1)

    def __str__(self):
        return self.testColumn

    class Meta:
        db_table = 'projects'
