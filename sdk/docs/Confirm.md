# Confirm

Class representing a user confirmation state.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | [optional] [default to False]
**child_id** | **str** |  | [optional] 
**instruction** | **str** |  | [optional] 
**options** | **List[str]** |  | 

## Example

```python
from finbourne_candela.models.confirm import Confirm

# TODO update the JSON string below
json = "{}"
# create an instance of Confirm from a JSON string
confirm_instance = Confirm.from_json(json)
# print the JSON string representation of the object
print Confirm.to_json()

# convert the object into a dict
confirm_dict = confirm_instance.to_dict()
# create an instance of Confirm from a dict
confirm_form_dict = confirm.from_dict(confirm_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


