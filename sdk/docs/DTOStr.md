# DTOStr


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'string']
**is_nullable** | **bool** |  | [optional] 
**max_tokens** | **int** |  | 
**regex** | **str** |  | 
**stop** | **str** |  | 

## Example

```python
from finbourne_candela.models.dto_str import DTOStr

# TODO update the JSON string below
json = "{}"
# create an instance of DTOStr from a JSON string
dto_str_instance = DTOStr.from_json(json)
# print the JSON string representation of the object
print DTOStr.to_json()

# convert the object into a dict
dto_str_dict = dto_str_instance.to_dict()
# create an instance of DTOStr from a dict
dto_str_form_dict = dto_str.from_dict(dto_str_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


