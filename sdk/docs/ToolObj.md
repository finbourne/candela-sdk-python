# ToolObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_type** | **str** |  | [optional] 
**instruction** | **str** |  | [optional] 

## Example

```python
from finbourne_candela.models.tool_obj import ToolObj

# TODO update the JSON string below
json = "{}"
# create an instance of ToolObj from a JSON string
tool_obj_instance = ToolObj.from_json(json)
# print the JSON string representation of the object
print ToolObj.to_json()

# convert the object into a dict
tool_obj_dict = tool_obj_instance.to_dict()
# create an instance of ToolObj from a dict
tool_obj_form_dict = tool_obj.from_dict(tool_obj_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


