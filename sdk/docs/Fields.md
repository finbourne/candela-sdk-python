# Fields


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
**value** | **str** |  | 

## Example

```python
from finbourne_candela.models.fields import Fields

# TODO update the JSON string below
json = "{}"
# create an instance of Fields from a JSON string
fields_instance = Fields.from_json(json)
# print the JSON string representation of the object
print Fields.to_json()

# convert the object into a dict
fields_dict = fields_instance.to_dict()
# create an instance of Fields from a dict
fields_form_dict = fields.from_dict(fields_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


