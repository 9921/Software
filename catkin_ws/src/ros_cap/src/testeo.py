#!/usr/bin/env python

import rospy #importar ros para python
from std_msgs.msg import String, Int32 # importar mensajes de ROS tipo String y tipo Int32
from geometry_msgs.msg import Twist # importar mensajes de ROS tipo geometry / Twist
from sensor_msgs.msg import Joy
from duckietown_msgs.msg import Twist2DStamped #mensajes
import cosa # donde se detectan los gestos


class Template(object):
	def __init__(self, args):
		super(Template, self).__init__()
		self.args = args
		self.publisher = rospy.Publisher('/duckiebot/wheels_driver_node/car_cmd', Twist2DStamped, queue_size = 1)
		self.subscriber = rospy.Subscriber('/duckiebot/joy', Joy, self.callback)
		self.twist = Twist2DStamped()
		
		

	def callback(self,joy):
		joy.buttons
		accion = cosa.prediccion()

		if accion == 'Atrás':
			rospy.loginfo("atras")
			self.twist.v = -8
		elif accion == 'Derecha':
			rospy.loginfo("derecha")
			self.twist.omega = 150
			self.twist.v= 8
		elif accion == 'Izquierda':
			rospy.loginfo("izquierda")
			self.twist.omega = -150
			self.twist.v=8
		elif accion == 'Adelante':
			rospy.loginfo("adelante")
			self.twist.v = 8
		else: 
			self.twist.v = 0
			self.twist.omega = 0
		self.publisher.publish(self.twist)
		rospy.sleep(1)

			



def main():
	rospy.init_node('test') #creacion y registro del nodo!

	obj = Template('args') # Crea un objeto del tipo Template, cuya definicion se encuentra arriba

	#objeto.publicar() #llama al metodo publicar del objeto obj de tipo Template

	rospy.spin() #funcion de ROS que evita que el programa termine -  se debe usar en  Subscribers


if __name__ =='__main__':
	main()


