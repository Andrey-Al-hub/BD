from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(verbose_name="Наименование", max_length=75)
    category = models.CharField(verbose_name="Категория", max_length=25)
    # category = models.ForeignKey("Category", on_delete=models.CASCADE) # не знаю что писать в ограничение при удалении
    price = models.IntegerField(verbose_name="Цена") # не Decimal???
    # price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    amount = models.IntegerField(verbose_name="Количество")
    expiration_date = models.DateTimeField(verbose_name="Срок годности", null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="photos/", null=True, blank=True)
    description = models.TextField(verbose_name="Описание", max_length=1000, null=True, blank=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,
                                    verbose_name="Производитель") # id к названию не надо добавлять Django при миграции сам добавит

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
    operation_type = models.CharField(verbose_name="Тип операции", max_length=15)
    percent = models.IntegerField(verbose_name="Процент", null=True, blank=True)

    def __str__(self):
        return self.operation_type

    class Meta:
        db_table = 'operation_type'
        verbose_name_plural = 'Типы операций'
        verbose_name = 'Тип операции'

# CREATE TABLE sys_user (
# 	login VARCHAR(20) PRIMARY KEY NOT NULL,
# 	password VARCHAR(20) NOT NULL,  
# 	role VARCHAR(15) NOT NULL
# );

# Тут посмотреть про юзеров уже в Django
# А пустые или с значением NULL строк не будет???
# Может правда добавить таблицу с катигорией? Легче будет получать данные
# Также это будет нормализация данных
# Можно потом сделать выборку (отображение) по категориям используя просто данную таблицу

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

# class Category(models.Model):
#     name = models.CharField("Категория", max_length=25)

#     def __str__(self):
#         return self.name

#     class Meta:
#         db_table = 'category'
