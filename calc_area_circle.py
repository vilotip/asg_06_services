#!/usr/bin/env python

import rospy
from math import pi
from ros_102_services.srv import xSquare
from ros_102_services.srv import circArea, circAreaResponse

def client(r):
    rospy.wait_for_service('x_squarer_server')
    try:
        service = rospy.ServiceProxy('x_squarer_server',xSquare) #rospy.Service('service_name',srv file)
        response = service(r) 				   #passing request
        return response.response_x_square			   #receive response
    except rospy.ServiceException as e:
        print('I failed finding the service')

def callback(request):
    response = circAreaResponse()
    response.response_circArea = pi*client(request.request_r)   #gets r**2 from x_squarer_server
    return response

def circArea_server():
    service = rospy.Service('circArea_server', circArea, callback)  #starting rospy.Service('service_name',srv file)
    rospy.spin()

if __name__ == "__main__":
    rospy.init_node('calc_area_circle_client_server')
    #r = float(input('Enter radius: '))
    #answer=client(r)
    #circle_area = pi*answer					#client calculates circle_area
    #print('Area = %.2f'%(circle_area))
    circArea_server()
    
