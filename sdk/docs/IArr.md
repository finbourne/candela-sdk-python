# IArr

Class representing a variable length array intent field with a defined element type.      

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**min_len** | **object** |  | 
**max_len** | [**MaxLen**](MaxLen.md) |  | 
**obj** | [**Obj**](Obj.md) |  | 

## Example

```python
from finbourne_candela.models.i_arr import IArr

# TODO update the JSON string below
json = "{}"
# create an instance of IArr from a JSON string
i_arr_instance = IArr.from_json(json)
# print the JSON string representation of the object
print IArr.to_json()

# convert the object into a dict
i_arr_dict = i_arr_instance.to_dict()
# create an instance of IArr from a dict
i_arr_form_dict = i_arr.from_dict(i_arr_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


