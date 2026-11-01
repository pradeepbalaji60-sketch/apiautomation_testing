import requests
def test_verify_app_status():
    #make the call to validate the API

    URL = "http://localhost:3050/api/health"
    response = requests.get(URL)

    #verify the status code
    status_code=response.status_code
    assert status_code==200, f"Expected status code 200, but received {status_code}"

#Verify the response body
    responsebody=response.json()

    assert responsebody["status"]== "ok", f"Expected status to be ok, but received {responsebody.status}"

def test_verify_demo_status():
    ""
    {
        "total_seeded_applications": 4,
        "status_counts": {
        "potential": 2,
        "applied": 1,
        "in_progress": 1,
        "final_stage": 0,
        "hired": 0,
        "rejected": 0,
        "withdrawn": 0,
        "total": 4
        }
    }
    ""
#make the call to validate the API
URL= "http://localhost:3050/api/v1/public/demo-stats"
response= requests.get(URL)
# Verify the status code

status_code=response.status_code
assert status_code==200

# Verify the response body

responsebody=response.json()

assert responsebody["total_seeded_applications"]==4
assert responsebody["status_counts"]["potential"]==1