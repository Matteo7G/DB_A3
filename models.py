import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Mapped, mapped_column

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(sa.String, nullable=False)
    last_name: Mapped[str] = mapped_column(sa.String, nullable=False)
    email: Mapped[str] = mapped_column(sa.String, nullable=False, unique=True)
    enrollment_date: Mapped[sa.Date] = mapped_column(sa.Date)

