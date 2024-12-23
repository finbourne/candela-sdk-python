# coding: utf-8

"""
    FINBOURNE Candela Platform Web API

    FINBOURNE Technology  # noqa: E501

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, ValidationError, validator
from finbourne_candela.models.base_tool import BaseTool
from typing import Union, Any, List, TYPE_CHECKING
from pydantic.v1 import StrictStr, Field

TOOLOBJ_ANY_OF_SCHEMAS = ["BaseTool", "object"]

class ToolObj(BaseModel):
    """
    ToolObj
    """

    # data type: object
    anyof_schema_1_validator: Optional[Dict[str, Any]] = None
    # data type: BaseTool
    anyof_schema_2_validator: Optional[BaseTool] = None
    if TYPE_CHECKING:
        actual_instance: Union[BaseTool, object]
    else:
        actual_instance: Any
    any_of_schemas: List[str] = Field(TOOLOBJ_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        instance = ToolObj.construct()
        error_messages = []
        # validate data type: object
        try:
            instance.anyof_schema_1_validator = v
            return v
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # validate data type: BaseTool
        if not isinstance(v, BaseTool):
            error_messages.append(f"Error! Input type `{type(v)}` is not `BaseTool`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when setting the actual_instance in ToolObj with anyOf schemas: BaseTool, object. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ToolObj:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ToolObj:
        """Returns the object represented by the json string"""
        instance = ToolObj.construct()
        error_messages = []
        # deserialize data into object
        try:
            # validation
            instance.anyof_schema_1_validator = json.loads(json_str)
            # assign value to actual_instance
            instance.actual_instance = instance.anyof_schema_1_validator
            return instance
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[BaseTool] = None
        try:
            instance.actual_instance = BaseTool.from_json(json_str)
            return instance
        except (ValidationError, ValueError) as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ToolObj with anyOf schemas: BaseTool, object. Details: " + ", ".join(error_messages))
        else:
            return instance

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_dict()
        else:
            return json.dumps(self.actual_instance)
