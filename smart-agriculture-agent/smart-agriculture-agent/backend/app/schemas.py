from pydantic import BaseModel, Field

class CropRequest(BaseModel):
    nitrogen: float = Field(..., ge=0)
    phosphorus: float = Field(..., ge=0)
    potassium: float = Field(..., ge=0)
    temperature: float
    humidity: float = Field(..., ge=0, le=100)
    ph: float = Field(..., ge=0, le=14)
    rainfall: float = Field(..., ge=0)

class AssistantRequest(BaseModel):
    question: str
    crop: str | None = None
    location: str | None = None

class IrrigationRequest(BaseModel):
    temperature: float
    humidity: float
    rainfall: float
    soil_moisture: float = Field(..., ge=0, le=100)
