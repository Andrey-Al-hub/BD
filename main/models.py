from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=75)
    category = models.CharField(verbose_name="Категория", max_length=25)
    price = models.IntegerField(verbose_name="Цена")
    amount = models.IntegerField(verbose_name="Количество")
    expiration_date = models.DateTimeField(verbose_name="Срок годности", null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="img/", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", max_length=1000, null=True, blank=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,
                                    verbose_name="Производитель")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'


class Manufacturer(models.Model):
    manufacturer = models.CharField(verbose_name="Производитель", max_length=40)
    city = models.CharField(verbose_name="Город", max_length=15)

    def __str__(self):
        return self.manufacturer

    class Meta:
        db_table = 'manufacturer'
        verbose_name_plural = 'Производители'
        verbose_name = 'Производитель'


class Operation_type(models.Model):
    operation_type = models.CharField(verbose_name="Тип операции", max_length=40)
    percent = models.IntegerField(verbose_name="Процент", null=True, blank=True)

    def __str__(self):
        return self.operation_type

    class Meta:
        db_table = 'operation_type'
        verbose_name_plural = 'Типы операций'
        verbose_name = 'Тип операции'


class Operation_on_product(models.Model):
    doc_creation_date = models.DateTimeField(verbose_name="Дата создания документа")
    operation_type = models.ForeignKey("Operation_type", 
                                    on_delete=models.CASCADE, verbose_name="Тип операции")
    product = models.ForeignKey("Product", on_delete=models.CASCADE,
                                verbose_name="Товар")
    amount_of_product = models.IntegerField("Количество товаров")
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            verbose_name="Пользователь")

    class Meta:
        db_table = 'operation_on_product'
        verbose_name_plural = 'Операции над товаром'
        verbose_name = 'Операция над товаром'
