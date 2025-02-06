# DevSessionStartRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | [**ObjectId**](ObjectId.md) |  | 
**circuit** | [**Circuit**](Circuit.md) |  | 
**directive** | [**Directive**](Directive.md) |  | 
**scope** | **str** |  | [optional] 
**parent_session** | [**ObjectId**](ObjectId.md) |  | [optional] 
**tool_module_override** | [**ToolModule**](ToolModule.md) |  | [optional] 

## Example

```python
from finbourne_candela.models.dev_session_start_request import DevSessionStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DevSessionStartRequest from a JSON string
dev_session_start_request_instance = DevSessionStartRequest.from_json(json)
# print the JSON string representation of the object
print DevSessionStartRequest.to_json()

# convert the object into a dict
dev_session_start_request_dict = dev_session_start_request_instance.to_dict()
# create an instance of DevSessionStartRequest from a dict
dev_session_start_request_form_dict = dev_session_start_request.from_dict(dev_session_start_request_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


