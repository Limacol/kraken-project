# coding: utf-8

"""
    kraken

    The core component of kraken-project

    The version of the OpenAPI document: 0.1.0
    Contact: git@omikron.dev
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from kraken_sdk.models.manual_insert_one_of import ManualInsertOneOf
from kraken_sdk.models.manual_insert_one_of1 import ManualInsertOneOf1
from kraken_sdk.models.manual_insert_one_of2 import ManualInsertOneOf2
from kraken_sdk.models.manual_insert_one_of3 import ManualInsertOneOf3
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

MANUALINSERT_ONE_OF_SCHEMAS = ["ManualInsertOneOf", "ManualInsertOneOf1", "ManualInsertOneOf2", "ManualInsertOneOf3"]

class ManualInsert(BaseModel):
    """
    The different types of manual inserts
    """
    # data type: ManualInsertOneOf
    oneof_schema_1_validator: Optional[ManualInsertOneOf] = None
    # data type: ManualInsertOneOf1
    oneof_schema_2_validator: Optional[ManualInsertOneOf1] = None
    # data type: ManualInsertOneOf2
    oneof_schema_3_validator: Optional[ManualInsertOneOf2] = None
    # data type: ManualInsertOneOf3
    oneof_schema_4_validator: Optional[ManualInsertOneOf3] = None
    actual_instance: Optional[Union[ManualInsertOneOf, ManualInsertOneOf1, ManualInsertOneOf2, ManualInsertOneOf3]] = None
    one_of_schemas: List[str] = Literal["ManualInsertOneOf", "ManualInsertOneOf1", "ManualInsertOneOf2", "ManualInsertOneOf3"]

    model_config = {
        "validate_assignment": True
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ManualInsert.model_construct()
        error_messages = []
        match = 0
        # validate data type: ManualInsertOneOf
        if not isinstance(v, ManualInsertOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ManualInsertOneOf`")
        else:
            match += 1
        # validate data type: ManualInsertOneOf1
        if not isinstance(v, ManualInsertOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ManualInsertOneOf1`")
        else:
            match += 1
        # validate data type: ManualInsertOneOf2
        if not isinstance(v, ManualInsertOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ManualInsertOneOf2`")
        else:
            match += 1
        # validate data type: ManualInsertOneOf3
        if not isinstance(v, ManualInsertOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ManualInsertOneOf3`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ManualInsert with oneOf schemas: ManualInsertOneOf, ManualInsertOneOf1, ManualInsertOneOf2, ManualInsertOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ManualInsert with oneOf schemas: ManualInsertOneOf, ManualInsertOneOf1, ManualInsertOneOf2, ManualInsertOneOf3. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ManualInsertOneOf
        try:
            instance.actual_instance = ManualInsertOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ManualInsertOneOf1
        try:
            instance.actual_instance = ManualInsertOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ManualInsertOneOf2
        try:
            instance.actual_instance = ManualInsertOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ManualInsertOneOf3
        try:
            instance.actual_instance = ManualInsertOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ManualInsert with oneOf schemas: ManualInsertOneOf, ManualInsertOneOf1, ManualInsertOneOf2, ManualInsertOneOf3. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ManualInsert with oneOf schemas: ManualInsertOneOf, ManualInsertOneOf1, ManualInsertOneOf2, ManualInsertOneOf3. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


