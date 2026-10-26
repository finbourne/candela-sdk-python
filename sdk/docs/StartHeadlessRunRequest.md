# StartHeadlessRunRequest

A run for a Drive file (fileId, filePath and fileName together), or for a Workflow task (taskId alone).
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | **str** |  | 
**file_id** | **str** |  | [optional] 
**file_path** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**task_id** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.start_headless_run_request import StartHeadlessRunRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

agent: StrictStr = "example_agent"
file_id: Optional[StrictStr] = "example_file_id"
file_path: Optional[StrictStr] = "example_file_path"
file_name: Optional[StrictStr] = "example_file_name"
task_id: Optional[StrictStr] = "example_task_id"
start_headless_run_request_instance = StartHeadlessRunRequest(agent=agent, file_id=file_id, file_path=file_path, file_name=file_name, task_id=task_id)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

