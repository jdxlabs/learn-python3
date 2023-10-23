
import requests
import numpy

if __name__ == "__main__":

    # Use the requests library
    request = requests.get("https://httpbin.org/get")
    print("Response : " + request.text[:200])

    # Use the numpy library
    print("Numpy version : " + numpy.__version__)

