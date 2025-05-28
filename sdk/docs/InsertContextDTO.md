# InsertContextDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'insert']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**label** | **str** |  | 
**context** | **str** |  | 

## Example

```python
from finbourne_candela.models.insert_context_dto import InsertContextDTO

# TODO update the JSON string below
json = "{}"
# create an instance of InsertContextDTO from a JSON string
insert_context_dto_instance = InsertContextDTO.from_json(json)
# print the JSON string representation of the object
print InsertContextDTO.to_json()

# convert the object into a dict
insert_context_dto_dict = insert_context_dto_instance.to_dict()
# create an instance of InsertContextDTO from a dict
insert_context_dto_form_dict = insert_context_dto.from_dict(insert_context_dto_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


