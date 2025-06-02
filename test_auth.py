import pytest
from httpx import AsyncClient
from httpx import ASGITransport
from main import app  # adjust this if your FastAPI app is in a different file


@pytest.mark.asyncio
async def test_signup_and_signin():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        response = await ac.post("/user/signup", json={
            "email": "test@example.com",
            "password": "testpassword",
            "place": "testplace",
            "age": 20
        })
        assert response.status_code == 200
