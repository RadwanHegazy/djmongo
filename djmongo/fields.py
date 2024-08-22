from uuid import UUID


class  BaseField ():
    rtype = None

    def __str__(self) -> str:
        return "BaseField"

class CharField (BaseField) : 
    rtype = str


class IntegerField (BaseField) : 
    rtype = int
    
class FloatField (BaseField) : 
    rtype = float
    
class BoolField (BaseField) : 
    rtype = bool

class UUIDField (BaseField) : 
    rtype = UUID