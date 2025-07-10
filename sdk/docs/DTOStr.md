# DTOStr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'string']
**is_nullable** | **bool** |  | [optional] 
**max_tokens** | **int** |  | 
**regex** | **str** |  | 
**stop** | **str** |  | 
## Example

```python
from finbourne_candela.models.dto_str import DTOStr
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

type: Optional[StrictStr] = "example_type"
is_nullable: Optional[StrictBool] = None
is_nullable:Optional[StrictBool] = None
max_tokens: StrictInt = # Replace with your value
max_tokens: StrictInt = 42
regex: StrictStr = "example_regex"
stop: StrictStr = "example_stop"
dto_str_instance = DTOStr(type=type, is_nullable=is_nullable, max_tokens=max_tokens, regex=regex, stop=stop)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

