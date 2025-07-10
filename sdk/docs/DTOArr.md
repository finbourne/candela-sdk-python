# DTOArr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'array']
**is_nullable** | **bool** |  | [optional] 
**min_len** | **int** |  | 
**max_len** | **int** |  | 
**obj** | [**Obj**](Obj.md) |  | 
## Example

```python
from finbourne_candela.models.dto_arr import DTOArr
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
min_len: StrictInt = # Replace with your value
min_len: StrictInt = 42
max_len: Optional[StrictInt] = # Replace with your value
max_len: StrictInt = 42
obj: Obj = # Replace with your value
dto_arr_instance = DTOArr(type=type, is_nullable=is_nullable, min_len=min_len, max_len=max_len, obj=obj)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

