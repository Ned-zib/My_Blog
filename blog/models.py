from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

# Our Custom Manager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset()\
                                            .filter(status='published')

# Our models


class Post(models.Model):

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    # This is a little item to set the choices about status
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))

    # A variable that define the Title of the post, this is a Charfield type
    title = models.CharField(max_length=250)

    # Slug is a variable for made user and seo friendly urls, unique for date is in order to build the url using the publish date
    slug = models.SlugField(max_length=250, unique_for_date='publish')

    # This field define a MANY-TO-ONE relationship, meaning that each post is written by an user, the word USER on the sentence comes from the import
    # user from the Django authentication system
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_post')

    # is the 'body' of the post
    body = RichTextUploadingField(blank=True)

    # the publish date
    publish = models.DateTimeField(default=timezone.now)

    # the creating date
    created = models.DateTimeField(auto_now_add=True)

    # the las update date
    updated = models.DateTimeField(auto_now=True)

    # the actual status using the choices and a default content
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    ##
    # more types of fields on https://docs.djangoproject.com/en/3.0/ref/models/fields/.
    ##

    # Metadata with this we tell django to sort results by the publish field
    class Meta:
        ordering = ('-publish',)

    # is a default human readable representation of the object Django will use it in many places, such as the admin site

    def __str__(self):
        return self.title

    # Cannonical url
    def get_absolute_url(self):
        #pylint: disable=E1101
        return reverse('blog:post_detail',
                       args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])
