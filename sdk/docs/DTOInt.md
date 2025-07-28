# DTOInt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'int']
**values** | **List[int]** |  | [optional] 
**is_nullable** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**default_value** | **int** |  | [optional] 
**min_value** | **int** |  | [optional] 
**max_value** | **int** |  | [optional] 
**lower_bound** | **str** |  | [optional] 
**upper_bound** | **str** |  | [optional] 
**allow_negative** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_int import DTOInt
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, StrictBool, StrictInt, StrictStr, conlist, validator

type: Optional[StrictStr] = "example_type"
values: Optional[conlist(StrictInt)] = None
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
default_value: Optional[StrictInt] = None
default_value: Optional[StrictInt] = None
min_value: Optional[StrictInt] = None
min_value: Optional[StrictInt] = None
max_value: Optional[StrictInt] = None
max_value: Optional[StrictInt] = None
lower_bound: Optional[StrictStr] = "example_lower_bound"
upper_bound: Optional[StrictStr] = "example_upper_bound"
allow_negative: Optional[StrictBool] = None
allow_negative:Optional[StrictBool] = None
dto_int_instance = DTOInt(type=type, values=values, is_nullable=is_nullable, description=description, default_value=default_value, min_value=min_value, max_value=max_value, lower_bound=lower_bound, upper_bound=upper_bound, allow_negative=allow_negative)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

