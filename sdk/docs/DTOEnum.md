# DTOEnum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'enum']
**is_nullable** | **bool** |  | [optional] 
**options** | **List[str]** |  | 
## Example

```python
from finbourne_candela.models.dto_enum import DTOEnum
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
options: conlist(StrictStr) = # Replace with your value
dto_enum_instance = DTOEnum(type=type, is_nullable=is_nullable, options=options)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

