# IReal

Class representing a real (continuous number) valued field in an intent.      

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**allow_negative** | **object** |  | 

## Example

```python
from finbourne_candela.models.i_real import IReal

# TODO update the JSON string below
json = "{}"
# create an instance of IReal from a JSON string
i_real_instance = IReal.from_json(json)
# print the JSON string representation of the object
print IReal.to_json()

# convert the object into a dict
i_real_dict = i_real_instance.to_dict()
# create an instance of IReal from a dict
i_real_form_dict = i_real.from_dict(i_real_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


