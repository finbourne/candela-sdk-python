# ObjectId

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** |  | 
**identifier** | **str** |  | 
**version** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.object_id import ObjectId
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

scope: StrictStr = "example_scope"
identifier: StrictStr = "example_identifier"
version: Optional[StrictStr] = "example_version"
object_id_instance = ObjectId(scope=scope, identifier=identifier, version=version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

