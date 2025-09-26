import numpy as np
import math

class Rett:
  def __init__(self, vertA, vertB, vertC, vertD, angle):
    self.vertA = vertA
    self.vertB = vertB
    self.vertC = vertC
    self.vertD = vertD
    self.angle = angle


def rotate(fig, angle):
  #angle in radiants
  radGrad =(angle/360)*2*math.pi;

  #find barycenter
  barycenter_x = (fig.vertA[0] + fig.vertB[0] + fig.vertC[0] + fig.vertD[0])/4;
  barycenter_y = (fig.vertA[1] + fig.vertB[1] + fig.vertC[1] + fig.vertD[1])/4;

  #compute rotation
  Ax = (fig.vertA[0]-barycenter_x)* math.cos(radGrad) - (fig.vertA[1]-barycenter_y)*math.sin(radGrad) + barycenter_x
  Ay = (fig.vertA[0]-barycenter_x)* math.sin(radGrad) + (fig.vertA[1]-barycenter_y)*math.cos(radGrad) + barycenter_y

  Bx = (fig.vertB[0]-barycenter_x)* math.cos(radGrad) - (fig.vertB[1]-barycenter_y)*math.sin(radGrad) + barycenter_x
  By = (fig.vertB[0]-barycenter_x)* math.sin(radGrad) + (fig.vertB[1]-barycenter_y)*math.cos(radGrad) + barycenter_y

  Cx = (fig.vertC[0]-barycenter_x)* math.cos(radGrad) - (fig.vertC[1]-barycenter_y)*math.sin(radGrad) + barycenter_x
  Cy = (fig.vertC[0]-barycenter_x)* math.sin(radGrad) + (fig.vertC[1]-barycenter_y)*math.cos(radGrad) + barycenter_y

  Dx = (fig.vertD[0]-barycenter_x)* math.cos(radGrad) - (fig.vertD[1]-barycenter_y)*math.sin(radGrad) + barycenter_x
  Dy = (fig.vertD[0]-barycenter_x)* math.sin(radGrad) + (fig.vertD[1]-barycenter_y)*math.cos(radGrad) + barycenter_y

  return Rett(np.array([Ax,Ay]), np.array([Bx,By]), np.array([Cx,Cy]), np.array([Dx,Dy]),angle)



def compensateToolDiameter(fig, toolRadius):
  #transform to polar coordinates
  ro = math.sqrt((toolRadius*toolRadius)+(toolRadius*toolRadius))
  angRot_A = ((315+fig.angle)/360)*2*math.pi;
  Ax = fig.vertA[0] + ro*math.cos(angRot_A)
  Ay = fig.vertA[1] + ro*math.sin(angRot_A)

  angRot_B = ((225+fig.angle)/360)*2*math.pi;
  Bx = fig.vertB[0] + ro*math.cos(angRot_B)
  By = fig.vertB[1] + ro*math.sin(angRot_B)

  angRot_C = ((135+fig.angle)/360)*2*math.pi;
  Cx = fig.vertC[0] + ro*math.cos(angRot_C)
  Cy = fig.vertC[1] + ro*math.sin(angRot_C)

  angRot_D = ((45+fig.angle)/360)*2*math.pi;
  Dx = fig.vertD[0] + ro*math.cos(angRot_D)
  Dy = fig.vertD[1] + ro*math.sin(angRot_D)

  return Rett(np.array([Ax,Ay]), np.array([Bx,By]), np.array([Cx,Cy]), np.array([Dx,Dy]),fig.angle)



def printFig(fig):
  print("Vertex A = ", fig.vertA[0]," ; ", fig.vertA[1])
  print("Vertex B = ", fig.vertB[0]," ; ", fig.vertB[1])
  print("Vertex C = ", fig.vertC[0]," ; ", fig.vertC[1])
  print("Vertex D = ", fig.vertD[0]," ; ", fig.vertD[1])
  print("\n")



#A vertex
Ax=300
Ay =525

#B vertex
Bx= 400
By = 525

#C vertex
Cx = 400
Cy = 475

#D vertex
Dx = 300
Dy = 475

fig_0 = Rett(np.array([Ax,Ay]), np.array([Bx,By]), np.array([Cx,Cy]), np.array([Dx,Dy]),0)

printFig(rotate(fig_0,45))

fig_45 = compensateToolDiameter(rotate(fig_0,45),3)

printFig(fig_45)

