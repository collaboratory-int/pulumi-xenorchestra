# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import builtins
import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from .. import _utilities

insecure: Optional[bool]
"""
Whether SSL should be verified or not. Can be set via the XOA_INSECURE environment variable.
"""

password: Optional[str]
"""
Password for xoa api. Can be set via the XOA_PASSWORD environment variable.
"""

retryMaxTime: Optional[str]
"""
If `retry_mode` is set, this specifies the duration for which the backoff method will continue retries. Can be set via
the `XOA_RETRY_MAX_TIME` environment variable
"""

retryMode: Optional[str]
"""
Specifies if retries should be attempted for requests that require eventual . Can be set via the XOA_RETRY_MODE
environment variable.
"""

token: Optional[str]
"""
Password for xoa api. Can be set via the XOA_TOKEN environment variable.
"""

url: Optional[str]
"""
Hostname of the xoa router. Can be set via the XOA_URL environment variable.
"""

username: Optional[str]
"""
User account for xoa api. Can be set via the XOA_USER environment variable.
"""

