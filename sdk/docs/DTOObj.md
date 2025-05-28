# DTOObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'object']
**is_nullable** | **bool** |  | [optional] 
**fields** | [**Dict[str, Fields]**](Fields.md) |  | 

## Example

```python
from finbourne_candela.models.dto_obj import DTOObj

# TODO update the JSON string below
json = "{}"
# create an instance of DTOObj from a JSON string
dto_obj_instance = DTOObj.from_json(json)
# print the JSON string representation of the object
print DTOObj.to_json()

# convert the object into a dict
dto_obj_dict = dto_obj_instance.to_dict()
# create an instance of DTOObj from a dict
dto_obj_form_dict = dto_obj.from_dict(dto_obj_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


