# DevSessionStartRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_id** | [**ObjectId**](ObjectId.md) |  | 
**circuit** | [**CircuitDTO**](CircuitDTO.md) |  | 
**directive** | [**Directive**](Directive.md) |  | 
**scope** | **str** |  | [optional] 
**parent_session** | [**ObjectId**](ObjectId.md) |  | [optional] 
**tool_module_override** | [**ToolModule**](ToolModule.md) |  | [optional] 
## Example

```python
from finbourne_candela.models.dev_session_start_request import DevSessionStartRequest
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

model_id: ObjectId = # Replace with your value
circuit: CircuitDTO = # Replace with your value
directive: Directive = # Replace with your value
scope: Optional[StrictStr] = "example_scope"
parent_session: Optional[ObjectId] = None
tool_module_override: Optional[ToolModule] = None
dev_session_start_request_instance = DevSessionStartRequest(model_id=model_id, circuit=circuit, directive=directive, scope=scope, parent_session=parent_session, tool_module_override=tool_module_override)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

