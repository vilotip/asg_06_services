#!/usr/bin/env python

import rospy
from math import pi
from ros_102_services.srv import circArea

def client(r):
    rospy.wait_for_service('circArea_server')
    try:
        service = rospy.ServiceProxy('circArea_server',circArea) 	#rospy.Service('service_name',srv file)
        response = service(r)						#passing request
        return response.response_circArea				#receive response
    except rospy.ServiceException as e:
        print('I failed finding the service')

if __name__ == "__main__":
    rospy.init_node('calc_vol_cylinder_client')
    r = float(input('Enter radius: '))
    h = float(input('Enter height: '))
    answer = client(r)					
    cylinder_vol = answer*h				#client calculates cylinder_volume
    print('Volume = %.2f'%(cylinder_vol))

