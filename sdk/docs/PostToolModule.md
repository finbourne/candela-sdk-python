# PostToolModule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**identifier** | **str** |  | 
**description** | **str** |  | [optional] 
**version_bump** | **str** |  | [optional] [default to 'patch']
**data** | [**ToolModule**](ToolModule.md) |  | 

## Example

```python
from finbourne_candela.models.post_tool_module import PostToolModule

# TODO update the JSON string below
json = "{}"
# create an instance of PostToolModule from a JSON string
post_tool_module_instance = PostToolModule.from_json(json)
# print the JSON string representation of the object
print PostToolModule.to_json()

# convert the object into a dict
post_tool_module_dict = post_tool_module_instance.to_dict()
# create an instance of PostToolModule from a dict
post_tool_module_form_dict = post_tool_module.from_dict(post_tool_module_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


