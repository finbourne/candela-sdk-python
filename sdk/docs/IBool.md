# IBool

Class representing a boolean-valued field in an intent.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 

## Example

```python
from finbourne_candela.models.i_bool import IBool

# TODO update the JSON string below
json = "{}"
# create an instance of IBool from a JSON string
i_bool_instance = IBool.from_json(json)
# print the JSON string representation of the object
print IBool.to_json()

# convert the object into a dict
i_bool_dict = i_bool_instance.to_dict()
# create an instance of IBool from a dict
i_bool_form_dict = i_bool.from_dict(i_bool_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


