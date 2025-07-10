# ToolModuleMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_id** | [**ObjectId**](ObjectId.md) |  | 
**domain** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | [optional] 
**tools** | **List[str]** |  | 
## Example

```python
from finbourne_candela.models.tool_module_metadata import ToolModuleMetadata
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist
from datetime import datetime
obj_id: ObjectId = # Replace with your value
domain: StrictStr = "example_domain"
created_by: StrictStr = "example_created_by"
created_at: datetime = # Replace with your value
description: Optional[StrictStr] = "example_description"
tools: conlist(StrictStr) = # Replace with your value
tool_module_metadata_instance = ToolModuleMetadata(obj_id=obj_id, domain=domain, created_by=created_by, created_at=created_at, description=description, tools=tools)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

