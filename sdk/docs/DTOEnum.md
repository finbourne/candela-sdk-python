# DTOEnum


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'enum']
**is_nullable** | **bool** |  | [optional] 
**options** | **List[str]** |  | 

## Example

```python
from finbourne_candela.models.dto_enum import DTOEnum

# TODO update the JSON string below
json = "{}"
# create an instance of DTOEnum from a JSON string
dto_enum_instance = DTOEnum.from_json(json)
# print the JSON string representation of the object
print DTOEnum.to_json()

# convert the object into a dict
dto_enum_dict = dto_enum_instance.to_dict()
# create an instance of DTOEnum from a dict
dto_enum_form_dict = dto_enum.from_dict(dto_enum_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


