from pymongo import MongoClient
from django.conf import settings
from inspect import getmembers
from . import data_manager



class Model(
    data_manager.RetriveData,
    data_manager.FilterData,
    data_manager.CreateData,
    data_manager.DeleteData,
    data_manager.UpdateData,
) :
    """
        Main Model For implement CRUD on the mongodb
    """
    def __init__(self, *args, **kwargs) -> None:
        try : 
            self.mongodb = settings.MONGODB.get('SERVER')
            self.mongodb = self.mongodb.client
        except Exception as error:
            raise Exception("An error accoured while connect to mongodb server")
        self.collection = self.__class__.__name__
        tuple_fields = getmembers(self)
        self.fields = {}
        # check user-define  fields 
        for f in tuple_fields:
            field_name, field_type = f[0], f[1]
            if str(field_type) == "BaseField":
                self.fields[field_name] = field_type




class MongoServer:
    """
        Connect To Mongodb Protocol
    """ 
    
    def __init__(self, host='localhost', port=27017, db_name='default') -> None:
        self.__mongo = MongoClient(host, port)
        self.__db_name = db_name

    @property
    def client(self) :
        return self.__mongo[self.__db_name]


