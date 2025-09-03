# models.py
from sqlalchemy import Column, Integer, String, Float, Date, Boolean, ForeignKey
from db import Base

class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)

    # Core fields
    date = Column(Date, nullable=False)
    store_id = Column(Integer, index=True, nullable=False)
    sales = Column(Float, nullable=False)

    # Engineered features
    weekday = Column(String)                # Monday, Tuesday, etc.
    month = Column(Integer)                 # numeric month 1-12
    sales_category = Column(String)         # e.g. High/Low sales bucket
    cumulative_sales = Column(Float)        # running sum
    promo_day = Column(Boolean, default=False)
    zscore = Column(Float)                  # anomaly detection
    anomaly = Column(String)                # "Normal" or "Anomaly"
    footfall_est = Column(Integer)          # estimated customers

    # Link back to dataset
    dataset_id = Column(Integer, index=True)  # optional: ForeignKey("datasets.id")


