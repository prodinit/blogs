# Play with List of dictionaries in Python

## Sort a list of dictionaries in Python based on a specific key

```
list_of_dicts = [
    {"folder_name": "C", "other_key": "value1"},
    {"folder_name": "A", "other_key": "value2"},
    {"folder_name": "B", "other_key": "value3"}
]

sorted_list = sorted(list_of_dicts, key=lambda x: x['folder_name'])

>>> sorted_list 
[
    {"folder_name": "A", "other_key": "value2"},
    {"folder_name": "B", "other_key": "value3"}
    {"folder_name": "C", "other_key": "value1"},
]
```

## Extract a list of values from a list of dictionaries based on a specific key

```
list_of_dicts = [
    {"folder_name": "C", "other_key": "value1"},
    {"folder_name": "A", "other_key": "value2"},
    {"folder_name": "B", "other_key": "value3"}
]

folder_names_list = [d['folder_name'] for d in list_of_dicts]
other_keys_list = [d['other_key'] for d in list_of_dicts]

>>> folder_names_list
['C', 'A', 'B']

>>> other_keys_list
['value1', 'value2', 'value3']
```

## Flaten List of Lists

```
list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

flattened_list = [item for sublist in list_of_lists for item in sublist]

>>> flattened_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Recommended:
```
from itertools import chain

list_of_lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened_list = list(chain.from_iterable(list_of_lists))

>>> flattened_list
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### Written by - [Dishant Sethi](https://linkedin.com/in/dishantsethi)

#### Tags

<a>
<img alt="Backend Engineering" src="https://img.shields.io/badge/Backend_Engineering-8A2BE2" />
<a>
<img alt="Python" src="https://img.shields.io/badge/Python-8A2BE2" />
</a>

### Enjoyed the blog? If so, you'll appreciate collaborating with the minds behind it as well.