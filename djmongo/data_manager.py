"""
    Data manager depends on all operation for data that is saved on the db.
"""

class Base:
    """
        Base Model For Used for make iteration and return data without key '_id'
    """
    @staticmethod
    def _data_itr (x) :
        """
            Remove Object_id from returned data
        """
        x.pop('_id')
        return x

    def _validate(self, **kwargs) :
        model_keys = self.fields.keys()
        user_enter_keys = kwargs.keys()
        for k in user_enter_keys:
            if k not in model_keys : 
                raise Exception(f"key='{k}' not defind in model='{self.collection}' ")


class RetriveData(Base):
    """
        Depends on retriving data : 
            - get: one pience of data
            - all:  get all data
    """
    def get (self, **kwargs) :
        data = self.mongodb[self.collection].find_one(kwargs)
        data.pop('_id')
        return data
    
    def all (self):
        data = map(self._data_itr, self.mongodb[self.collection].find())
        return list(data)
    
    
    

class FilterData:
    """
        Filter the data on the db
    """
    def filter (self, **fields):
        self._validate(**fields)
        data = map(self._data_itr, self.mongodb[self.collection].find(fields))
        return list(data)
    

class CreateData:
    """
        Create new database object
    """
    def create (self, **kwargs) : 
        self._validate(**kwargs)
        self.mongodb[self.collection].insert_one(kwargs)

class DeleteData:
    """
        Delete object from db
    """
    def delete (self, **kwargs) :
        self._validate(**kwargs)
        self.mongodb[self.collection].delete_one(kwargs)


class UpdateData:
    """
        Update data on the db
    """
    def update (self, get_by:dict, updated_fields:dict) : 
        self._validate(**updated_fields)
        self.mongodb[self.collection].update_one(
            get_by,
            {'$set':updated_fields}
        )