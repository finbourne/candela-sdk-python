# Directive

Class that encapsulates directive (system prompt) content and its application to the llm dialogue.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | **str** |  | [optional] [default to ' * ']
**hide** | **bool** |  | [optional] [default to True]
**identity** | [**AnyOf**](AnyOf.md) |  | [optional] 
**purpose** | [**AnyOf**](AnyOf.md) |  | [optional] 
**style** | [**AnyOf**](AnyOf.md) |  | [optional] 
**restriction** | [**AnyOf**](AnyOf.md) |  | [optional] 
**context_vals** | **Dict[str, str]** |  | [optional] 
## Example

```python
from finbourne_candela.models.directive import Directive
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, StrictBool, StrictStr, validator

point: Optional[StrictStr] = "example_point"
hide: Optional[StrictBool] = True
hide:Optional[StrictBool] = None
identity: Optional[Any] = None
purpose: Optional[Any] = None
style: Optional[Any] = None
restriction: Optional[Any] = None
context_vals: Optional[Any] = None
directive_instance = Directive(point=point, hide=hide, identity=identity, purpose=purpose, style=style, restriction=restriction, context_vals=context_vals)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

