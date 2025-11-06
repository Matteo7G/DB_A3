import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from datetime import datetime, date

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(sa.String, nullable=False)
    last_name: Mapped[str] = mapped_column(sa.String, nullable=False)
    email: Mapped[str] = mapped_column(sa.String, nullable=False, unique=True)
    enrollment_date: Mapped[date] = mapped_column(sa.Date)

    def __init__(self, first_name, last_name, email, enrollment_date):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if isinstance(enrollment_date, str):
            self.enrollment_date = datetime.strptime(enrollment_date, "%Y-%m-%d").date()
        else:
            self.enrollment_date = enrollment_date

    def __repr__(self):
        return f"Student(id={self.student_id}, name={self.first_name} {self.last_name}, email={self.email}, enrollment_date={self.enrollment_date})"
