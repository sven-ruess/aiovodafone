"""aiovodafone library."""

__version__ = "0.11.0"

from .api import (
    VodafoneStationCommonApi,
    VodafoneStationDevice,
    VodafoneStationSercommApi,
    VodafoneStationTechnicolorApi,
)
from .const import (
    DeviceType,
)
from .exceptions import (
    AlreadyLogged,
    CannotAuthenticate,
    CannotConnect,
    GenericLoginError,
    ModelNotSupported,
    VodafoneError,
)

__all__ = [
    "AlreadyLogged",
    "CannotAuthenticate",
    "CannotConnect",
    "DeviceType",
    "GenericLoginError",
    "ModelNotSupported",
    "VodafoneError",
    "VodafoneStationCommonApi",
    "VodafoneStationDevice",
    "VodafoneStationSercommApi",
    "VodafoneStationTechnicolorApi",
]
