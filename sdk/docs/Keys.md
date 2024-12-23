# Keys


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**max_tokens** | **object** |  | 
**regex** | [**Regex**](Regex.md) |  | 
**stop** | [**Stop**](Stop.md) |  | 
**options** | **object** |  | 

## Example

```python
from finbourne_candela.models.keys import Keys

# TODO update the JSON string below
json = "{}"
# create an instance of Keys from a JSON string
keys_instance = Keys.from_json(json)
# print the JSON string representation of the object
print Keys.to_json()

# convert the object into a dict
keys_dict = keys_instance.to_dict()
# create an instance of Keys from a dict
keys_form_dict = keys.from_dict(keys_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


