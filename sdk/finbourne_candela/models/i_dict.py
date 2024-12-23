# coding: utf-8

"""
    FINBOURNE Candela Platform Web API

    FINBOURNE Technology  # noqa: E501

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field
from finbourne_candela.models.keys import Keys

class IDict(BaseModel):
    """
    Class representing a variable-sized dictionary with string-valued keys and items of the same defined type.        # noqa: E501
    """
    is_nullable: Optional[Any] = None
    obj: Obj = Field(...)
    keys: Keys = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["is_nullable", "obj", "keys"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

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
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> IDict:
        """Create an instance of IDict from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of obj
        if self.obj:
            _dict['obj'] = self.obj.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keys
        if self.keys:
            _dict['keys'] = self.keys.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if is_nullable (nullable) is None
        # and __fields_set__ contains the field
        if self.is_nullable is None and "is_nullable" in self.__fields_set__:
            _dict['is_nullable'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IDict:
        """Create an instance of IDict from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IDict.parse_obj(obj)

        _obj = IDict.parse_obj({
            "is_nullable": obj.get("is_nullable"),
            "obj": Obj.from_dict(obj.get("obj")) if obj.get("obj") is not None else None,
            "keys": Keys.from_dict(obj.get("keys")) if obj.get("keys") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj