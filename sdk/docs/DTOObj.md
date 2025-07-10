# DTOObj

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'object']
**is_nullable** | **bool** |  | [optional] 
**fields** | [**Dict[str, Fields]**](Fields.md) |  | 
## Example

```python
from finbourne_candela.models.dto_obj import DTOObj
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
fields: Optional[Any] = # Replace with your value
dto_obj_instance = DTOObj(type=type, is_nullable=is_nullable, fields=fields)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

