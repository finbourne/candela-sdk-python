# StartHeadlessRunRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | **str** |  | 
**file_id** | **str** |  | 
**file_path** | **str** |  | 
**file_name** | **str** |  | 
## Example

```python
from finbourne_candela.models.start_headless_run_request import StartHeadlessRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agent: StrictStr = "example_agent"
file_id: StrictStr = "example_file_id"
file_path: StrictStr = "example_file_path"
file_name: StrictStr = "example_file_name"
start_headless_run_request_instance = StartHeadlessRunRequest(agent=agent, file_id=file_id, file_path=file_path, file_name=file_name)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

