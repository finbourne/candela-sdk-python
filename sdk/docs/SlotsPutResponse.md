# SlotsPutResponse

Response model for a put response where the response sends previous value along with updated value

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**old_value** | **int** |  | 
**new_value** | **int** |  | 

## Example

```python
from finbourne_candela.models.slots_put_response import SlotsPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SlotsPutResponse from a JSON string
slots_put_response_instance = SlotsPutResponse.from_json(json)
# print the JSON string representation of the object
print SlotsPutResponse.to_json()

# convert the object into a dict
slots_put_response_dict = slots_put_response_instance.to_dict()
# create an instance of SlotsPutResponse from a dict
slots_put_response_form_dict = slots_put_response.from_dict(slots_put_response_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


