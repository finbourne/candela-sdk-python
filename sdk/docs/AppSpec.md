# AppSpec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**circuit** | [**ObjectId**](ObjectId.md) |  | 
**directive** | [**ObjectId**](ObjectId.md) |  | 

## Example

```python
from finbourne_candela.models.app_spec import AppSpec

# TODO update the JSON string below
json = "{}"
# create an instance of AppSpec from a JSON string
app_spec_instance = AppSpec.from_json(json)
# print the JSON string representation of the object
print AppSpec.to_json()

# convert the object into a dict
app_spec_dict = app_spec_instance.to_dict()
# create an instance of AppSpec from a dict
app_spec_form_dict = app_spec.from_dict(app_spec_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


