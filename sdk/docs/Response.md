# Response

Class representing a response state in a circuit. Response states are normal chat responses that can optionally be constrained to a particular form with a guidance template.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **str** |  | [optional] 
**node_type** | **str** |  | [optional] 
**as_block** | **bool** |  | 
**child_id** | **str** |  | [optional] 
**template** | **str** |  | 
**context** | **str** |  | 
**inserts** | **Dict[str, str]** |  | 

## Example

```python
from finbourne_candela.models.response import Response

# TODO update the JSON string below
json = "{}"
# create an instance of Response from a JSON string
response_instance = Response.from_json(json)
# print the JSON string representation of the object
print Response.to_json()

# convert the object into a dict
response_dict = response_instance.to_dict()
# create an instance of Response from a dict
response_form_dict = response.from_dict(response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


