# BaseTool

Base class for tools

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_type** | **str** |  | [optional] 
**instruction** | **str** |  | [optional] 

## Example

```python
from finbourne_candela.models.base_tool import BaseTool

# TODO update the JSON string below
json = "{}"
# create an instance of BaseTool from a JSON string
base_tool_instance = BaseTool.from_json(json)
# print the JSON string representation of the object
print BaseTool.to_json()

# convert the object into a dict
base_tool_dict = base_tool_instance.to_dict()
# create an instance of BaseTool from a dict
base_tool_form_dict = base_tool.from_dict(base_tool_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


