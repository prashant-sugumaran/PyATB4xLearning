import allure
import pytest
import requests


@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Prashant")
@allure.testcase("TC#1")
@pytest.mark.crud
def test_create_booking_positive_tc1():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {

            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": 111,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"

    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200

    responseData = response.json()
    bookingid = responseData["bookingid"]
    assert bookingid is not None
    assert bookingid > 0
    assert type(bookingid) == int
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]

    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == False
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"
