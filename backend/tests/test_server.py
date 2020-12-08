import pytest
from httpx import AsyncClient
from bs4 import BeautifulSoup

from app.server import app


@pytest.mark.asyncio
async def test_get_index_page():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/calculate/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_calculate_total_order_price():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/calculate/", data={
            'product_quantity': 12,
            'price': 13,
            'state_code': 'UT',
        })
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.find(id='total_order_price')
    assert "Total order price: 166.6860" == result.get_text()


@pytest.mark.asyncio
async def test_calculate_total_order_price_with_wrong_params():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/calculate/", data={
            'product_quantity': 12,
            'price': 13,
            'state_code': 'UK',
        })
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, 'html.parser')
    all_errors = soup.findAll("li", {"class": "error"})
    assert 1 == len(all_errors)
    assert all_errors[0].get_text() == 'write correct US state'
