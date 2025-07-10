# ToolObj

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_type** | **str** |  | [optional] 
**instruction** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.tool_obj import ToolObj
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

tool_type: Optional[StrictStr] = "example_tool_type"
instruction: Optional[StrictStr] = "example_instruction"
tool_obj_instance = ToolObj(tool_type=tool_type, instruction=instruction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

