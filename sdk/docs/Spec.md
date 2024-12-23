# Spec


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**fields** | [**Dict[str, Fields]**](Fields.md) |  | 
**min_len** | **object** |  | 
**max_len** | [**MaxLen**](MaxLen.md) |  | 
**obj** | [**Obj**](Obj.md) |  | 

## Example

```python
from finbourne_candela.models.spec import Spec

# TODO update the JSON string below
json = "{}"
# create an instance of Spec from a JSON string
spec_instance = Spec.from_json(json)
# print the JSON string representation of the object
print Spec.to_json()

# convert the object into a dict
spec_dict = spec_instance.to_dict()
# create an instance of Spec from a dict
spec_form_dict = spec.from_dict(spec_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


