# SlotData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot_id** | **str** |  | 
**slot_type** | **str** |  | 
**domain** | **str** |  | 
**state** | [**SlotState**](SlotState.md) |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**assigned** | **datetime** |  | [optional] 
**disposed** | **datetime** |  | [optional] 
**ready** | **datetime** |  | [optional] 

## Example

```python
from finbourne_candela.models.slot_data import SlotData

# TODO update the JSON string below
json = "{}"
# create an instance of SlotData from a JSON string
slot_data_instance = SlotData.from_json(json)
# print the JSON string representation of the object
print SlotData.to_json()

# convert the object into a dict
slot_data_dict = slot_data_instance.to_dict()
# create an instance of SlotData from a dict
slot_data_form_dict = slot_data.from_dict(slot_data_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


