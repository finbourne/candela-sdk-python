# DTOInt


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'int']
**is_nullable** | **bool** |  | [optional] 
**values** | **List[int]** |  | [optional] 
**allow_negative** | **bool** |  | [optional] 

## Example

```python
from finbourne_candela.models.dto_int import DTOInt

# TODO update the JSON string below
json = "{}"
# create an instance of DTOInt from a JSON string
dto_int_instance = DTOInt.from_json(json)
# print the JSON string representation of the object
print DTOInt.to_json()

# convert the object into a dict
dto_int_dict = dto_int_instance.to_dict()
# create an instance of DTOInt from a dict
dto_int_form_dict = dto_int.from_dict(dto_int_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


