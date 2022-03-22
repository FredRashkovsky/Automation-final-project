import requests
import json



class booking_api_test:
    def __init__(self):
        self.url = "https://restful-booker.herokuapp.com/booking/"
        self.headers = {
            'Authorization': 'Basic YWRtaW46cGFzc3dvcmQxMjM=',
            'Content-Type': 'application/json' }


    def POST_Booking(self):
        payload = json.dumps({
        "firstname": "Fred",
        "lastname": "rash",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2022-02-01",
            "checkout": "2019-02-08"
        },
        "additionalneeds": "Breakfast"
        })
        
        response = json.loads(requests.request("POST", self.url, headers=self.headers, data=payload).text)
        self.url = self.url + str(response["bookingid"])
        return response


    def GET_Booking(self):
        return json.loads(requests.request("GET", self.url, headers=self.headers).text)
        

    def PATCH_Booking(self):
        payload = json.dumps({
            "bookingdates": {
            "checkin": '2022-02-01',
            "checkout": "2022-02-08" }})

        return json.loads(requests.request("PATCH", self.url, headers=self.headers, data=payload).text)
    
    def DELETE_Booking(self):
        return requests.request("DELETE", self.url, headers=self.headers).text



#test = booking_api_test()
#print(test.POST_Booking())
#print(test.GET_Booking())
#print(test.PATCH_Booking())
#print(test.DELETE_Booking())