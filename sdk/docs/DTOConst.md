# DTOConst

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'constant']
**value** | **str** |  | 
**is_nullable** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_const import DTOConst
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
value: StrictStr = "example_value"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
dto_const_instance = DTOConst(type=type, value=value, is_nullable=is_nullable)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

