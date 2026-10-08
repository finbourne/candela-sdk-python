# TraceEventDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** |  | [optional] 
**trace_event_id** | **str** |  | [optional] 
**created_at** | **datetime** | When the event occurred, from the clock of the code that observed it — not when the row was written. Ordering by this is what makes a replayed conversation match the order the user saw live. Do not equate it with the identically-named field on an insights trace log, which is stamped by the log aggregator on receipt. | [optional] 
**user_id** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**agent_code** | **str** |  | [optional] 
**agent_version** | **int** |  | [optional] 
**event_type** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.trace_event_definition import TraceEventDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trace_id: Optional[StrictStr] = "example_trace_id"
trace_event_id: Optional[StrictStr] = "example_trace_event_id"
created_at: Optional[datetime] = # Replace with your value
user_id: Optional[StrictStr] = "example_user_id"
origin: Optional[StrictStr] = "example_origin"
content: Optional[StrictStr] = "example_content"
agent_code: Optional[StrictStr] = "example_agent_code"
agent_version: Optional[StrictInt] = # Replace with your value
agent_version: Optional[StrictInt] = None
event_type: Optional[StrictStr] = "example_event_type"
trace_event_definition_instance = TraceEventDefinition(trace_id=trace_id, trace_event_id=trace_event_id, created_at=created_at, user_id=user_id, origin=origin, content=content, agent_code=agent_code, agent_version=agent_version, event_type=event_type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

