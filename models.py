from pydantic import BaseModel, field_validator
from utils import clean_int, clean_number


class CustomerDetails(BaseModel):
    name: str
    billing_address: str
    phone: str
    email: str
    enquiry_id: str
    place_of_supply: str


class Item(BaseModel):
    description: str
    hsn: int
    rate: float
    quantity: int
    amount: float

    @field_validator("rate", "amount", mode="before")
    def parse_float(cls, value):
        if isinstance(value, str):
            return clean_number(value)
        return value

    @field_validator("quantity", mode="before")
    def parse_int(cls, value):
        if isinstance(value, str):
            return clean_int(value)
        return value


class TotalAmount(BaseModel):
    taxable_amount: float
    igst: float
    round_off: float
    tcs: float
    total: float

    @field_validator(
        "taxable_amount", "igst", "round_off", "tcs", "total", mode="before"
    )
    def parse_float(cls, value):
        """Convert comma-separated string to float."""
        if isinstance(value, str):
            return clean_number(value)
        return value


class InvoiceDetails(BaseModel):
    customer_details: CustomerDetails
    items: list[Item]
    total_amount: TotalAmount
