# DTOBool


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'bool']
**is_nullable** | **bool** |  | [optional] 

## Example

```python
from finbourne_candela.models.dto_bool import DTOBool

# TODO update the JSON string below
json = "{}"
# create an instance of DTOBool from a JSON string
dto_bool_instance = DTOBool.from_json(json)
# print the JSON string representation of the object
print DTOBool.to_json()

# convert the object into a dict
dto_bool_dict = dto_bool_instance.to_dict()
# create an instance of DTOBool from a dict
dto_bool_form_dict = dto_bool.from_dict(dto_bool_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


