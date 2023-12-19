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



class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField(null=False)
    order_status = models.IntegerField(null=False)
    order_payment_status = models.IntegerField(null=False)
    order_amount = models.IntegerField(null=False)
    user_id = models.ForeignKey(GamifyUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "order"


class OrderDetail(models.Model):
    orderdetail_id = models.AutoField(primary_key=True)
    orderdetail_quantity = models.IntegerField(null=False)
    orderdetail_amount = models.IntegerField(null=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

    class Meta:
        db_table = "orderdetail"


class Wishlist(models.Model):
    wishlist_id = models.AutoField(primary_key=True)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_id = models.ForeignKey(GamifyUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "wishlist"


class Feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    feedback_date = models.DateField()
    feedback_des = models.CharField(max_length=500)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    user_id = models.ForeignKey(GamifyUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "feedback"


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    cart_quantity = models.IntegerField(null=False)
    cart_amount = models.IntegerField(null=False)
    cart_added_date = models.DateField(null=False)
    user_id = models.ForeignKey(GamifyUser, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, on_delete=models.PROTECT)

    class Meta:
        db_table = "cart"
