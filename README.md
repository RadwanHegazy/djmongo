# DjMongo
this is package for connect your django models with mongodb and create CRUD operation on it.

## How to install

Open your django project then type

```
git clone https://github.com/RadwanHegazy/djmongo
```

```python
# Add package to INSTALLED_APPS

INSTALLED_APPS = [
    ...
    'djmongo',
    ...
]


# connect your djmongo to your mongodb server
from djmongo.models import MongoServer

MONGODB = {
    'SERVER' : MongoServer()
}
```

### MongoServer Takes 3 parameters : 
- host [default=localhost]
- port [default=27017]
- db_name [default=defualt]


<b>by just enter MongoServer() you connected with the mongodb server by the 
default parameters, you can edit what you want in connection.</b>



## How to Use 

```python
# models.py

from djmongo.models import Model
from djmongo import fields

class User(Model) : 
    username = fields.CharField()
    age = fields.IntegerField()
```


```python
# views.py
from django.http import JsonResponse
from your_app.models import User

def your_view (request) : 
    user = User() # pick up our model

    # create new user
    # NOTE: it will push you an error if you try to add a field does not exists 
    user.create(
        username='radwan',
        age=19,
    )

    # for delete user
    user.delete(
        username='radwan',
    )

    # get user from users
    user.get(
        username='radwan',
        age=19,
    )

    # fetch all users
    users_list = users.all()
    
    # update user
    users.update(
        get_by={
            'age' : 19
        },
        updated_fields={
            'username' : 'Radwan Gaber'
        }
    )
    
    return JsonResponse(users_list, safe=False)

```
