# ResponseDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'response']
**node_id** | **str** |  | 
**child_id** | **str** |  | 
**as_block** | **bool** |  | 
**template** | **str** |  | 
**context** | **str** |  | 
**inserts** | **Dict[str, str]** |  | 
## Example

```python
from finbourne_candela.models.response_dto import ResponseDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
child_id: StrictStr = "example_child_id"
as_block: StrictBool = # Replace with your value
as_block:StrictBool = True
template: StrictStr = "example_template"
context: StrictStr = "example_context"
inserts: Optional[Any] = # Replace with your value
response_dto_instance = ResponseDTO(type=type, node_id=node_id, child_id=child_id, as_block=as_block, template=template, context=context, inserts=inserts)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

