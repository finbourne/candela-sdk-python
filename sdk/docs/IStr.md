# IStr

Class representing a string-valued field in an intent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**max_tokens** | **object** |  | 
**regex** | [**Regex**](Regex.md) |  | 
**stop** | [**Stop**](Stop.md) |  | 

## Example

```python
from finbourne_candela.models.i_str import IStr

# TODO update the JSON string below
json = "{}"
# create an instance of IStr from a JSON string
i_str_instance = IStr.from_json(json)
# print the JSON string representation of the object
print IStr.to_json()

# convert the object into a dict
i_str_dict = i_str_instance.to_dict()
# create an instance of IStr from a dict
i_str_form_dict = i_str.from_dict(i_str_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


