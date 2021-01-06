from django.contrib import admin
# import of the model that we want see in the admin site
from .models import Post

# Register your models here.
@admin.register(Post) #this decorator make the same thing as admin.site.register()

#customizing the admins site, how the site show you the information
class PostAdmin(admin.ModelAdmin):

    #how django show the info
    list_display = ('title', 'slug', 'author', 'publish', 'status')

    #you can add filters
    list_filter = ('status', 'created', 'publish', 'author')

    #you can add search fields criteria
    search_fields = ('title', 'body')

    #create a relation between fields
    prepopulated_fields = {'slug': ('title',)}

    #this is in order to use the id insted of the name just in case for instance if you have thousand of users
    raw_id_fields = ('author',)

    #add a bar to navigate with links
    date_hierarchy = 'publish'

    #default order
    ordering = ('status', 'publish')