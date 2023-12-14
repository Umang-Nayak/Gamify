from django.db import models


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=50)

    class Meta:
        db_table = "City"


class GamifyUser(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100)
    user_date_of_birth = models.DateField()
    user_contact = models.CharField(max_length=15)
    user_email = models.EmailField(unique=True)
    user_password = models.CharField(max_length=50)
    is_admin = models.IntegerField(null=True)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    user_otp = models.IntegerField(null=True)
    user_otp_used = models.IntegerField(null=True)

    class Meta:
        db_table = "GamifyUser"


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=500)

    class Meta:
        db_table = "Company"


class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=100)

    class Meta:
        db_table = "Type"


class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_name = models.CharField(max_length=100)
    game_version = models.CharField(max_length=100)
    game_image = models.CharField(max_length=100)
    game_price = models.IntegerField()
    game_launch_date = models.DateField()
    game_quantity = models.IntegerField()
    game_description = models.CharField(max_length=500)
    is_available = models.IntegerField(null=True)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        db_table = "Game"
