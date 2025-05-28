# DTOArr


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'array']
**is_nullable** | **bool** |  | [optional] 
**min_len** | **int** |  | 
**max_len** | **int** |  | 
**obj** | [**Obj**](Obj.md) |  | 

## Example

```python
from finbourne_candela.models.dto_arr import DTOArr

# TODO update the JSON string below
json = "{}"
# create an instance of DTOArr from a JSON string
dto_arr_instance = DTOArr.from_json(json)
# print the JSON string representation of the object
print DTOArr.to_json()

# convert the object into a dict
dto_arr_dict = dto_arr_instance.to_dict()
# create an instance of DTOArr from a dict
dto_arr_form_dict = dto_arr.from_dict(dto_arr_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


