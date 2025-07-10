# ObjectMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_id** | [**ObjectId**](ObjectId.md) |  | 
**domain** | **str** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.object_metadata import ObjectMetadata
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
obj_id: ObjectId = # Replace with your value
domain: StrictStr = "example_domain"
created_by: StrictStr = "example_created_by"
created_at: datetime = # Replace with your value
description: Optional[StrictStr] = "example_description"
object_metadata_instance = ObjectMetadata(obj_id=obj_id, domain=domain, created_by=created_by, created_at=created_at, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

