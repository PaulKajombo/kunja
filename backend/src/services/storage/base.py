from abc import ABC, abstractmethod


class BaseStorageProvider(ABC):
    """Abstract object-storage interface. Implementations: local, S3, R2, Supabase."""

    @abstractmethod
    def save(self, key: str, content: bytes, content_type: str = "application/octet-stream") -> str:
        """Persist content under `key` and return the storage key/path."""

    @abstractmethod
    def open(self, key: str) -> bytes:
        """Read the full content of the object at `key`."""

    @abstractmethod
    def delete(self, key: str) -> None:
        """Remove the object at `key`."""

    @abstractmethod
    def get_url(self, key: str) -> str:
        """Return a URL consumers can use to fetch the object."""