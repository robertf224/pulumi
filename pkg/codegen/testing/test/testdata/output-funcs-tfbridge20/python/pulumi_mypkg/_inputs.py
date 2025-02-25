# coding=utf-8
# *** WARNING: this file was generated by test. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAmiIdsFilterArgs',
]

@pulumi.input_type
class GetAmiIdsFilterArgs:
    def __init__(__self__, *,
                 name: str,
                 values: Sequence[str]):
        GetAmiIdsFilterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            values=values,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             values: Optional[Sequence[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if values is None:
            raise TypeError("Missing 'values' argument")

        _setter("name", name)
        _setter("values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: str):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        return pulumi.get(self, "values")

    @values.setter
    def values(self, value: Sequence[str]):
        pulumi.set(self, "values", value)


