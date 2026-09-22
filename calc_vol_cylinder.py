#!/usr/bin/env python

import rospy
from math import pi
from ros_102_services.srv import circArea

def client(r):
    rospy.wait_for_service('circArea')
    try:
        service = rospy.ServiceProxy('circArea',circArea)
        response = service(r)
        return response.circArea
    except rospy.ServiceException as e:
        print('I failed finding the service')

if __name__ == "__main__":
    rospy.init_node('calc_vol_cylinder')
    r = float(input('Enter radius: '))
    h = float(input('Enter height: '))
    calc_area = client(r)
    cylinder_vol = calc_area*h
    print('Volume = %.2f'%(cylinder_vol))

