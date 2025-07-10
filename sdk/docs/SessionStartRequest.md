# SessionStartRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ObjectId**](ObjectId.md) |  | 
**model_cfg** | [**ObjectId**](ObjectId.md) |  | 
**scope** | **str** |  | [optional] 
**parent_session** | [**ObjectId**](ObjectId.md) |  | [optional] 
**circuit_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
**directive_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
## Example

```python
from finbourne_candela.models.session_start_request import SessionStartRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

app: ObjectId = # Replace with your value
model_cfg: ObjectId = # Replace with your value
scope: Optional[StrictStr] = "example_scope"
parent_session: Optional[ObjectId] = None
circuit_override: Optional[ObjectId] = None
directive_override: Optional[ObjectId] = None
session_start_request_instance = SessionStartRequest(app=app, model_cfg=model_cfg, scope=scope, parent_session=parent_session, circuit_override=circuit_override, directive_override=directive_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

