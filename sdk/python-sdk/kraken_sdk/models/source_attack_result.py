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
from kraken_sdk.models.source_attack_result_one_of import SourceAttackResultOneOf
from kraken_sdk.models.source_attack_result_one_of1 import SourceAttackResultOneOf1
from kraken_sdk.models.source_attack_result_one_of2 import SourceAttackResultOneOf2
from kraken_sdk.models.source_attack_result_one_of3 import SourceAttackResultOneOf3
from kraken_sdk.models.source_attack_result_one_of4 import SourceAttackResultOneOf4
from kraken_sdk.models.source_attack_result_one_of5 import SourceAttackResultOneOf5
from kraken_sdk.models.source_attack_result_one_of6 import SourceAttackResultOneOf6
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

SOURCEATTACKRESULT_ONE_OF_SCHEMAS = ["SourceAttackResultOneOf", "SourceAttackResultOneOf1", "SourceAttackResultOneOf2", "SourceAttackResultOneOf3", "SourceAttackResultOneOf4", "SourceAttackResultOneOf5", "SourceAttackResultOneOf6"]

class SourceAttackResult(BaseModel):
    """
    The different types of attack and their results
    """
    # data type: SourceAttackResultOneOf
    oneof_schema_1_validator: Optional[SourceAttackResultOneOf] = None
    # data type: SourceAttackResultOneOf1
    oneof_schema_2_validator: Optional[SourceAttackResultOneOf1] = None
    # data type: SourceAttackResultOneOf2
    oneof_schema_3_validator: Optional[SourceAttackResultOneOf2] = None
    # data type: SourceAttackResultOneOf3
    oneof_schema_4_validator: Optional[SourceAttackResultOneOf3] = None
    # data type: SourceAttackResultOneOf4
    oneof_schema_5_validator: Optional[SourceAttackResultOneOf4] = None
    # data type: SourceAttackResultOneOf5
    oneof_schema_6_validator: Optional[SourceAttackResultOneOf5] = None
    # data type: SourceAttackResultOneOf6
    oneof_schema_7_validator: Optional[SourceAttackResultOneOf6] = None
    actual_instance: Optional[Union[SourceAttackResultOneOf, SourceAttackResultOneOf1, SourceAttackResultOneOf2, SourceAttackResultOneOf3, SourceAttackResultOneOf4, SourceAttackResultOneOf5, SourceAttackResultOneOf6]] = None
    one_of_schemas: List[str] = Literal["SourceAttackResultOneOf", "SourceAttackResultOneOf1", "SourceAttackResultOneOf2", "SourceAttackResultOneOf3", "SourceAttackResultOneOf4", "SourceAttackResultOneOf5", "SourceAttackResultOneOf6"]

    model_config = {
        "validate_assignment": True
    }


    discriminator_value_class_map: Dict[str, str] = {
        'SourceAttack': 'SourceAttack'
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
        instance = SourceAttackResult.model_construct()
        error_messages = []
        match = 0
        # validate data type: SourceAttackResultOneOf
        if not isinstance(v, SourceAttackResultOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf`")
        else:
            match += 1
        # validate data type: SourceAttackResultOneOf1
        if not isinstance(v, SourceAttackResultOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf1`")
        else:
            match += 1
        # validate data type: SourceAttackResultOneOf2
        if not isinstance(v, SourceAttackResultOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf2`")
        else:
            match += 1
        # validate data type: SourceAttackResultOneOf3
        if not isinstance(v, SourceAttackResultOneOf3):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf3`")
        else:
            match += 1
        # validate data type: SourceAttackResultOneOf4
        if not isinstance(v, SourceAttackResultOneOf4):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf4`")
        else:
            match += 1
        # validate data type: SourceAttackResultOneOf5
        if not isinstance(v, SourceAttackResultOneOf5):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf5`")
        else:
            match += 1
        # validate data type: SourceAttackResultOneOf6
        if not isinstance(v, SourceAttackResultOneOf6):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SourceAttackResultOneOf6`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in SourceAttackResult with oneOf schemas: SourceAttackResultOneOf, SourceAttackResultOneOf1, SourceAttackResultOneOf2, SourceAttackResultOneOf3, SourceAttackResultOneOf4, SourceAttackResultOneOf5, SourceAttackResultOneOf6. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in SourceAttackResult with oneOf schemas: SourceAttackResultOneOf, SourceAttackResultOneOf1, SourceAttackResultOneOf2, SourceAttackResultOneOf3, SourceAttackResultOneOf4, SourceAttackResultOneOf5, SourceAttackResultOneOf6. Details: " + ", ".join(error_messages))
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

        # deserialize data into SourceAttackResultOneOf
        try:
            instance.actual_instance = SourceAttackResultOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAttackResultOneOf1
        try:
            instance.actual_instance = SourceAttackResultOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAttackResultOneOf2
        try:
            instance.actual_instance = SourceAttackResultOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAttackResultOneOf3
        try:
            instance.actual_instance = SourceAttackResultOneOf3.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAttackResultOneOf4
        try:
            instance.actual_instance = SourceAttackResultOneOf4.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAttackResultOneOf5
        try:
            instance.actual_instance = SourceAttackResultOneOf5.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SourceAttackResultOneOf6
        try:
            instance.actual_instance = SourceAttackResultOneOf6.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into SourceAttackResult with oneOf schemas: SourceAttackResultOneOf, SourceAttackResultOneOf1, SourceAttackResultOneOf2, SourceAttackResultOneOf3, SourceAttackResultOneOf4, SourceAttackResultOneOf5, SourceAttackResultOneOf6. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into SourceAttackResult with oneOf schemas: SourceAttackResultOneOf, SourceAttackResultOneOf1, SourceAttackResultOneOf2, SourceAttackResultOneOf3, SourceAttackResultOneOf4, SourceAttackResultOneOf5, SourceAttackResultOneOf6. Details: " + ", ".join(error_messages))
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


