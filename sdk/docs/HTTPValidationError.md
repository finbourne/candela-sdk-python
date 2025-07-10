# HTTPValidationError

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | [**List[ValidationError]**](ValidationError.md) |  | [optional] 
## Example

```python
from finbourne_candela.models.http_validation_error import HTTPValidationError
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, conlist

detail: Optional[conlist(ValidationError)] = None
http_validation_error_instance = HTTPValidationError(detail=detail)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

