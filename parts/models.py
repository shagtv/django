from django.db import models
import re


def clear_name(name):
    r = re.compile(r"([^\w])|_")
    return r.sub('', name).lower()


# Create your models here.
class Brand(models.Model):
    class Meta():
        db_table = "brands"

    name = models.CharField(max_length=50)
    name_fix = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.name_fix = clear_name(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class BrandAlias(models.Model):
    class Meta():
        db_table = "brands_aliases"

    brand = models.ForeignKey(Brand)
    alias = models.CharField(max_length=50)
    alias_fix = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.alias_fix = clear_name(self.alias)
        super(BrandAlias, self).save(*args, **kwargs)

    def __str__(self):
        return self.alias


class Article(models.Model):
    class Meta():
        db_table = "articles"
        unique_together = ['brand', 'number_fix']

    brand = models.ForeignKey(Brand)
    number = models.CharField(max_length=50)
    number_fix = models.CharField(max_length=50, db_index=True)
    descr = models.TextField(default="", blank=True)
    descr_en = models.TextField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.number_fix = clear_name(self.number)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} {1}".format(self.brand, self.number)


class Cross(models.Model):
    class Meta():
        db_table = "crosses"
        unique_together = ['article', 'carticle']

    article = models.ForeignKey(Article, related_name='article_cross')
    carticle = models.ForeignKey(Article, related_name='carticle_cross')

    def __str__(self):
        return  "%s %s" % (self.article, self.carticle)