# SwitchDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'switch']
**node_id** | **str** |  | 
**case_spec** | **Dict[str, str]** |  | 
**case_objs** | [**Dict[str, NoOpDTO]**](NoOpDTO.md) |  | 
**isolate** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.switch_dto import SwitchDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
node_id: StrictStr = "example_node_id"
case_spec: Optional[Any] = # Replace with your value
case_objs: Optional[Any] = # Replace with your value
isolate: Optional[StrictBool] = None
isolate:Optional[StrictBool] = None
switch_dto_instance = SwitchDTO(type=type, node_id=node_id, case_spec=case_spec, case_objs=case_objs, isolate=isolate)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

