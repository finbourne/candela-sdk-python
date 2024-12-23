# NoOp

Class representing a no-op op state. This is used to represent cases in switching logic and joining branching states back together.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | [optional] [default to False]
**child_id** | **str** |  | [optional] 
**label** | **str** |  | 

## Example

```python
from finbourne_candela.models.no_op import NoOp

# TODO update the JSON string below
json = "{}"
# create an instance of NoOp from a JSON string
no_op_instance = NoOp.from_json(json)
# print the JSON string representation of the object
print NoOp.to_json()

# convert the object into a dict
no_op_dict = no_op_instance.to_dict()
# create an instance of NoOp from a dict
no_op_form_dict = no_op.from_dict(no_op_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


