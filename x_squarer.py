#!/usr/bin/env python

import rospy
from ros_102_services.srv import xSquare, xSquareResponse

def callback(request):
    response = xSquareResponse()
    response.response_x_square = request.request_x*request.request_x
    return response

def x_squarer_server():
    service = rospy.Service('x_squarer_server', xSquare, callback) #starting rospy.Service('service_name',srv file)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('x_squarer_server')
    x_squarer_server()
