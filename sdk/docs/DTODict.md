# DTODict

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dictionary']
**is_nullable** | **bool** |  | [optional] 
**obj** | [**Obj**](Obj.md) |  | 
**keys** | [**Keys**](Keys.md) |  | 
## Example

```python
from finbourne_candela.models.dto_dict import DTODict
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
obj: Obj = # Replace with your value
keys: Keys = # Replace with your value
dto_dict_instance = DTODict(type=type, is_nullable=is_nullable, obj=obj, keys=keys)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

