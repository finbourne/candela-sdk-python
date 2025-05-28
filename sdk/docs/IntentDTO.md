# IntentDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'intent']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**spec** | [**Spec**](Spec.md) |  | 
**instruction** | **str** |  | [optional] 

## Example

```python
from finbourne_candela.models.intent_dto import IntentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of IntentDTO from a JSON string
intent_dto_instance = IntentDTO.from_json(json)
# print the JSON string representation of the object
print IntentDTO.to_json()

# convert the object into a dict
intent_dto_dict = intent_dto_instance.to_dict()
# create an instance of IntentDTO from a dict
intent_dto_form_dict = intent_dto.from_dict(intent_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


