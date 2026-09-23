from django.db import models
from django.contrib.auth.models import User

class Hotels(models.Model):
    name=models.CharField(max_length=150,verbose_name="Название")
    discription=models.TextField(verbose_name="Описание")
    adress=models.CharField(max_length=150,verbose_name="Адрес")
    city=models.CharField(max_length=150,verbose_name="Город")
    foto=models.ImageField(upload_to="hotels/",verbose_name="Фото")
    reiting=models.IntegerField(verbose_name="ОТ 1 ДО 5 Оценка")

    class Meta:
        verbose_name="Отел"
        verbose_name_plural="Отели"

    def __str__(self):
        return self.name

class Numbers(models.Model):
    TYPE_CHOICES=(
        ("massege","Стандарт"),
        ("massege","Улушенный"),
        ("massege","Делюкс"),
        ("massege","Сьют"),
        ("massege","Апартаменты"),
    )
    name=models.CharField(max_length=150,verbose_name="Номер")
    discription=models.CharField(verbose_name="Тип номера",choices=TYPE_CHOICES)
    price_for_day=models.IntegerField(verbose_name="Цена за ночь")
    count=models.IntegerField(verbose_name="Количество месть")
    foto=models.ImageField(upload_to="hotels/numbers/",verbose_name="Фото")
    availability=models.BooleanField(default=True,verbose_name="Доступность")

    class Meta:
            verbose_name="Номер"
            verbose_name_plural="Номера"
    
    def __str__(self):
            return self.name

class Booking(models.Model):
    user=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Пользователь")
    nombers=models.ForeignKey(Numbers,on_delete=models.CASCADE,verbose_name="Номер")
    data=models.DateField(verbose_name="Дата заезда")
    data_out=models.DateField(verbose_name="Дата выезда")
    guest_count=models.IntegerField(verbose_name="Количество гостей")
    endprice=models.IntegerField(verbose_name="Общая цена")
    status=models.BooleanField(default=False,verbose_name="Статус бронирования")

    class Meta:
            verbose_name="Бронирование"
            verbose_name_plural="Бронирования"

    def __str__(self):
            return f"Бронирование {self.user.username} - {self.nombers.name}"

class Reviews(models.Model):
    user=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Пользователь")
    hotel=models.ForeignKey(Hotels,on_delete=models.CASCADE,verbose_name="Отель")
    text=models.TextField(verbose_name="Отзыв")
    rating=models.IntegerField(verbose_name="Оценка от 1 до 5")
    

    class Meta:
            verbose_name="Отзыв"
            verbose_name_plural="Отзывы"

    def __str__(self):
            return f"Отзыв {self.user.username} - {self.hotel.name}"

