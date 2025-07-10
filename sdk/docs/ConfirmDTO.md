# ConfirmDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'confirm']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**instruction** | **str** |  | [optional] 
**options** | **List[str]** |  | 
## Example

```python
from finbourne_candela.models.confirm_dto import ConfirmDTO
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
child_id: StrictStr = "example_child_id"
instruction: Optional[StrictStr] = "example_instruction"
options: conlist(StrictStr) = # Replace with your value
confirm_dto_instance = ConfirmDTO(type=type, node_id=node_id, child_id=child_id, instruction=instruction, options=options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

