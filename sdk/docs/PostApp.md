# PostApp

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**identifier** | **str** |  | 
**description** | **str** |  | [optional] 
**version_bump** | **str** |  | [optional] [default to 'patch']
**data** | [**AppSpec**](AppSpec.md) |  | 
## Example

```python
from finbourne_candela.models.post_app import PostApp
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, validator

scope: StrictStr = "example_scope"
identifier: StrictStr = "example_identifier"
description: Optional[StrictStr] = "example_description"
version_bump: Optional[StrictStr] = "example_version_bump"
data: AppSpec = # Replace with your value
post_app_instance = PostApp(scope=scope, identifier=identifier, description=description, version_bump=version_bump, data=data)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

