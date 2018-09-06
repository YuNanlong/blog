from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post:post_list_by_category', args=[self.slug])

class Post(models.Model):
    POST_STATUS = (
        ('PUBLISHED', 'Published'),
        ('DRAFT', 'Draft')
    )
    category = models.ForeignKey(Category, related_name='posts')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    tags = TaggableManager()
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=POST_STATUS)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:post_detail', args=[self.publish.year, self.publish.strftime('%m'),
                        self.publish.strftime('%d'), self.slug])

    def get_published():
        return Post.objects.filter(status="PUBLISHED")
