
import requests
import numpy

if __name__ == "__main__":

    # Use the requests library
    request = requests.get("https://httpbin.org/get")
    print "Response : "
    print request.text

    # Use the numpy library
    print "Numpy version : " + numpy.__version__

