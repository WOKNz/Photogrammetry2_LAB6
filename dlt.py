import numpy as np
from scipy.spatial.transform import Rotation as R
import pandas as pd

class dlt():
	"""
	DLT module
	:param ground_points: Ground points
	:param picture_points: Picture points
	"""
	def __init__(self,ground_points, picture_points):
		self.ground_points = ground_points
		self.picture_points = picture_points
		pass

	@staticmethod
	def generatePicturePoints(f,xp,yp,omega,phi,kappa,X0,Y0,Z0,ground_points):
		"""

		:param f: Focal length (mm)
		:param xp: Camera center fix on axis x (micron)
		:param yp: Camera center fix on axis y (micron)
		:param omega: External rotation (rad)
		:param phi: External rotation (rad)
		:param kappa: External rotation (rad)
		:param X0: External location of the camera (m)
		:param Y0: External location of the camera (m)
		:param Z0: External location of the camera (m)
		:param ground_points: Ground points
		:return: Picture points
		:type f: float
		:type xp: float
		:type yp: float
		:type omega: float
		:type phi: float
		:type kappa: float
		:type X0: float
		:type Y0: float
		:type Z0: float
		:type ground_points: ndarray
		:rtype: ndarray
		"""




if __name__ == '__main__':

	r = np.array(R.from_euler('zyx', [60,45,-30], degrees=True).as_matrix())
	print('Rotation matrix\n',pd.DataFrame(r))

	c = np.array([[15],[10],[50]])
	print('\nCamera location\n',pd.DataFrame(c))

	k = np.array([[-153,0,0.2],
	              [0,-153,0.2],
	              [0,0,1]])
	print('\nK Matrix\n',pd.DataFrame(k))

	p = np.dot(np.dot(k,r),np.hstack((np.identity(3),-c)))
	print('\nP Matrix\n',pd.DataFrame(p))

	ground_box_points = np.array([[-5,-5,-5],
	                              [-5,5,-5],
	                              [5,5,-5],
	                              [5,-5,-5],
	                              [-5,-5,5],
	                              [-5,5,5],
	                              [5,5,5],
	                              [5,-5,5]])

	ground_box_points = np.vstack((ground_box_points.T,np.ones((1,ground_box_points.shape[0]))))
	print('\nGround points of the box\n',pd.DataFrame(ground_box_points))

	picture_box_points = np.dot(p,ground_box_points)
	print('\nPicture points of the box (x,y,w)\n',pd.DataFrame(picture_box_points.T))
