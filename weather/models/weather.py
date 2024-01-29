from fastapi.encoders import jsonable_encoder

# Pydantic, and Python's built-in typing are used to define a schema
# that defines the structure and types of the different objects stored
# in the recipes collection, and managed by this API.
from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional, Union, Dict
from datetime import datetime
from bson import ObjectId

BaseModel.model_config["json_encoders"] = {ObjectId: lambda v: str(v)}


class WeatherValue(BaseModel):
    data: Dict
    created_at: str
    is_deleted: bool


class Weather(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


    id: ObjectId = Field(None, alias="_id")
    value: WeatherValue

    def to_json(self):
        return jsonable_encoder(self, exclude_none=True)

    def to_bson(self):
        data = self.model_dump(by_alias=True, exclude_none=True)
        if data.get("_id") is None:
            data.pop("_id", None)
        return data
    