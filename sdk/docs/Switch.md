# Switch

Class representing a switch state. Switch states allow conditional branching of states so the circuit can branch down multiple paths depending on the prior dialog state.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**case_spec** | **Dict[str, str]** |  | 
**case_objs** | [**Dict[str, NoOp]**](NoOp.md) |  | [optional] 

## Example

```python
from finbourne_candela.models.switch import Switch

# TODO update the JSON string below
json = "{}"
# create an instance of Switch from a JSON string
switch_instance = Switch.from_json(json)
# print the JSON string representation of the object
print Switch.to_json()

# convert the object into a dict
switch_dict = switch_instance.to_dict()
# create an instance of Switch from a dict
switch_form_dict = switch.from_dict(switch_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


