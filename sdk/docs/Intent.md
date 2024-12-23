# Intent

Class representing an intent state. Intent states construct a json with a defined structure that depends on prior dialogue content.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | [optional] [default to True]
**child_id** | **str** |  | [optional] 
**spec** | [**Spec**](Spec.md) |  | 
**instruction** | **str** |  | [optional] 

## Example

```python
from finbourne_candela.models.intent import Intent

# TODO update the JSON string below
json = "{}"
# create an instance of Intent from a JSON string
intent_instance = Intent.from_json(json)
# print the JSON string representation of the object
print Intent.to_json()

# convert the object into a dict
intent_dict = intent_instance.to_dict()
# create an instance of Intent from a dict
intent_form_dict = intent.from_dict(intent_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


