class SingeltonObject(object):
    class __SingeltonObject():
        def __init__(self):
            self.val = None
        
        def __str__(self):
            return "{0!r} {1}".format(self, self.val)

    instance = None

    def __new__(cls):
        if not SingeltonObject.instance:
            SingeltonObject.instance = SingeltonObject.__SingeltonObject
        return SingeltonObject.instance

    def __getattribute__(self, name):
        return getattr(self.instance, name)
    
    def __setattr__(self, name):
        return setattr(self.instance, name)

 
