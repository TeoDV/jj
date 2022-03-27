from typing import Any, Dict

from packed import packable

from ._expiration_policy import ExpirationPolicy

__all__ = ("ExpireNever",)


@packable("jj.expiration_policy.ExpireNever")
class ExpireNever(ExpirationPolicy):
    def is_expired(self) -> bool:
        return False

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}()"

    def __packed__(self) -> Dict[str, Any]:
        return dict()

    @classmethod
    def __unpacked__(cls, **kwargs: Any) -> "ExpireNever":
        return cls()
