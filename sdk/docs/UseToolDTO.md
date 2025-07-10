# UseToolDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'use-tool']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**intent_id** | **str** |  | 
**tool_obj** | [**ToolObj**](ToolObj.md) |  | 
## Example

```python
from finbourne_candela.models.use_tool_dto import UseToolDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
child_id: StrictStr = "example_child_id"
intent_id: StrictStr = "example_intent_id"
tool_obj: ToolObj = # Replace with your value
use_tool_dto_instance = UseToolDTO(type=type, node_id=node_id, child_id=child_id, intent_id=intent_id, tool_obj=tool_obj)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

