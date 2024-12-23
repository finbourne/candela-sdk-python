# IObj

Class representing a structured object with fixed fields.      

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**fields** | [**Dict[str, Fields]**](Fields.md) |  | 

## Example

```python
from finbourne_candela.models.i_obj import IObj

# TODO update the JSON string below
json = "{}"
# create an instance of IObj from a JSON string
i_obj_instance = IObj.from_json(json)
# print the JSON string representation of the object
print IObj.to_json()

# convert the object into a dict
i_obj_dict = i_obj_instance.to_dict()
# create an instance of IObj from a dict
i_obj_form_dict = i_obj.from_dict(i_obj_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


