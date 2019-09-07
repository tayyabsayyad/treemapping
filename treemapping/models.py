from django.contrib.gis.db import models


class TreeData(models.Model):
    treeID = models.IntegerField(default=0)
    location = models.PointField()
    commonName = models.CharField(max_length=100)
    scientificName = models.CharField(max_length=100)
    trunkDiameter = models.IntegerField(default=0)
    treeHeight = models.IntegerField(default=0)
    datePlanted = models.DateTimeField(auto_now=True)
    condition = models.CharField(max_length=100)
    treeStewardship = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField(default=413405)

