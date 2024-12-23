# SessionStartRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ObjectId**](ObjectId.md) |  | 
**model_cfg** | [**ObjectId**](ObjectId.md) |  | 
**scope** | **str** |  | [optional] 
**parent_session** | [**ObjectId**](ObjectId.md) |  | [optional] 
**circuit_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
**directive_override** | [**ObjectId**](ObjectId.md) |  | [optional] 

## Example

```python
from finbourne_candela.models.session_start_request import SessionStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionStartRequest from a JSON string
session_start_request_instance = SessionStartRequest.from_json(json)
# print the JSON string representation of the object
print SessionStartRequest.to_json()

# convert the object into a dict
session_start_request_dict = session_start_request_instance.to_dict()
# create an instance of SessionStartRequest from a dict
session_start_request_form_dict = session_start_request.from_dict(session_start_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


