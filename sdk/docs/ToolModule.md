# ToolModule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
## Example

```python
from finbourne_candela.models.tool_module import ToolModule
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

content: StrictStr = "example_content"
tool_module_instance = ToolModule(content=content)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

