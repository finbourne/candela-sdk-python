# DTOConst


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'constant']
**value** | **str** |  | 
**is_nullable** | **bool** |  | [optional] 

## Example

```python
from finbourne_candela.models.dto_const import DTOConst

# TODO update the JSON string below
json = "{}"
# create an instance of DTOConst from a JSON string
dto_const_instance = DTOConst.from_json(json)
# print the JSON string representation of the object
print DTOConst.to_json()

# convert the object into a dict
dto_const_dict = dto_const_instance.to_dict()
# create an instance of DTOConst from a dict
dto_const_form_dict = dto_const.from_dict(dto_const_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


