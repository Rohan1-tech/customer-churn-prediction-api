from pydantic import BaseModel

class ChurnRequest(BaseModel):
    Frequency: float
    Monetary: float
    AOV: float