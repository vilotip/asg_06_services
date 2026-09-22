#!/usr/bin/env python

import rospy
from math import pi
from ros_102_services.srv import xSquare
from ros_102_services.srv import circArea, circAreaResponse

def callback(request):
    r_square = client(request.r)
    response = circAreaResponse()
    response.circArea = pi*r_square
    return response

def circArea_server():
    service = rospy.Service('circArea', circArea, callback)
    rospy.spin()

def client(r):
    rospy.wait_for_service('x_square')
    try:
        service = rospy.ServiceProxy('x_square',xSquare)
        response = service(r)
        return response.x_square
    except rospy.ServiceException as e:
        print('I failed finding the service')

if __name__ == "__main__":
    rospy.init_node('calc_area_circle')
    #r = float(input('Enter radius: '))
    circArea_server()
    #print('Area = %.2f'%(circle_area))
