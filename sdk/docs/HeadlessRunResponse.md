# HeadlessRunResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trace_id** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.headless_run_response import HeadlessRunResponse
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

trace_id: Optional[StrictStr] = "example_trace_id"
headless_run_response_instance = HeadlessRunResponse(trace_id=trace_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

