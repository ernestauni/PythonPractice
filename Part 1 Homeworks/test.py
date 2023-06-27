from typing import List, Tuple, Dict, Any

def select(*args: str) -> List[Dict[str, Any]]:
    def inner_select(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [{k: v for k, v in d.items() if k in args} for d in data]
    return inner_select

def field_filter(field: str, *values: Any) -> List[Dict[str, Any]]:
    def inner_filter(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [d for d in data if d.get(field) in values]
    return inner_filter

def query(data: List[Dict[str, Any]], *filters) -> List[Dict[str, Any]]:
    for f in filters:
        data = f(data)
    return data

# example usage
friends = [
    {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'},
    {'name': 'Emily', 'gender': 'female', 'sport': 'volleyball'},
]

result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', *('Basketball', 'volleyball')),
    field_filter('gender', *('male',)),
)
print(result)