# AgentDefinition

The details of an agent
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **str** | The scope of the agent | [optional] 
**code** | **str** | The unique code for the agent | [optional] 
**version** | **int** | The version of the agent | 
**name** | **str** | The name of the agent as it is referred to by Candela. This must be unique to avoid clashes. | 
**prompt** | **str** | The agent&#39;s prompt | 
**example_prompts** | **List[str]** | Example prompts to offer the uer | [optional] 
**created_by** | **str** | The unique identifier of the user who created the agent | 
**created_at** | **datetime** | The date and time when the agent was created | 
**is_enabled** | **bool** | Whether the agent is enabled | 
**tool_names** | **List[str]** | The list of MCP tools that this agent is allowed to use | 
**description** | **str** | A description of the agent | 
## Example

```python
from finbourne_candela.models.agent_definition import AgentDefinition
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

scope: Optional[StrictStr] = "example_scope"
code: Optional[StrictStr] = "example_code"
version: StrictInt = # Replace with your value
version: StrictInt = 42
name: StrictStr = "example_name"
prompt: StrictStr = "example_prompt"
example_prompts: Optional[List[StrictStr]] = # Replace with your value
created_by: StrictStr = "example_created_by"
created_at: datetime = # Replace with your value
is_enabled: StrictBool = # Replace with your value
is_enabled:StrictBool = True
tool_names: List[StrictStr] = # Replace with your value
description: StrictStr = "example_description"
agent_definition_instance = AgentDefinition(scope=scope, code=code, version=version, name=name, prompt=prompt, example_prompts=example_prompts, created_by=created_by, created_at=created_at, is_enabled=is_enabled, tool_names=tool_names, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

