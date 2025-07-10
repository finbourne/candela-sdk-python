# AppSpec

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**circuit** | [**ObjectId**](ObjectId.md) |  | 
**directive** | [**ObjectId**](ObjectId.md) |  | 
## Example

```python
from finbourne_candela.models.app_spec import AppSpec
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, validator

type: StrictStr = "example_type"
circuit: ObjectId = # Replace with your value
directive: ObjectId = # Replace with your value
app_spec_instance = AppSpec(type=type, circuit=circuit, directive=directive)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

