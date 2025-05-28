# UseToolDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'use-tool']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**intent_id** | **str** |  | 
**tool_obj** | [**ToolObj**](ToolObj.md) |  | 

## Example

```python
from finbourne_candela.models.use_tool_dto import UseToolDTO

# TODO update the JSON string below
json = "{}"
# create an instance of UseToolDTO from a JSON string
use_tool_dto_instance = UseToolDTO.from_json(json)
# print the JSON string representation of the object
print UseToolDTO.to_json()

# convert the object into a dict
use_tool_dto_dict = use_tool_dto_instance.to_dict()
# create an instance of UseToolDTO from a dict
use_tool_dto_form_dict = use_tool_dto.from_dict(use_tool_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


