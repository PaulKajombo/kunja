from sqlalchemy.orm import Session

from src.models.models import User


class UserRepository:
    """All SQLAlchemy queries for users live here."""

    @staticmethod
    def get_by_email(db: Session, email: str) -> User | None:
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def get_by_id(db: Session, user_id: int) -> User | None:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def create(
        db: Session,
        *,
        email: str,
        hashed_password: str,
        full_name: str,
        country: str,
    ) -> User:
        user = User(
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
            country=country,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user