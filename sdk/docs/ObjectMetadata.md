# ObjectMetadata


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_id** | [**ObjectId**](ObjectId.md) |  | 
**domain** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from finbourne_candela.models.object_metadata import ObjectMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectMetadata from a JSON string
object_metadata_instance = ObjectMetadata.from_json(json)
# print the JSON string representation of the object
print ObjectMetadata.to_json()

# convert the object into a dict
object_metadata_dict = object_metadata_instance.to_dict()
# create an instance of ObjectMetadata from a dict
object_metadata_form_dict = object_metadata.from_dict(object_metadata_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


