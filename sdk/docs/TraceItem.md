# TraceItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | 
**content** | **str** |  | 

## Example

```python
from finbourne_candela.models.trace_item import TraceItem

# TODO update the JSON string below
json = "{}"
# create an instance of TraceItem from a JSON string
trace_item_instance = TraceItem.from_json(json)
# print the JSON string representation of the object
print TraceItem.to_json()

# convert the object into a dict
trace_item_dict = trace_item_instance.to_dict()
# create an instance of TraceItem from a dict
trace_item_form_dict = trace_item.from_dict(trace_item_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


