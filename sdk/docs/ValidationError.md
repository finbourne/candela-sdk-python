# ValidationError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loc** | [**List[ValidationErrorLocInner]**](ValidationErrorLocInner.md) |  | 
**msg** | **str** |  | 
**type** | **str** |  | 
## Example

```python
from finbourne_candela.models.validation_error import ValidationError
from typing import Any, Dict, List
from pydantic.v1 import BaseModel, Field, StrictStr, conlist

loc: conlist(ValidationErrorLocInner) = # Replace with your value
msg: StrictStr = "example_msg"
type: StrictStr = "example_type"
validation_error_instance = ValidationError(loc=loc, msg=msg, type=type)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

