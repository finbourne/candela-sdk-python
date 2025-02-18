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
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, validator 
from finbourne_candela.models.circuit import Circuit

class PostCircuit(BaseModel):
    """
    PostCircuit
    """
    scope:  StrictStr = Field(...,alias="scope") 
    identifier:  StrictStr = Field(...,alias="identifier") 
    description:  Optional[StrictStr] = Field(None,alias="description") 
    version_bump:  Optional[StrictStr] = Field(None,alias="version_bump") 
    data: Circuit = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["scope", "identifier", "description", "version_bump", "data"]

    @validator('version_bump')
    def version_bump_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('major', 'minor', 'patch'):
            raise ValueError("must be one of enum values ('major', 'minor', 'patch')")
        return value

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
    def from_json(cls, json_str: str) -> PostCircuit:
        """Create an instance of PostCircuit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostCircuit:
        """Create an instance of PostCircuit from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostCircuit.parse_obj(obj)

        _obj = PostCircuit.parse_obj({
            "scope": obj.get("scope"),
            "identifier": obj.get("identifier"),
            "description": obj.get("description"),
            "version_bump": obj.get("version_bump") if obj.get("version_bump") is not None else 'patch',
            "data": Circuit.from_dict(obj.get("data")) if obj.get("data") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
