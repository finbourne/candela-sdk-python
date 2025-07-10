# Session

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**ObjectId**](ObjectId.md) |  | 
**model_cfg** | [**ObjectId**](ObjectId.md) |  | 
**host_id** | **str** |  | 
**parent_session** | [**ObjectId**](ObjectId.md) |  | [optional] 
**circuit_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
**directive_override** | [**ObjectId**](ObjectId.md) |  | [optional] 
**dev_session** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.session import Session
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

app: Optional[ObjectId] = # Replace with your value
model_cfg: ObjectId = # Replace with your value
host_id: StrictStr = "example_host_id"
parent_session: Optional[ObjectId] = None
circuit_override: Optional[ObjectId] = None
directive_override: Optional[ObjectId] = None
dev_session: Optional[StrictBool] = None
dev_session:Optional[StrictBool] = None
session_instance = Session(app=app, model_cfg=model_cfg, host_id=host_id, parent_session=parent_session, circuit_override=circuit_override, directive_override=directive_override, dev_session=dev_session)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

