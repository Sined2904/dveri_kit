from django.db import models

from ckeditor.fields import RichTextField


class SizeDoor(models.Model):
    """Модель размеров двери."""

    size = models.CharField(max_length=256, verbose_name='Размер двери')

    class Meta:
        ordering = ('size', )
        verbose_name = "Размер двери"
        verbose_name_plural = "Размеры дверей"

    def __str__(self):
        return self.size


class Product(models.Model):
    """Модель товара."""

    TYPE_PRODUCTS = (
        ('None', ' '),
        ('subproduct', 'Сопутствующие товары'),
        ('accessories', 'Фурнитура'),
        ('entrance_door', 'Входная дверь'),
        ('interior_door', 'Межкомнатная дверь'),
        ('window', 'Окно'),
        ('roller_shutters', 'Рольставни'),
    )
    CATEGORY = (
        ('None', '  '),
        ('royal', 'Царговые'),
        ('pvc', 'ПВХ'),
        ('veneer', 'Шпон'),
        ('laminate', 'Ламинат'),
        ('solid', 'Массив натуральный'),
    )
    type = models.CharField(
        max_length=50,
        default=None,
        choices=TYPE_PRODUCTS,
        verbose_name='Выберите тип товара'
    )
    category = models.CharField(
        max_length=50,
        default=None,
        choices=CATEGORY,
        verbose_name='Выберите тип двери (для межкомнатных дверей)'
    )
    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название товара'
    )
    price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена товара',
        blank=True,
        null=True
    )
    for_sale = models.BooleanField('Товар по акции')
    old_price = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Цена товара БЕЗ акции',
        blank=True,
        null=True
    )
    description = RichTextField(
        verbose_name='Описание товара',
        blank=True,
        null=True
    )
    size = models.ManyToManyField(
        SizeDoor,
        related_name='door',
        verbose_name='Размеры двери',
        blank=True,
    )
    subproduct = models.ManyToManyField(
        'Product',
        related_name='qwerty',
        verbose_name='Сопутка',
        blank=True,
        null=True
    )
    for_order = models.BooleanField('Под заказ')
    hit_sale = models.BooleanField('Хит продаж')

    class Meta:
        ordering = ('name', )
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name


class Article(models.Model):
    """Модель статей."""

    title = models.CharField(
        max_length=500,
        verbose_name='Заголовок статьи'
    )
    text = RichTextField(
        verbose_name='Описание товара',
        blank=True,
        null=True
    )
    date = models.DateTimeField(verbose_name='Дата публикации')

    class Meta:
        ordering = ('title', )
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


'''
class RelatedProduct(models.Model):
    """Модель сопутствующих товаров."""

    name = models.CharField(
        max_length=256,
        verbose_name='Название сопутствующего товара'
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена сопутствующего товара',
        blank=True,
        null=True
    )
    price_discount = models.PositiveIntegerField(
        verbose_name='Цена по акции',
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to="related_product/",
        verbose_name='Фото сопутствующего товара',
        blank=True,
        null=True
    )
    description = RichTextField(
        verbose_name='Описание сопутствующего товара',
        blank=True,
        null=True
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='related_products',
        verbose_name='Дверь',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = "Сопутствующий товар"
        verbose_name_plural = "Сопутствующие товары"

    def __str__(self):
        return self.name
'''


class ProductAlbum(models.Model):
    """Модель альбома изображений для товаров."""

    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название фото'
    )
    image = models.ImageField(
        upload_to="product/",
        verbose_name='Фото',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='album_product',
        verbose_name='Дверь',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = "Фотографии товара"
        verbose_name_plural = "Фотографии товаров"

    def __str__(self):
        return self.name


class ProductAlbumColor(models.Model):
    """Модель альбома изображений для расцветок товара."""

    name = models.CharField(
        max_length=250,
        null=False,
        verbose_name='Название цвета'
    )
    image = models.ImageField(
        upload_to="produst_color/",
        verbose_name='Фото',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='album_color',
        verbose_name='Дверь',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ('name', )
        verbose_name = "Фотографии расцветок товара"
        verbose_name_plural = "Фотографии расцветок товаров"

    def __str__(self):
        return self.name
