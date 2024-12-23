# ObjectId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**identifier** | **str** |  | 
**version** | **str** |  | [optional] 

## Example

```python
from finbourne_candela.models.object_id import ObjectId

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectId from a JSON string
object_id_instance = ObjectId.from_json(json)
# print the JSON string representation of the object
print ObjectId.to_json()

# convert the object into a dict
object_id_dict = object_id_instance.to_dict()
# create an instance of ObjectId from a dict
object_id_form_dict = object_id.from_dict(object_id_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


