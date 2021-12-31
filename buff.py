class DummyUpdater(object):
    def __init__(self, iterable=(), **kwargs):
        self.__dict__.update(iterable, **kwargs)

# class Passenger(DummyUpdater):
#     def __init__(self, iterable=(), **kwargs):
#        super().__init__(iterable, **kwargs)

# See the power of unpacking!
# We can create a class like this just with variables
d = DummyUpdater(first_name="abc", last_name='sgkf', middle_name='something else', title='ook iets', maturity='', doc_num='4', doc_type='1900')

# Or with a dictionary
d2 = DummyUpdater({'first_name' : 'abc', 'last_name' : 'def'}) # etc..
# d2 = Passenger({'first_name' : 'abc', 'last_name' : 'def'}) # etc..


class Employee(object):
    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])