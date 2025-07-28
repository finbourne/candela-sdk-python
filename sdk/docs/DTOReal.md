# DTOReal

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'real']
**is_nullable** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**default_value** | **float** |  | [optional] 
**min_value** | **float** |  | [optional] 
**max_value** | **float** |  | [optional] 
**lower_bound** | **str** |  | [optional] 
**upper_bound** | **str** |  | [optional] 
**allow_negative** | **bool** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_real import DTOReal
from typing import Any, Dict, Optional, Union
from pydantic.v1 import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
description: Optional[StrictStr] = "example_description"
default_value: Optional[Union[StrictFloat, StrictInt]] = None
default_value:Optional[StrictFloat] = None
min_value: Optional[Union[StrictFloat, StrictInt]] = None
min_value:Optional[StrictFloat] = None
max_value: Optional[Union[StrictFloat, StrictInt]] = None
max_value:Optional[StrictFloat] = None
lower_bound: Optional[StrictStr] = "example_lower_bound"
upper_bound: Optional[StrictStr] = "example_upper_bound"
allow_negative: Optional[StrictBool] = None
allow_negative:Optional[StrictBool] = None
dto_real_instance = DTOReal(type=type, is_nullable=is_nullable, description=description, default_value=default_value, min_value=min_value, max_value=max_value, lower_bound=lower_bound, upper_bound=upper_bound, allow_negative=allow_negative)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

