# NoOpDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'no-op']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**label** | **str** |  | 

## Example

```python
from finbourne_candela.models.no_op_dto import NoOpDTO

# TODO update the JSON string below
json = "{}"
# create an instance of NoOpDTO from a JSON string
no_op_dto_instance = NoOpDTO.from_json(json)
# print the JSON string representation of the object
print NoOpDTO.to_json()

# convert the object into a dict
no_op_dto_dict = no_op_dto_instance.to_dict()
# create an instance of NoOpDTO from a dict
no_op_dto_form_dict = no_op_dto.from_dict(no_op_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


