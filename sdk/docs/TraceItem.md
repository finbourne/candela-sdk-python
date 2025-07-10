# TraceItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_type** | **str** |  | 
**content** | **str** |  | 
## Example

```python
from finbourne_candela.models.trace_item import TraceItem
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, validator

item_type: StrictStr = "example_item_type"
content: StrictStr = "example_content"
trace_item_instance = TraceItem(item_type=item_type, content=content)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

