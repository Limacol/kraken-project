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
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List
from pydantic import BaseModel, StrictBool
from pydantic import Field
from typing_extensions import Annotated
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class SimpleAggregationSource(BaseModel):
    """
    Numbers how many attacks of a certain kind found an aggregated model
    """ # noqa: E501
    bruteforce_subdomains: Annotated[int, Field(strict=True, ge=0)] = Field(description="Bruteforce subdomains via DNS requests")
    tcp_port_scan: Annotated[int, Field(strict=True, ge=0)] = Field(description="Scan tcp ports")
    query_certificate_transparency: Annotated[int, Field(strict=True, ge=0)] = Field(description="Query certificate transparency")
    query_dehashed: Annotated[int, Field(strict=True, ge=0)] = Field(description="Query the dehashed API")
    host_alive: Annotated[int, Field(strict=True, ge=0)] = Field(description="Check if a host is reachable via icmp")
    service_detection: Annotated[int, Field(strict=True, ge=0)] = Field(description="Detect the service that is running on a port")
    dns_resolution: Annotated[int, Field(strict=True, ge=0)] = Field(description="Resolve domain names")
    forced_browsing: Annotated[int, Field(strict=True, ge=0)] = Field(description="Perform forced browsing")
    os_detection: Annotated[int, Field(strict=True, ge=0)] = Field(description="Detect the OS of the target")
    anti_port_scanning_detection: Annotated[int, Field(strict=True, ge=0)] = Field(description="Detect if anti-port scanning techniques are in place")
    udp_port_scan: Annotated[int, Field(strict=True, ge=0)] = Field(description="Scan udp ports")
    version_detection: Annotated[int, Field(strict=True, ge=0)] = Field(description="Perform version detection")
    manual: StrictBool = Field(description="Manually inserted")
    __properties: ClassVar[List[str]] = ["bruteforce_subdomains", "tcp_port_scan", "query_certificate_transparency", "query_dehashed", "host_alive", "service_detection", "dns_resolution", "forced_browsing", "os_detection", "anti_port_scanning_detection", "udp_port_scan", "version_detection", "manual"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of SimpleAggregationSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of SimpleAggregationSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bruteforce_subdomains": obj.get("bruteforce_subdomains"),
            "tcp_port_scan": obj.get("tcp_port_scan"),
            "query_certificate_transparency": obj.get("query_certificate_transparency"),
            "query_dehashed": obj.get("query_dehashed"),
            "host_alive": obj.get("host_alive"),
            "service_detection": obj.get("service_detection"),
            "dns_resolution": obj.get("dns_resolution"),
            "forced_browsing": obj.get("forced_browsing"),
            "os_detection": obj.get("os_detection"),
            "anti_port_scanning_detection": obj.get("anti_port_scanning_detection"),
            "udp_port_scan": obj.get("udp_port_scan"),
            "version_detection": obj.get("version_detection"),
            "manual": obj.get("manual")
        })
        return _obj


