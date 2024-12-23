# Obj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_nullable** | **object** |  | [optional] 
**obj** | [**Obj**](Obj.md) |  | 
**keys** | [**Keys**](Keys.md) |  | 
**min_len** | **object** |  | 
**max_len** | [**MaxLen**](MaxLen.md) |  | 
**fields** | [**Dict[str, Fields]**](Fields.md) |  | 
**options** | **object** |  | 
**max_tokens** | **object** |  | 
**regex** | [**Regex**](Regex.md) |  | 
**stop** | [**Stop**](Stop.md) |  | 
**allow_negative** | **object** |  | 
**values** | **object** |  | 

## Example

```python
from finbourne_candela.models.obj import Obj

# TODO update the JSON string below
json = "{}"
# create an instance of Obj from a JSON string
obj_instance = Obj.from_json(json)
# print the JSON string representation of the object
print Obj.to_json()

# convert the object into a dict
obj_dict = obj_instance.to_dict()
# create an instance of Obj from a dict
obj_form_dict = obj.from_dict(obj_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


