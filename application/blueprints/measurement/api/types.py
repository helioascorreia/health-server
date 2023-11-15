import strawberry


@strawberry.type
class Measurement:
    id: str
    # document_id: str
    # date_time: strawberry.auto
    weight: float
    # metabolic_age: strawberry.auto

