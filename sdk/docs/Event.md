# Event

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_type** | **str** |  | 
**content** | **str** |  | 
## Example

```python
from finbourne_candela.models.event import Event
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr, validator

event_type: StrictStr = "example_event_type"
content: StrictStr = "example_content"
event_instance = Event(event_type=event_type, content=content)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

