# IInt

Class representing an integer-valued field in an intent.      

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**values** | **object** |  | 
**allow_negative** | **object** |  | 

## Example

```python
from finbourne_candela.models.i_int import IInt

# TODO update the JSON string below
json = "{}"
# create an instance of IInt from a JSON string
i_int_instance = IInt.from_json(json)
# print the JSON string representation of the object
print IInt.to_json()

# convert the object into a dict
i_int_dict = i_int_instance.to_dict()
# create an instance of IInt from a dict
i_int_form_dict = i_int.from_dict(i_int_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


