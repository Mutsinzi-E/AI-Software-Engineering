import os

from sqlalchemy import String, create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM models."""
    pass


class User(Base):
    """SQLAlchemy ORM model representing the users table."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )
    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )

    def __repr__(self):
        return (
            f"User(id={self.id!r}, "
            f"username={self.username!r}, "
            f"email={self.email!r})"
        )


def get_database_url():
    """Get the database URL from an environment variable."""
    return os.getenv(
        "DATABASE_URL",
        "sqlite:///users.db"
    )


engine = create_engine(
    get_database_url(),
    echo=False
)

Base.metadata.create_all(engine)


def create_user(session: Session, username: str, email: str):
    """Create a new user with transaction handling."""
    if not username or not email:
        raise ValueError("Username and email are required.")

    user = User(username=username, email=email)

    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError:
        session.rollback()
        raise


def get_user_by_username(session: Session, username: str):
    """Retrieve a user by username."""
    statement = select(User).where(User.username == username)
    return session.scalar(statement)


def update_user_email(
    session: Session,
    username: str,
    new_email: str
):
    """Update a user's email address."""
    if not new_email:
        raise ValueError("New email is required.")

    user = get_user_by_username(session, username)

    if user is None:
        return None

    try:
        user.email = new_email
        session.commit()
        session.refresh(user)
        return user
    except SQLAlchemyError:
        session.rollback()
        raise


def delete_user(session: Session, username: str):
    """Delete a user by username."""
    user = get_user_by_username(session, username)

    if user is None:
        return False

    try:
        session.delete(user)
        session.commit()
        return True
    except SQLAlchemyError:
        session.rollback()
        raise


def list_users(session: Session):
    """Return all users."""
    statement = select(User).order_by(User.id)
    return list(session.scalars(statement).all())


def main():
    """Demonstrate SQLAlchemy ORM CRUD operations."""
    with Session(engine) as session:
        try:
            user = create_user(
                session,
                "enock",
                "enock@example.com"
            )
            print("Created:", user)

            found_user = get_user_by_username(
                session,
                "enock"
            )
            print("Found:", found_user)

            updated_user = update_user_email(
                session,
                "enock",
                "new-enock@example.com"
            )
            print("Updated:", updated_user)

            print("All users:", list_users(session))

            deleted = delete_user(
                session,
                "enock"
            )
            print("Deleted:", deleted)

        except (SQLAlchemyError, ValueError) as error:
            print(f"Operation failed: {error}")


if __name__ == "__main__":
    main()
