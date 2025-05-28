# DTOReal


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'real']
**is_nullable** | **bool** |  | [optional] 
**allow_negative** | **bool** |  | [optional] 

## Example

```python
from finbourne_candela.models.dto_real import DTOReal

# TODO update the JSON string below
json = "{}"
# create an instance of DTOReal from a JSON string
dto_real_instance = DTOReal.from_json(json)
# print the JSON string representation of the object
print DTOReal.to_json()

# convert the object into a dict
dto_real_dict = dto_real_instance.to_dict()
# create an instance of DTOReal from a dict
dto_real_form_dict = dto_real.from_dict(dto_real_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


