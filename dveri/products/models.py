from django.db import models
from ckeditor.fields import RichTextField


class Size(models.Model):
    """Модель размеров двери."""

    size = models.CharField(max_length=256, verbose_name='Размер двери')

    class Meta:
        ordering = ('size', )
        verbose_name = "Размер двери"
        verbose_name_plural = "Размеры дверей"

    def __str__(self):
        return self.size


class Door(models.Model):
    """Модель двери."""

    CATEGORY = (
        ('entrance', 'Входные'),
        ('royal', 'Царговые'),
        ('pvc', 'ПВХ'),
        ('veneer', 'Шпон'),
        ('laminate', 'Ламинат'),
        ('solid', 'Массив натуральный'),
    )
    category = models.CharField(
        max_length=50,
        default=None,
        choices=CATEGORY,
        verbose_name='Выберите тип двери'
    )
    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название двери'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена двери',
        blank=True,
        null=True
    )
    description = RichTextField(
        verbose_name='Описание двери',
        blank=True,
        null=True
    )
    size = models.ManyToManyField(
        Size,
        related_name='door',
        verbose_name='Размеры двери',
        blank=True,
    )

    class Meta:
        ordering = ('name', )
        verbose_name = "Дверь"
        verbose_name_plural = "Двери"

    def __str__(self):
        return self.name


class DoorAlbum(models.Model):
    """Модель альбома изображений для двери."""

    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название фото'
    )
    image = models.ImageField(
        upload_to="doors/",
        verbose_name='Фото',
    )
    door = models.ForeignKey(
        Door,
        on_delete=models.CASCADE,
        related_name='album_door',
        verbose_name='Дверь',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = "Фотографии двери"
        verbose_name_plural = "Фотографии двери"

    def __str__(self):
        return self.name


class DoorAlbumColor(models.Model):
    """Модель альбома изображений для расцветок двери."""

    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название цвета'
    )
    image = models.ImageField(
        upload_to="doors_color/",
        verbose_name='Фото',
    )
    door = models.ForeignKey(
        Door,
        on_delete=models.CASCADE,
        related_name='album_color',
        verbose_name='Дверь',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = "Фотографии цветов двери"
        verbose_name_plural = "Фотографии цветов двери"

    def __str__(self):
        return self.name
