# ToolModuleMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_id** | [**ObjectId**](ObjectId.md) |  | 
**domain** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | [optional] 
**tools** | **List[str]** |  | 

## Example

```python
from finbourne_candela.models.tool_module_metadata import ToolModuleMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ToolModuleMetadata from a JSON string
tool_module_metadata_instance = ToolModuleMetadata.from_json(json)
# print the JSON string representation of the object
print ToolModuleMetadata.to_json()

# convert the object into a dict
tool_module_metadata_dict = tool_module_metadata_instance.to_dict()
# create an instance of ToolModuleMetadata from a dict
tool_module_metadata_form_dict = tool_module_metadata.from_dict(tool_module_metadata_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


