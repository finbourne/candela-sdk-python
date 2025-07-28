# DTOEnum

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'enum']
**options** | **List[str]** |  | 
**is_nullable** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_enum import DTOEnum
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, validator

type: Optional[StrictStr] = "example_type"
options: conlist(StrictStr) = # Replace with your value
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
default_value: Optional[StrictStr] = "example_default_value"
dto_enum_instance = DTOEnum(type=type, options=options, is_nullable=is_nullable, description=description, default_value=default_value)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

