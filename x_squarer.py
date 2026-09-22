#!/usr/bin/env python

import rospy
from ros_102_services.srv import xSquare, xSquareResponse

def callback(request):
    response = xSquareResponse()
    response.x_square = request.x*request.x
    return response

def x_square_server():
    rospy.init_node('x_square_server')
    service = rospy.Service('x_square', xSquare, callback)
    rospy.spin()

if __name__ == "__main__":
    x_square_server()
