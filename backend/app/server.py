from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.models.tax import STATES

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.post("/calculate/")
async def calculate_total_order_price(
        request: Request,
        product_quantity: int = Form(...),
        price: str = Form(...),
        state_code: str = Form(...),
):
    errors = []
    if product_quantity <= 0:
        errors.append("quantity should > 0")

    if state_code not in STATES:
        errors.append("write correct US state")

    try:
        price = Decimal(price)
    except InvalidOperation:
        errors.append("write correct price")

    if errors:
        return templates.TemplateResponse(
            "index.html",
            context={
                "request": request,
                "errors": errors,
                "price": price,
                "state_code": state_code,
                "product_quantity": product_quantity,
            },
        )

    price_calculator = Calculator(state_code, product_quantity, price)
    return templates.TemplateResponse(
        "index.html",
        context={
            "request": request,
            "total_order_price": price_calculator.calculate_total_order_price(),
            "price": price,
            "state_code": state_code,
            "product_quantity": product_quantity,
        },
    )


@app.get("/calculate/")
async def get_index_page(request: Request):
    return templates.TemplateResponse("index.html", context={"request": request})
