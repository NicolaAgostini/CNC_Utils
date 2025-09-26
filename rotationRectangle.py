import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class Rett:
  def __init__(self, vertA, vertB, vertC, vertD, angle=0, MAB = np.array([]), MBA = np.array([]), MBC=np.array([]), MCB=np.array([]), MCD = np.array([]), MDC = np.array([]), MDA=np.array([]), MAD=np.array([])):
    self.vertA = vertA
    self.vertB = vertB
    self.vertC = vertC
    self.vertD = vertD
    self.angle = angle
    self.MAB = MAB
    self.MBA = MBA
    self.MBC = MBC
    self.MCB = MCB
    self.MCD = MCD
    self.MDC = MDC
    self.MDA = MDA
    self.MAD = MAD



def rotate(fig, angle):
  #angle in radiants
  radGrad =(angle/360)*2*math.pi

  #find barycenter
  barycenter_x = (fig.vertA[0] + fig.vertB[0] + fig.vertC[0] + fig.vertD[0])/4
  barycenter_y = (fig.vertA[1] + fig.vertB[1] + fig.vertC[1] + fig.vertD[1])/4

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
  angRot_A = ((315+fig.angle)/360)*2*math.pi
  Ax = fig.vertA[0] + ro*math.cos(angRot_A)
  Ay = fig.vertA[1] + ro*math.sin(angRot_A)

  angRot_B = ((225+fig.angle)/360)*2*math.pi
  Bx = fig.vertB[0] + ro*math.cos(angRot_B)
  By = fig.vertB[1] + ro*math.sin(angRot_B)

  angRot_C = ((135+fig.angle)/360)*2*math.pi
  Cx = fig.vertC[0] + ro*math.cos(angRot_C)
  Cy = fig.vertC[1] + ro*math.sin(angRot_C)

  angRot_D = ((45+fig.angle)/360)*2*math.pi
  Dx = fig.vertD[0] + ro*math.cos(angRot_D)
  Dy = fig.vertD[1] + ro*math.sin(angRot_D)

  return Rett(np.array([Ax,Ay]), np.array([Bx,By]), np.array([Cx,Cy]), np.array([Dx,Dy]),fig.angle)



