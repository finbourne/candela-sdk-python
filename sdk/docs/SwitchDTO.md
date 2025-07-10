# SwitchDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'switch']
**node_id** | **str** |  | 
**case_spec** | **Dict[str, str]** |  | 
**case_objs** | [**Dict[str, NoOpDTO]**](NoOpDTO.md) |  | 
## Example

```python
from finbourne_candela.models.switch_dto import SwitchDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
case_spec: Optional[Any] = # Replace with your value
case_objs: Optional[Any] = # Replace with your value
switch_dto_instance = SwitchDTO(type=type, node_id=node_id, case_spec=case_spec, case_objs=case_objs)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

