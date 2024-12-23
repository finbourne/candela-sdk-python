# UseTool

Class representing a tool use state. Tools are bit of code that take intents and perform an action. This lets circuits call out to external systems or local software.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | [optional] [default to False]
**child_id** | **str** |  | [optional] 
**intent_id** | **str** |  | 
**tool_obj** | [**ToolObj**](ToolObj.md) |  | 

## Example

```python
from finbourne_candela.models.use_tool import UseTool

# TODO update the JSON string below
json = "{}"
# create an instance of UseTool from a JSON string
use_tool_instance = UseTool.from_json(json)
# print the JSON string representation of the object
print UseTool.to_json()

# convert the object into a dict
use_tool_dict = use_tool_instance.to_dict()
# create an instance of UseTool from a dict
use_tool_form_dict = use_tool.from_dict(use_tool_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


