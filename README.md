# simpvent
### A simple event manager in python

Initializing the manager
```python
from simpvent import EventHandler

def something_happened(what_happened):
  print(f"Hey! '{what_happened}' happened!")
  
manager = EventHandler()
manager.register("happened", something_happened)
```

Firing an event
```python
manager.fire("happened", "Something cool")
```

Registering several events
```python
def first(number):
  print(f"I'll do something with this '{number}'")
  
def second(number):
  print(number + 5)
  
manager.register("first", first)
manager.register("second", second)
```

Calling each event with 6
```python
manager.emit(6)
```

Removing an event
```python
manager.remove("first")
```
