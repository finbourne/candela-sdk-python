# Keys

## Example

```python
from finbourne_candela.models.keys import Keys
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with Keys 

dto_str_instance = finbourne_candela.models.dto_str.DTOStr(
                        is_nullable = True, 
                        min_length = 56, 
                        max_length = 56, 
                        regex = '', 
                        format = '', 
                        description = '', 
                        default_value = '', 
                        stop = '', 
                        max_tokens = 56, )

keys_instance = Keys(dto_str_instance)

```
See all compatible oneOf types with Keys


 * [DTOEnum](./DTOEnum.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

