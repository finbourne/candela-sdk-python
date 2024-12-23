# IEnum

Class representing an enum-valued field in an intent. This is a value that can take on one of a discrete set of string values.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**options** | **object** |  | 

## Example

```python
from finbourne_candela.models.i_enum import IEnum

# TODO update the JSON string below
json = "{}"
# create an instance of IEnum from a JSON string
i_enum_instance = IEnum.from_json(json)
# print the JSON string representation of the object
print IEnum.to_json()

# convert the object into a dict
i_enum_dict = i_enum_instance.to_dict()
# create an instance of IEnum from a dict
i_enum_form_dict = i_enum.from_dict(i_enum_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


