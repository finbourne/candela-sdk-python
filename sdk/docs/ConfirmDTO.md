# ConfirmDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'confirm']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**instruction** | **str** |  | [optional] 
**options** | **List[str]** |  | 

## Example

```python
from finbourne_candela.models.confirm_dto import ConfirmDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmDTO from a JSON string
confirm_dto_instance = ConfirmDTO.from_json(json)
# print the JSON string representation of the object
print ConfirmDTO.to_json()

# convert the object into a dict
confirm_dto_dict = confirm_dto_instance.to_dict()
# create an instance of ConfirmDTO from a dict
confirm_dto_form_dict = confirm_dto.from_dict(confirm_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


