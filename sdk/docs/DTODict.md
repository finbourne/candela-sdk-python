# DTODict

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'dictionary']
**is_nullable** | **bool** |  | [optional] 
**obj** | [**Obj1**](Obj1.md) |  | 
**keys** | [**Keys**](Keys.md) |  | 
**min_size** | **int** |  | [optional] 
**max_size** | **int** |  | [optional] 
**description** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_dict import DTODict
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
obj: Obj1 = # Replace with your value
keys: Keys = # Replace with your value
min_size: Optional[StrictInt] = None
min_size: Optional[StrictInt] = None
max_size: Optional[StrictInt] = None
max_size: Optional[StrictInt] = None
description: Optional[StrictStr] = "example_description"
dto_dict_instance = DTODict(type=type, is_nullable=is_nullable, obj=obj, keys=keys, min_size=min_size, max_size=max_size, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

