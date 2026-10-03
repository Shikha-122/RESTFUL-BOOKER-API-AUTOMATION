import requests
from utils.logger import get_logger

class APIClient:
    logger = get_logger(__name__)

    def __init__(self,base_url):
        self.base_url=base_url

    def get(self, endpoint, **kwargs):
        self.logger.info(f"GET request: {endpoint}")

        response = requests.get(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        self.logger.info(f"Response status: {response.status_code}")

        return response

    def post(self, endpoint, **kwargs):
        self.logger.info(f"POST request: {endpoint}")

        response = requests.post(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        self.logger.info(f"Response status: {response.status_code}")

        return response

    def put(self, endpoint, **kwargs):
        self.logger.info(f"PUT request: {endpoint}")

        response = requests.put(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        self.logger.info(f"Response status: {response.status_code}")

        return response

    def patch(self,endpoint,**kwargs):
        return requests.patch(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

    def delete(self, endpoint, **kwargs):
        self.logger.info(f"DELETE request: {endpoint}")

        response = requests.delete(
            f"{self.base_url}{endpoint}",
            **kwargs
        )

        self.logger.info(f"Response status: {response.status_code}")

        return response