class WeatherInsert():

    def __init__(self, data: dict, created_at: str, is_deleted: bool = False) -> None:
        self.data = data
        self.created_at = created_at
        self.is_deleted = is_deleted
    
    def to_json(self):
        return {
            "data": self.data,
            "created_at": self.created_at,
            "is_deleted": self.is_deleted,
        }