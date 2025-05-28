# Obj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'array']
**is_nullable** | **bool** |  | [optional] 
**min_len** | **int** |  | 
**max_len** | **int** |  | 
**obj** | [**Obj**](Obj.md) |  | 
**fields** | [**Dict[str, Fields]**](Fields.md) |  | 
**options** | **List[str]** |  | 
**max_tokens** | **int** |  | 
**regex** | **str** |  | 
**stop** | **str** |  | 
**allow_negative** | **bool** |  | [optional] 
**values** | **List[int]** |  | [optional] 

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


