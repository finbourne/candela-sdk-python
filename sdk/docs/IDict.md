# IDict

Class representing a variable-sized dictionary with string-valued keys and items of the same defined type.      

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**obj** | [**Obj**](Obj.md) |  | 
**keys** | [**Keys**](Keys.md) |  | 

## Example

```python
from finbourne_candela.models.i_dict import IDict

# TODO update the JSON string below
json = "{}"
# create an instance of IDict from a JSON string
i_dict_instance = IDict.from_json(json)
# print the JSON string representation of the object
print IDict.to_json()

# convert the object into a dict
i_dict_dict = i_dict_instance.to_dict()
# create an instance of IDict from a dict
i_dict_form_dict = i_dict.from_dict(i_dict_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


