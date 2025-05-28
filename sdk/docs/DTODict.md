# DTODict


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dictionary']
**is_nullable** | **bool** |  | [optional] 
**obj** | [**Obj**](Obj.md) |  | 
**keys** | [**Keys**](Keys.md) |  | 

## Example

```python
from finbourne_candela.models.dto_dict import DTODict

# TODO update the JSON string below
json = "{}"
# create an instance of DTODict from a JSON string
dto_dict_instance = DTODict.from_json(json)
# print the JSON string representation of the object
print DTODict.to_json()

# convert the object into a dict
dto_dict_dict = dto_dict_instance.to_dict()
# create an instance of DTODict from a dict
dto_dict_form_dict = dto_dict.from_dict(dto_dict_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


