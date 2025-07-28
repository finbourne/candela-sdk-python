# Fields

## Example

```python
from finbourne_candela.models.fields import Fields
from typing import Any, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator

# Example with Fields 

dto_dict_instance = finbourne_candela.models.dto_dict.DTODict(
                        is_nullable = True, 
                        obj = null, 
                        keys = null, 
                        min_size = 56, 
                        max_size = 56, 
                        description = '', )

fields_instance = Fields(dto_dict_instance)

```
See all compatible oneOf types with Fields


 * [DTOArr](./DTOArr.md)

 * [DTOObj](./DTOObj.md)

 * [DTOEnum](./DTOEnum.md)

 * [DTOStr](./DTOStr.md)

 * [DTOBool](./DTOBool.md)

 * [DTOReal](./DTOReal.md)

 * [DTOInt](./DTOInt.md)

 * [DTOConst](./DTOConst.md)

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

