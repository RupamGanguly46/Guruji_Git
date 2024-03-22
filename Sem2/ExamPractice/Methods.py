class tmp:

    # on printing object, this method will handle the printing of the object/instance
    def __str__(self):
        return 'hello'
    
    # it handles representation of object other than printing
    def __repr__(self):
        return 'hi'
    
obj1=tmp()
print(obj1)

