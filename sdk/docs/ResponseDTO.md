# ResponseDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'response']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**as_block** | **bool** |  | 
**template** | **str** |  | 
**context** | **str** |  | 
**inserts** | **Dict[str, str]** |  | 

## Example

```python
from finbourne_candela.models.response_dto import ResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseDTO from a JSON string
response_dto_instance = ResponseDTO.from_json(json)
# print the JSON string representation of the object
print ResponseDTO.to_json()

# convert the object into a dict
response_dto_dict = response_dto_instance.to_dict()
# create an instance of ResponseDTO from a dict
response_dto_form_dict = response_dto.from_dict(response_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


