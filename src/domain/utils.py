from sqlalchemy import Column, DateTime, func

from config.db_connection import Base


class ActivityTracking(Base):
    """
    ## Abstract base model for tracking user activities.

    `Attributes`:
    - `created_at (datetime)`: Timestamp indicating when the activity record was created.
    - `modified_at (datetime)`: Timestamp indicating the last modification time of the activity record.

    `Notes`:
    - This model serves as an abstract base for tracking model activities.
    """

    __abstract__ = True

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False
    )