def printFig(fig):
    print("Vertex A = ", fig.vertA[0]," ; ", fig.vertA[1])
    print("Vertex B = ", fig.vertB[0]," ; ", fig.vertB[1])
    print("Vertex C = ", fig.vertC[0]," ; ", fig.vertC[1])
    print("Vertex D = ", fig.vertD[0]," ; ", fig.vertD[1])
    print("\n")


    if (fig.MAB.size != 0):
        print("MAB = ", fig.MAB[0]," ; ", fig.MAB[1])
        print("MBA = ", fig.MBA[0]," ; ", fig.MBA[1])
        print("MBC = ", fig.MBC[0]," ; ", fig.MBC[1])
        print("MCB = ", fig.MCB[0]," ; ", fig.MCB[1])
        print("MCD = ", fig.MCD[0]," ; ", fig.MCD[1])
        print("MDC = ", fig.MDC[0]," ; ", fig.MDC[1])
        print("MDA = ", fig.MDA[0]," ; ", fig.MDA[1])
        print("MAD = ", fig.MAD[0]," ; ", fig.MAD[1])

    figMat, ax = plt.subplots()

    heigth = twoPointsDistance(fig.vertB, fig.vertC)
    width = twoPointsDistance(fig.vertA, fig.vertB)

    rect = Rectangle((fig.vertD[0], fig.vertD[1]), width, heigth,
            angle=fig.angle,
            edgecolor='blue',
            facecolor='yellow',
            lw=1)

    ax.add_patch(rect)

    # plot all the vertex
    ax.plot(fig.vertA[0], fig.vertA[1], 'ro')
    ax.text(fig.vertA[0], fig.vertA[1], '({0:.2f}, {1:.2f})'.format(fig.vertA[0],fig.vertA[1]))

    ax.plot(fig.vertB[0], fig.vertB[1], 'ro')
    ax.text(fig.vertB[0], fig.vertB[1], '({0:.2f}, {1:.2f})'.format(fig.vertB[0], fig.vertB[1]))

    ax.plot(fig.vertC[0], fig.vertC[1], 'ro')
    ax.text(fig.vertC[0], fig.vertC[1], '({0:.2f}, {1:.2f})'.format(fig.vertC[0], fig.vertC[1]))

    ax.plot(fig.vertD[0], fig.vertD[1], 'ro')
    ax.text(fig.vertD[0], fig.vertD[1], '({0:.2f}, {1:.2f})'.format(fig.vertD[0], fig.vertD[1]))

    # plot micro-joint
    if fig.MAB.size != 0:
        ax.plot(fig.MAB[0], fig.MAB[1], 'ro')
        ax.text(fig.MAB[0], fig.MAB[1], '(MAB = {0:.2f}, {1:.2f})'.format(fig.MAB[0], fig.MAB[1]))
    if fig.MBA.size != 0:
        ax.plot(fig.MBA[0], fig.MBA[1], 'ro')
        ax.text(fig.MBA[0], fig.MBA[1], '(MBA = {0:.2f}, {1:.2f})'.format(fig.MBA[0], fig.MBA[1]))
    if fig.MBC.size != 0:
        ax.plot(fig.MBC[0], fig.MBC[1], 'ro')
        ax.text(fig.MBC[0], fig.MBC[1], '(MBC = {0:.2f}, {1:.2f})'.format(fig.MBC[0], fig.MBC[1]))
    if fig.MCB.size != 0:
        ax.plot(fig.MCB[0], fig.MCB[1], 'ro')
        ax.text(fig.MCB[0], fig.MCB[1], '(MCB = {0:.2f}, {1:.2f})'.format(fig.MCB[0], fig.MCB[1]))
    if fig.MCD.size != 0:
        ax.plot(fig.MCD[0], fig.MCD[1], 'ro')
        ax.text(fig.MCD[0], fig.MCD[1], '(MCD = {0:.2f}, {1:.2f})'.format(fig.MCD[0], fig.MCD[1]))
    if fig.MDC.size != 0:
        ax.plot(fig.MDC[0], fig.MDC[1], 'ro')
        ax.text(fig.MDC[0], fig.MDC[1], '(MDC = {0:.2f}, {1:.2f})'.format(fig.MDC[0], fig.MDC[1]))
    if fig.MDA.size != 0:
        ax.plot(fig.MDA[0], fig.MDA[1], 'ro')
        ax.text(fig.MDA[0], fig.MDA[1], '(MDA = {0:.2f}, {1:.2f})'.format(fig.MDA[0], fig.MDA[1]))
    if fig.MAD.size != 0:
        ax.plot(fig.MAD[0], fig.MAD[1], 'ro')
        ax.text(fig.MAD[0], fig.MAD[1], '(MAD = {0:.2f}, {1:.2f})'.format(fig.MAD[0], fig.MAD[1]))


    # find barycenter
    barycenter_x = (fig.vertA[0] + fig.vertB[0] + fig.vertC[0] + fig.vertD[0]) / 4
    barycenter_y = (fig.vertA[1] + fig.vertB[1] + fig.vertC[1] + fig.vertD[1]) / 4

    # set plot limit
    padding = max(twoPointsDistance(fig.vertA, fig.vertB), twoPointsDistance(fig.vertB, fig.vertC)) * 3
    ax.set_xlim(barycenter_x - padding, barycenter_x + padding)
    ax.set_ylim(barycenter_y - padding, barycenter_y + padding)
    ax.set_aspect('equal')
    # display plot
    plt.show()



