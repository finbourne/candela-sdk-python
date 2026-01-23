# TraceDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**user_id** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.trace_definition import TraceDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trace_id: Optional[StrictStr] = "example_trace_id"
description: Optional[StrictStr] = "example_description"
created_at: Optional[datetime] = # Replace with your value
user_id: Optional[StrictStr] = "example_user_id"
trace_definition_instance = TraceDefinition(trace_id=trace_id, description=description, created_at=created_at, user_id=user_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

