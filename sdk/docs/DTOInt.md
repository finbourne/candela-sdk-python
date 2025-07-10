# DTOInt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'int']
**is_nullable** | **bool** |  | [optional] 
**values** | **List[int]** |  | [optional] 
**allow_negative** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_int import DTOInt
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, StrictBool, StrictInt, StrictStr, conlist, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
values: Optional[conlist(StrictInt)] = None
allow_negative: Optional[StrictBool] = None
allow_negative:Optional[StrictBool] = None
dto_int_instance = DTOInt(type=type, is_nullable=is_nullable, values=values, allow_negative=allow_negative)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

