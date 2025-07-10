# Trace

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_ids** | **List[str]** |  | 
**trace_items** | [**List[TraceItem]**](TraceItem.md) |  | 
## Example

```python
from finbourne_candela.models.trace import Trace
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

session_ids: conlist(StrictStr) = # Replace with your value
trace_items: conlist(TraceItem) = # Replace with your value
trace_instance = Trace(session_ids=session_ids, trace_items=trace_items)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

