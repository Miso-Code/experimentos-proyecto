from faker import Faker
from locust import HttpUser, task, constant

fake = Faker()


class WebsiteUser(HttpUser):
    wait_time = constant(20)

    @task
    def register(self):
        # Generate fake data for each request
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

        # self.client.post("/", json={
        #     "first_name": first_name,
        #     "last_name": last_name,
        #     "email": email,
        #     "password": password
        # })
        # self.client.get("/")
        # self.client.post("/user2", json={"name": first_name})
        self.client.request_name = "register"
        self.client.post("/mock/stream", json={
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password
        })
        # status = "Pending"
        # while status == "Pending":
        #     print("response pending")
        #     self.client.request_name = "status"
        #     response = self.client.get(f"/mock/{email}")
        #     message = response.json()["message"]
        #     if message == "Pending":
        #         self.wait()
        #     elif message == "User created":
        #         print("response created")
        #         status = "User created"
        #     else:
        #         print("response failed")
        #         raise Exception(f"Unexpected message: {message}")
        #     print(f"Status: {status}")
