import numpy as np

class animation:
    """Create an animation that holds keyframes"""
    def __init__(self, width=1920, height=1080, colorfunc=None):
        self.width, self.height = width, height #resolution of animation in pixels
        self.keyframes = [] #list of all keyframes

    def addKeyframe(self, keyframe):
        self.keyframes.append(keyframe)
        pass


class keyframe:
    """create a keyframe that holds data about the function, length, etc."""
    def __init__(self, min=(-1,-1), max=(1,1), function=lambda x:x, length = 60): 
        self.xmin, self.ymin = min # min and max should be a pair of reals, not an imaginry 
        self.xmax, self.ymax = max
        self.function = function
        self.length = length # the number of frames between this keyframe and the next
                             # [start,stop), except for last keyframe, which only renders its first frame
    
    def calculate(self, size=(1920,1080)):
        """calculate the values of the function"""

        print("╔══════════════════════════════")
        print("║  calculating...  ")
        print("║  xmin: " + str(self.xmin) + "; ymin: " + str(self.ymin))
        print("║  xmax: " + str(self.xmax) + "; ymax: " + str(self.ymax))
        print("║  function: " + str(self.function))

        # generate a 2d matrix of complex numbers
        real = np.linspace(self.xmin, self.xmax, size[0])
        complex = np.linspace(self.ymin, self.ymax, size[1])
        real, complex = np.meshgrid(real, complex)
        cplane = real + complex*1j
        
        # map function over the plane
        cplane = self.function(cplane)

        print(cplane)
        print("║  Done!")
        print("╚══════════════════════════════")
        
a = keyframe()
print("go")
for i in range(1000):
    a.calculate()
print("done!")