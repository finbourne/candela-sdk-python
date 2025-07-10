# Nodes

## Example

```python
from finbourne_candela.models.nodes import Nodes
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with Nodes 

response_dto_instance = finbourne_candela.models.response_dto.ResponseDTO(
                        type = 'response', 
                        node_id = '', 
                        child_id = '', 
                        as_block = True, 
                        template = '', 
                        context = '', 
                        inserts = {
                            'key' : ''
                            }, )

nodes_instance = Nodes(response_dto_instance)

```
See all compatible oneOf types with Nodes


 * [IntentDTO](./IntentDTO.md)

 * [ConfirmDTO](./ConfirmDTO.md)

 * [NoOpDTO](./NoOpDTO.md)

 * [UseToolDTO](./UseToolDTO.md)

 * [SwitchDTO](./SwitchDTO.md)

 * [InsertContextDTO](./InsertContextDTO.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

