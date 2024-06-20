from django.db import models

# Modelo para Tipo de producto
class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.type_id + ".- " + self.name

# Modelo para Categoría
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_id + ".- " + self.name

# Modelo para Producto
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    type_id = models.ForeignKey(Type, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_id + ".- " + self.name