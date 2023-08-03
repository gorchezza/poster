from django.db import models

class Post(models.Model):
    slug = models.SlugField(db_index=True, max_length=64, unique=True, verbose_name='URL')
    title = models.CharField(unique=True, max_length=128, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    pub_time = models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')
    upd_time = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    is_published = models.BooleanField(default=True, verbose_name='Опубликован')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url():
        ...

class Category(models.Model):
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    name = models.CharField(unique=True, db_index=True, verbose_name='Название категории', max_length=64)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url():
        ...

# class User(models.Model):
#     slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
#     name = models.CharField(unique=True, db_index=True, verbose_name='Имя')
#     email = models.EmailField(unique=True, db_index=True, verbose_name='Почта')
#     password = models.


