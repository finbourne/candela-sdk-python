# ToolMetadata

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** |  | 
**scope** | **str** |  | 
**module_name** | **str** |  | 
**module_version** | **str** |  | 
## Example

```python
from finbourne_candela.models.tool_metadata import ToolMetadata
from typing import Any, Dict
from pydantic.v1 import BaseModel, Field, StrictStr

tool_name: StrictStr = "example_tool_name"
scope: StrictStr = "example_scope"
module_name: StrictStr = "example_module_name"
module_version: StrictStr = "example_module_version"
tool_metadata_instance = ToolMetadata(tool_name=tool_name, scope=scope, module_name=module_name, module_version=module_version)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

