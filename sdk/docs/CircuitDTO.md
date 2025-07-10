# CircuitDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | 
**nodes** | [**Dict[str, Nodes]**](Nodes.md) |  | 
## Example

```python
from finbourne_candela.models.circuit_dto import CircuitDTO
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

first: StrictStr = "example_first"
nodes: Optional[Any] = # Replace with your value
circuit_dto_instance = CircuitDTO(first=first, nodes=nodes)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

