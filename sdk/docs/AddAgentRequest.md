# AddAgentRequest

Create/update Agent Request body
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | The unique code for the agent | [optional] 
**name** | **str** | The name of the agent as it is referred to by Candela. This must be unique to avoid clashes. | 
**prompt** | **str** | The agent&#39;s prompt | 
**example_prompts** | **List[str]** | Example prompts to offer the user | [optional] 
**is_enabled** | **bool** | Whether the agent is enabled | 
**tool_names** | **List[str]** | The list of MCP tools that this agent is allowed to use | 
**description** | **str** | A description of the agent | 
## Example

```python
from finbourne_candela.models.add_agent_request import AddAgentRequest
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

code: Optional[StrictStr] = "example_code"
name: StrictStr = "example_name"
prompt: StrictStr = "example_prompt"
example_prompts: Optional[List[StrictStr]] = # Replace with your value
is_enabled: StrictBool = # Replace with your value
is_enabled:StrictBool = True
tool_names: List[StrictStr] = # Replace with your value
description: StrictStr = "example_description"
add_agent_request_instance = AddAgentRequest(code=code, name=name, prompt=prompt, example_prompts=example_prompts, is_enabled=is_enabled, tool_names=tool_names, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

