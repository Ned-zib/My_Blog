# Django super notes

## Creating a Project
Just create it 
```python
    $ django-admin startproject projectName
```
## Creating an application
```python
    $ python manage.py stratapp appName
```
## Runing the develop server
this is only a lightweight server not for production
```python
    $ python manage.py runserver
```
## Migration important things
When you add an application to the settings part you have to Create and Apply migrations
use this:
```python
    $ python manage.py makemigrations appName
```

if you want to check the SQL code that Django execute in the database just type
```python
    $ python manage.py sqlmigrate appName migrationNumber
    
    Example:
    $ python manage.py sqlmigrate blog 0001
```
then sync your database with the new model. Run the following command to apply existing migrations:
```python
    $ python manage.py migrate
```
## Creating a super user
In order to use the admin site please use this first
```python
    $ python manage.py createsuperuser
```
## Admin Site
after you run the server you can go to
>  http://127.0.0.1:8000/admin/

## Adding a model to the admin site
Edit the admin py and import the model that you want and then register the class
```python
    $ from .models import modelName
    $
    $ admin.site.register(modelName)
```

# ORM
 Django ORM is based on QuerySets wich is a collection of database queries to retrieve objects from the DB.

 Open the terminal and run the following command to open the Python shell:
```python
    $ python manage.py shell
```

# The CRUD
## Creating objects (CREATE)

When you create a model the model comes with some methods, one of them is create() in this example we created a model called post with some attributes

```python
    $ Post.objects.create(title='One more post',
                          slug='one-more-post',
                          body='Post body.',
                          author=user)
```

## Getting objects (READ)

In order to get objects you can use get() and provide the method with a parameter

```python
    $ Post.objects.get(title="One more post")
```

If the item does not exist will raise a DoesNotExist exception, if there are more than one result, will raise a MultipleObjectsReturned exception

## Updating Objects (UPDATE)

after you get an object you can update it using the next way

```python
    $ post = Post.objects.get(title="One more post")
    $ post.title = "One more post updated"
    $ post.save()
```

is important use save() in order to the changes can persist in the database save() makes an UPDATE SQL statement

## Deleting Objects (DELETE)

If you want to delete an object, you can do it using Delete()

```python
    $ post = Post.objects.get(title="One more post")
    $ post.delete()
```

# More utils 

## Retrieving all objects in a QuerySet
### All objects
```python
    $ all_post = Post.object.all()
    $ all_post
```
## Using the filter() method
your object have parameters so you can filter the objects that meet the parameter, this return a QuerySet not an Object itself please be aware
```python
    $ post = Post.object.filter(publish__year=2020)
    $ post
```
this will return a QuerySet with all the post published in 2020 this also works with multiple fields
```python
    $ post = Post.object.filter(publish__year=2020,
                                author___username="admin")
```
## Using Exclude() method
You can exclude certain results from your QuerySet using Exclude() method so you can get for example all the post published in 2020 avoiding whose titles start with "Why"
```python
    $ Post.objects.filter(publish__year=2020) \
                  .exclude(title__startswith="Why")
```
## Using order_by() method
You can also retrieve objects with an order for example by title
```python
    $ Post.objects.order_by('title')
    #Or in a descending order
    $ Post.objects.order_by('-title')
```