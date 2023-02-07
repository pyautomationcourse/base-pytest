from pages.base_page import send_request


class TestRequests:
    def test_get_request(self):
        """Test GET request"""
        url = "https://www.example.com"
        headers = {"Content-Type": "application/json"}
        params = {"key": "value"}
        response = send_request("GET", url, headers=headers, params=params)
        assert response.status_code == 200

    def test_post_request(self):
        """Test POST request"""
        url = "https://www.example.com"
        headers = {"Content-Type": "application/json"}
        body = {"key": "value"}
        response = send_request("POST", url, body=body, headers=headers)
        assert response.status_code == 201