def computeMicrojoint(fig, toolRadius, microjoint):
    roMAB = twoPointsDistance(fig.vertA, fig.vertB)/2  - toolRadius - microjoint/2
    angRot_MAB = (fig.angle / 360) * 2 * math.pi

    MABx = fig.vertA[0] + roMAB * math.cos(angRot_MAB)
    MABy = fig.vertA[1] + roMAB * math.sin(angRot_MAB)

    roMBA = twoPointsDistance(fig.vertB, fig.vertA)/2  - toolRadius - microjoint/2
    angRot_MBA = ((180+fig.angle) / 360) * 2 * math.pi

    MBAx = fig.vertB[0] + roMBA * math.cos(angRot_MBA)
    MBAy = fig.vertB[1] + roMBA * math.sin(angRot_MBA)

    roMBC = twoPointsDistance(fig.vertB, fig.vertC)/2  - toolRadius - microjoint/2
    angRot_MBC = ((270+fig.angle) / 360) * 2 * math.pi

    MBCx = fig.vertB[0] + roMBC * math.cos(angRot_MBC)
    MBCy = fig.vertB[1] + roMBC * math.sin(angRot_MBC)

    roMCB = twoPointsDistance(fig.vertC, fig.vertB)/2  - toolRadius - microjoint/2
    angRot_MCB = ((90+fig.angle) / 360) * 2 * math.pi

    MCBx = fig.vertC[0] + roMCB * math.cos(angRot_MCB)
    MCBy = fig.vertC[1] + roMCB * math.sin(angRot_MCB)

    roMCD = twoPointsDistance(fig.vertC, fig.vertD)/2  - toolRadius - microjoint/2
    angRot_MCD = ((180+fig.angle) / 360) * 2 * math.pi

    MCDx = fig.vertC[0] + roMCD * math.cos(angRot_MCD)
    MCDy = fig.vertC[1] + roMCD * math.sin(angRot_MCD)

    roMDC = twoPointsDistance(fig.vertD, fig.vertC)/2  - toolRadius - microjoint/2
    angRot_MDC = (fig.angle / 360) * 2 * math.pi

    MDCx = fig.vertD[0] + roMDC * math.cos(angRot_MDC)
    MDCy = fig.vertD[1] + roMDC * math.sin(angRot_MDC)

    roMDA = twoPointsDistance(fig.vertD, fig.vertA)/2  - toolRadius - microjoint/2
    angRot_MDA = ((90+fig.angle) / 360) * 2 * math.pi

    MDAx = fig.vertD[0] + roMDA * math.cos(angRot_MDA)
    MDAy = fig.vertD[1] + roMDA * math.sin(angRot_MDA)

    roMAD = twoPointsDistance(fig.vertA, fig.vertD)/2  - toolRadius - microjoint/2
    angRot_MAD = ((270+fig.angle) / 360) * 2 * math.pi

    MADx = fig.vertA[0] + roMAD * math.cos(angRot_MAD)
    MADy = fig.vertA[1] + roMAD * math.sin(angRot_MAD)




    return Rett(fig.vertA, fig.vertB, fig.vertC, fig.vertD, fig.angle,np.array([MABx,MABy]), np.array([MBAx,MBAy]), np.array([MBCx,MBCy]), np.array([MCBx,MCBy]),np.array([MCDx,MCDy]), np.array([MDCx,MDCy]), np.array([MDAx,MDAy]), np.array([MADx,MADy]) )


def twoPointsDistance(A,B):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)


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

fig_0 = Rett(np.array([Ax,Ay]), np.array([Bx,By]), np.array([Cx,Cy]), np.array([Dx,Dy]))

printFig(rotate(fig_0,45)) # simple rotation by 45°

fig_45 = compensateToolDiameter(rotate(fig_0,45),3)

printFig(fig_45) # tool compensation

fig_45 = computeMicrojoint(fig_45, 3, 3)


printFig(fig_45) # micro-joint
