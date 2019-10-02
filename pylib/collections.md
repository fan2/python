# [collections](https://docs.python.org/3/library/collections.html)

collections — Container datatypes

- namedtuple(): factory function for creating tuple subclasses with named fields  
- deque: list-like container with fast appends and pops on either end  
- ChainMap: dict-like class for creating a single view of multiple mappings  
- Counter: dict subclass for counting hashable objects  
- OrderedDict: dict subclass that remembers the order entries were added  
- defaultdict: dict subclass that calls a factory function to supply missing values  
- UserDict: wrapper around dictionary objects for easier dict subclassing  
- UserList: wrapper around list objects for easier list subclassing  
- UserString: wrapper around string objects for easier string subclassing  

## OrderedDict

[Converting dict to OrderedDict](https://stackoverflow.com/questions/15711755/converting-dict-to-ordereddict)

```Python
import collections

Joe = {"Age": 28, "Race": "Latino", "Job": "Nurse"}
Bob = {"Age": 25, "Race": "White", "Job": "Mechanic", "Random": "stuff"}

#Just for clarity:
Joe = collections.OrderedDict(Joe)
Bob = collections.OrderedDict(Bob)

print(Joe)
# OrderedDict([('Age', 28), ('Race', 'Latino'), ('Job', 'Nurse')])
print(Bob)
# OrderedDict([('Age', 25), ('Race', 'White'), ('Job', 'Mechanic'), ('Random', 'stuff')])
```

## OrderedSet

[Does Python have an ordered set?](https://stackoverflow.com/questions/1653970/does-python-have-an-ordered-set)