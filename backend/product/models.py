from django.db import models


class ProductType(models.Model):


    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product_type'


class ProductMeasureUnit(models.Model):


    acronym = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.acronym
    
    class Meta:
        db_table = 'product_measure_unit'


class Product(models.Model):


    name = models.CharField(max_length=255, blank=False, null=False)
    price = models.FloatField(default=0.0)
    purchase_price = models.FloatField(default=0.0)
    brand = models.CharField(max_length=255)
    quantity = models.FloatField(default=0.0)
    
    measure_unit = models.ForeignKey(
        ProductMeasureUnit,
        related_name='product_measure_unit',
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    type = models.ForeignKey(
        ProductType,
        related_name='product_type',
        on_delete=models.PROTECT,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'products'
