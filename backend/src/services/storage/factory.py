from src.config import settings
from src.services.storage.base import BaseStorageProvider
from src.services.storage.local import LocalStorageProvider

_STORAGE: BaseStorageProvider | None = None


def get_storage() -> BaseStorageProvider:
    """Return the configured storage provider (singleton per process)."""
    global _STORAGE
    if _STORAGE is not None:
        return _STORAGE

    driver = settings.STORAGE_DRIVER
    if driver == "local":
        _STORAGE = LocalStorageProvider(settings.UPLOAD_DIR)
    else:
        raise RuntimeError(
            f"Unsupported STORAGE_DRIVER: {driver!r}. "
            "Supported drivers: local (s3/cloud coming soon)."
        )
    return _STORAGE