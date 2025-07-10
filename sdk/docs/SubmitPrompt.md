# SubmitPrompt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **str** |  | 
**session_id** | **str** |  | 
**scope** | **str** |  | [optional] [default to 'default']
## Example

```python
from finbourne_candela.models.submit_prompt import SubmitPrompt
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr

prompt: StrictStr = "example_prompt"
session_id: StrictStr = "example_session_id"
scope: Optional[StrictStr] = "example_scope"
submit_prompt_instance = SubmitPrompt(prompt=prompt, session_id=session_id, scope=scope)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

