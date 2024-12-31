from sqlalchemy import String
from core.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class FrontPreferences(Base):
    __tablename__ = "url_management"

    category: Mapped[str] = mapped_column(String(255), nullable=False )
    public_type: Mapped[int] = mapped_column(String(255), nullable=False)
    storage_type: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String(255), primary_key=True, index=True)
    end_point: Mapped[str] = mapped_column(String(255), nullable=False)
    word_1: Mapped[str] = mapped_column(String(255), nullable=False)
    word_2: Mapped[str] = mapped_column(String(255), nullable=False)
    
    