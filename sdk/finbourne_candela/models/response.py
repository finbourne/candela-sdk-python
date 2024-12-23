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
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr

class Response(BaseModel):
    """
    Class representing a response state in a circuit. Response states are normal chat responses that can optionally be constrained to a particular form with a guidance template.  # noqa: E501
    """
    node_id: Optional[StrictStr] = None
    node_type: Optional[StrictStr] = None
    as_block: StrictBool = Field(...)
    child_id: Optional[StrictStr] = None
    template: Optional[StrictStr] = Field(...)
    context: Optional[StrictStr] = Field(...)
    inserts: Optional[Any] = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["node_id", "node_type", "as_block", "child_id", "template", "context", "inserts"]

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
    def from_json(cls, json_str: str) -> Response:
        """Create an instance of Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if node_id (nullable) is None
        # and __fields_set__ contains the field
        if self.node_id is None and "node_id" in self.__fields_set__:
            _dict['node_id'] = None

        # set to None if node_type (nullable) is None
        # and __fields_set__ contains the field
        if self.node_type is None and "node_type" in self.__fields_set__:
            _dict['node_type'] = None

        # set to None if child_id (nullable) is None
        # and __fields_set__ contains the field
        if self.child_id is None and "child_id" in self.__fields_set__:
            _dict['child_id'] = None

        # set to None if template (nullable) is None
        # and __fields_set__ contains the field
        if self.template is None and "template" in self.__fields_set__:
            _dict['template'] = None

        # set to None if context (nullable) is None
        # and __fields_set__ contains the field
        if self.context is None and "context" in self.__fields_set__:
            _dict['context'] = None

        # set to None if inserts (nullable) is None
        # and __fields_set__ contains the field
        if self.inserts is None and "inserts" in self.__fields_set__:
            _dict['inserts'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Response:
        """Create an instance of Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Response.parse_obj(obj)

        _obj = Response.parse_obj({
            "node_id": obj.get("node_id"),
            "node_type": obj.get("node_type"),
            "as_block": obj.get("as_block"),
            "child_id": obj.get("child_id"),
            "template": obj.get("template"),
            "context": obj.get("context"),
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj
