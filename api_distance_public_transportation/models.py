from pydantic import BaseModel, ValidationError, validator


class Payload(BaseModel):
    lat: float
    lon: float

    @validator('lat')
    def lat_validator(cls, la):
        if la >= -24.06423 and la <= -23.18340:
            return la
        raise ValueError('Error Latitude')
        
        
    @validator('lon')
    def lon_validator(cls, lo):
        if lo >= -47.20853 and lo <= -45.69483:
            return lo
        raise ValueError('Error Longitude')
        