# InsertContextDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'insert']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**label** | **str** |  | 
**context** | **str** |  | 
## Example

```python
from finbourne_candela.models.insert_context_dto import InsertContextDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
child_id: StrictStr = "example_child_id"
label: StrictStr = "example_label"
context: StrictStr = "example_context"
insert_context_dto_instance = InsertContextDTO(type=type, node_id=node_id, child_id=child_id, label=label, context=context)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

