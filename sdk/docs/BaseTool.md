# BaseTool

Base class for tools
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_type** | **str** |  | [optional] 
**instruction** | **str** |  | [optional] 
## Example

```python
from finbourne_candela.models.base_tool import BaseTool
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictStr

tool_type: Optional[StrictStr] = "example_tool_type"
instruction: Optional[StrictStr] = "example_instruction"
base_tool_instance = BaseTool(tool_type=tool_type, instruction=instruction)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

