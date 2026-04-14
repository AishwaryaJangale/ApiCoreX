import pytest

class TestUsersAPI:

    @pytest.mark.smoke2
    def test_get_users(self, api_client):
        """Test retrieving a list of users."""
        response = api_client.get("/users?page=2")
        
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        
        data = response.json()
        assert "data" in data
        assert isinstance(data["data"], list)
        assert len(data["data"]) > 0

    @pytest.mark.smoke2
    @pytest.mark.parametrize("name, job", [
        ("Morphy", "leader"),
        ("Trinity", "developer")
    ])
    def test_create_user(self, api_client, name, job):
        """Test creating a new user with valid data."""
        payload = {
            "name": name,
            "job": job
        }
        response = api_client.post("/users", payload=payload)
        
        assert response.status_code == 201, f"Expected 201, got {response.status_code}"
        
        response_data = response.json()
        assert response_data["name"] == name
        assert response_data["job"] == job
        assert "id" in response_data
        assert "createdAt" in response_data
