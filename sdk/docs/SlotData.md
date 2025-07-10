# SlotData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**slot_id** | **str** |  | 
**slot_type** | **str** |  | 
**domain** | **str** |  | 
**state** | [**SlotState**](SlotState.md) |  | [optional] 
**assigned_to** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**assigned** | **datetime** |  | [optional] 
**disposed** | **datetime** |  | [optional] 
**ready** | **datetime** |  | [optional] 
## Example

```python
from finbourne_candela.models.slot_data import SlotData
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr
from datetime import datetime
slot_id: StrictStr = "example_slot_id"
slot_type: StrictStr = "example_slot_type"
domain: StrictStr = "example_domain"
state: Optional[SlotState] = None
assigned_to: Optional[StrictStr] = "example_assigned_to"
url: Optional[StrictStr] = "example_url"
created: Optional[datetime] = None
assigned: Optional[datetime] = None
disposed: Optional[datetime] = None
ready: Optional[datetime] = None
slot_data_instance = SlotData(slot_id=slot_id, slot_type=slot_type, domain=domain, state=state, assigned_to=assigned_to, url=url, created=created, assigned=assigned, disposed=disposed, ready=ready)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

