# DTOReal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'real']
**is_nullable** | **bool** |  | [optional] 
**allow_negative** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_real import DTOReal
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
allow_negative: Optional[StrictBool] = None
allow_negative:Optional[StrictBool] = None
dto_real_instance = DTOReal(type=type, is_nullable=is_nullable, allow_negative=allow_negative)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

