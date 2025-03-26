from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django import forms
from django.db import models
from django.contrib.auth.models import User

class Homework(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='homeworks/', blank=True, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.student.username}"


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True,unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)#nesnenin title ına göre slugify nesne oluşturacak
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False,blank=True, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category, blank=True)
    #category = models.ForeignKey(Category, default=1,on_delete=models.CASCADE) #CASCADE İLE KATEGORİSİ OLMAYAN BLOGLAR SİLİNir.
    #set_null ile null olarak kalabilirler.#set_default ile default bir değer belirleriz, silinen kategori için bu default u alır.
    
    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)#nesnenin title ına göre slugify nesne oluşturacak
        super().save(*args, **kwargs)
    
