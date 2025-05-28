# SwitchDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'switch']
**node_id** | **str** |  | 
**case_spec** | **Dict[str, str]** |  | 
**case_objs** | [**Dict[str, NoOpDTO]**](NoOpDTO.md) |  | 

## Example

```python
from finbourne_candela.models.switch_dto import SwitchDTO

# TODO update the JSON string below
json = "{}"
# create an instance of SwitchDTO from a JSON string
switch_dto_instance = SwitchDTO.from_json(json)
# print the JSON string representation of the object
print SwitchDTO.to_json()

# convert the object into a dict
switch_dto_dict = switch_dto_instance.to_dict()
# create an instance of SwitchDTO from a dict
switch_dto_form_dict = switch_dto.from_dict(switch_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


