import pytest
from utils.config import API_BASE_URL

@pytest.mark.api
def test_api_get_status_200(api_request):
    response = api_request.get(f"{API_BASE_URL}/status/200")
    assert response.status == 200

@pytest.mark.api
def test_api_get_json(api_request):
    response = api_request.get(f"{API_BASE_URL}/json")
    assert response.status == 200
    data = response.json()
    assert "slideshow" in data