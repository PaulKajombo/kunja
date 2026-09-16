from pathlib import Path

from src.services.storage.base import BaseStorageProvider


class LocalStorageProvider(BaseStorageProvider):
    """Filesystem-backed storage for local development."""

    def __init__(self, base_dir: str = "uploads"):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def _path(self, key: str) -> Path:
        candidate = (self.base_dir / key).resolve()
        base = self.base_dir.resolve()
        if not candidate.is_relative_to(base):
            raise ValueError("Storage key escapes base directory")
        return candidate

    def save(self, key: str, content: bytes, content_type: str = "application/octet-stream") -> str:
        target = self._path(key)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(content)
        return key

    def open(self, key: str) -> bytes:
        target = self._path(key)
        if not target.is_file():
            raise FileNotFoundError(f"Stored object not found: {key}")
        return target.read_bytes()

    def delete(self, key: str) -> None:
        target = self._path(key)
        if target.is_file():
            target.unlink()

    def get_url(self, key: str) -> str:
        return f"/api/v1/documents/download/{key}"