from django.db import models


# Create your models here.
class Heroes(models.Model):
    user_id = models.IntegerField(verbose_name='юзер айди')
    name = models.CharField(verbose_name='имя героя', max_length=255)
    gender = models.BooleanField(verbose_name='пол')
    apples = models.IntegerField(verbose_name='яблоки')
    moneys = models.IntegerField(verbose_name='деньги')
    health = models.IntegerField(verbose_name='здоровье')
    level = models.IntegerField(verbose_name='уровень')
    inventory = models.TextField(verbose_name='инвентарь')
    weapon = models.CharField(verbose_name='оружие', max_length=255)

    class Meta:
        db_table = 'users'
        verbose_name = 'герой'
        verbose_name_plural = 'герои'
        ordering = ['user_id', ]

    def __str__(self):
        return f'{self.name}({self.user_id}): {self.name}, {self.gender}, {self.apples}, {self.moneys}, {self.health}, {self.level}, {self.inventory}, {self.weapon}'
