from beanie import Document


class Measurement(Document):
    weight: float

    class Settings:
        name = "measurement"
