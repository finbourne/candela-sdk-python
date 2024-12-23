# Session


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ObjectId**](ObjectId.md) |  | 
**model_cfg** | [**ObjectId**](ObjectId.md) |  | 
**host_id** | **str** |  | 
**parent_session** | [**ObjectId**](ObjectId.md) |  | [optional] 
**circuit_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
**directive_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
**dev_session** | **bool** |  | [optional] 

## Example

```python
from finbourne_candela.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print Session.to_json()

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_form_dict = session.from_dict(session_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


