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
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictInt

old_value: StrictInt = # Replace with your value
old_value: StrictInt = 42
new_value: StrictInt = # Replace with your value
new_value: StrictInt = 42
slots_put_response_instance = SlotsPutResponse(old_value=old_value, new_value=new_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

