# DTOBool

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'bool']
**is_nullable** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_bool import DTOBool
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
dto_bool_instance = DTOBool(type=type, is_nullable=is_nullable)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

