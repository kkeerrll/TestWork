from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=100)

class NetworkObject(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_country = models.CharField(max_length=100)
    contact_city = models.CharField(max_length=100)
    contact_street = models.CharField(max_length=100)
    contact_house_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_release_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


class Factory(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_country = models.CharField(max_length=100)
    contact_city = models.CharField(max_length=100)
    contact_street = models.CharField(max_length=100)
    contact_house_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_release_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class RetailNetwork(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_country = models.CharField(max_length=100)
    contact_city = models.CharField(max_length=100)
    contact_street = models.CharField(max_length=100)
    contact_house_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_release_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class IndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_country = models.CharField(max_length=100)
    contact_city = models.CharField(max_length=100)
    contact_street = models.CharField(max_length=100)
    contact_house_number = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_model = models.CharField(max_length=100)
    product_release_date = models.DateField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
