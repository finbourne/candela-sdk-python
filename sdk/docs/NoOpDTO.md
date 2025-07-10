# NoOpDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'no-op']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**label** | **str** |  | 
## Example

```python
from finbourne_candela.models.no_op_dto import NoOpDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
child_id: StrictStr = "example_child_id"
label: StrictStr = "example_label"
no_op_dto_instance = NoOpDTO(type=type, node_id=node_id, child_id=child_id, label=label)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

