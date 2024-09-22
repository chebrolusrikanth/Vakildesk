from typing import List, Dict, Callable

def aggregate_data(data: List[Dict], key: str, aggregator: Callable) -> Dict:
    result = {}
    for item in data:
        group_key = item.get(key)
        
        if group_key not in result:
            result[group_key] = []

        result[group_key].append(item)

    aggregated_result = {}
    for group_key, items in result.items():

        aggregated_result[group_key] = aggregator(item for item in items)

    return aggregated_result

def sum_aggregator(items):
    return sum(item['value'] for item in items)


data = [
    {'category': 'A', 'value': 10},
    {'category': 'B', 'value': 20},
    {'category': 'A', 'value': 30},
    {'category': 'B', 'value': 40},
]

aggregated_data_result = aggregate_data(data, 'category', sum_aggregator)
print(aggregated_data_result)
