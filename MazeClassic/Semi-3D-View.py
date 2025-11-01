import math

class voxel:
  def __init__(self, vpx, vpy):
    self.vpx = vpx
    self.vpy = vpy

MapExample = [voxel(0,2), voxel(1,2), voxel(-1,1)]

class Rays:
  def __init__(self, rpx, rpy, slope, steps):
    self.rpx = rpx
    self.rpy = rpy
    self.slope = slope
    self.steps = steps

  #y = slope(x-rpx) + rpy
  def PutVertices(self):
    vertices = []
    for _ in range(self.steps):
      vertices.append(((self.rpx + _), (self.slope*(self.rpx + _) + self.rpy)))
    return vertices

TestRay = Rays(0, 0, 3, 5)
print(TestRay.PutVertices())

