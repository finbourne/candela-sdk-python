# IntentDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'intent']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**spec** | [**Spec**](Spec.md) |  | 
**instruction** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.intent_dto import IntentDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
child_id: StrictStr = "example_child_id"
spec: Spec = # Replace with your value
instruction: Optional[StrictStr] = "example_instruction"
intent_dto_instance = IntentDTO(type=type, node_id=node_id, child_id=child_id, spec=spec, instruction=instruction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

