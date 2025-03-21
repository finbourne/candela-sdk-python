# InsertContext

A class representing a state that adds some fixed sys context.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | [optional] [default to False]
**child_id** | **str** |  | [optional] 
**label** | **str** |  | 
**context** | **str** |  | 

## Example

```python
from finbourne_candela.models.insert_context import InsertContext

# TODO update the JSON string below
json = "{}"
# create an instance of InsertContext from a JSON string
insert_context_instance = InsertContext.from_json(json)
# print the JSON string representation of the object
print InsertContext.to_json()

# convert the object into a dict
insert_context_dict = insert_context_instance.to_dict()
# create an instance of InsertContext from a dict
insert_context_form_dict = insert_context.from_dict(insert_context_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


