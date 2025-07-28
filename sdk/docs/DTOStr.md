# DTOStr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'string']
**is_nullable** | **bool** |  | [optional] 
**min_length** | **int** |  | [optional] 
**max_length** | **int** |  | [optional] 
**regex** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**default_value** | **str** |  | [optional] 
**stop** | **str** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
## Example

```python
from finbourne_candela.models.dto_str import DTOStr
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictBool, StrictInt, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
min_length: Optional[StrictInt] = None
min_length: Optional[StrictInt] = None
max_length: Optional[StrictInt] = None
max_length: Optional[StrictInt] = None
regex: Optional[StrictStr] = "example_regex"
format: Optional[StrictStr] = "example_format"
description: Optional[StrictStr] = "example_description"
default_value: Optional[StrictStr] = "example_default_value"
stop: Optional[StrictStr] = "example_stop"
max_tokens: Optional[StrictInt] = None
max_tokens: Optional[StrictInt] = None
dto_str_instance = DTOStr(type=type, is_nullable=is_nullable, min_length=min_length, max_length=max_length, regex=regex, format=format, description=description, default_value=default_value, stop=stop, max_tokens=max_tokens)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

