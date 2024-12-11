
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as lin
import argparse
from matplotlib.animation import FuncAnimation

class FDM_Solver_2D_SteadyFlow:
    def __init__(self, Nx, Ny, boundary_cond:dict):
        self.Nx = Nx
        self.Ny = Ny
        self.boundary_cond=boundary_cond
        self.A,self.B=None,None
 
    def buildCoeffMatrix(self):
        Ddiag = -4 * np.eye(self.Nx - 1) ;  Dupper = np.diag([1] * (self.Nx - 2), 1) ; Dlower = np.diag([1] * (self.Nx - 2), -1)
        D = Ddiag + Dupper + Dlower
        Ds = [D] * (self.Nx - 1)
        coef_matrix = lin.block_diag(*Ds)
        I = np.ones((self.Nx - 1) * (self.Nx - 2))
        Iupper = np.diag(I, self.Nx - 1)
        Ilower = np.diag(I, -self.Nx + 1)
        coef_matrix += Iupper + Ilower
        return coef_matrix

    def buildRHSVector(self):
        b1=np.zeros((self.Nx-1,self.Ny-1))
        b2=np.zeros((self.Nx-1,self.Ny-1))
        b1[0,:]=self.boundary_cond['top']
        b1[-1,:]=self.boundary_cond['buttom']
        b2[:,0]=self.boundary_cond['left']
        b2[:,-1]=self.boundary_cond['right']
        b=b1+b2
        b=np.flip(b,axis=0)
        b=0 -(b.flatten()) 
        return b

    def solveLinearSystem(self, A, b):
        t = lin.solve(A, b)
        t= t.reshape((self.Nx - 1, self.Ny - 1))
        t=np.flip(t,axis=0)
        t2d=np.zeros((self.Nx+1,self.Ny+1))
        t2d[0,:]=self.boundary_cond['top']
        t2d[-1,:]=self.boundary_cond['buttom']
        t2d[:,0]=self.boundary_cond['left']
        t2d[:,-1]=self.boundary_cond['right']
        t2d[1:-1,1:-1]=t
        return t,t2d
    
    def plot(self,t):
        t2d=np.zeros((self.Nx+1,self.Ny+1))
        t2d[0,:]=self.boundary_cond['top']
        t2d[-1,:]=self.boundary_cond['buttom']
        t2d[:,0]=self.boundary_cond['left']
        t2d[:,-1]=self.boundary_cond['right']
        t2d[1:-1,1:-1]=t
        
        fig = plt.figure(1,figsize=(30,30))
        ax=fig.add_subplot(1,1,1)
        
        im=ax.imshow(t2d,cmap='jet')
        ax.set_xlabel('x(m)')
        ax.set_ylabel('y(m)')
        ax.set_title('Temperature Distribution for 2d steady flow')
        #plt.axis('off')
        plt.colorbar(im,ax=ax,label='Color Mapping')
       
        plt.show()
        
        return t2d
    
    def create_frame(self,step,ax):
        for cond in list(self.boundary_cond.keys()):
            self.boundary_cond[cond]=int(self.boundary_cond[cond])*np.cos(step)
        # print(self.boundary_cond)
        fdm = FDM_Solver_2D_SteadyFlow(Nx=self.Nx, Ny=self.Ny, boundary_cond=self.boundary_cond)
        A = fdm.buildCoeffMatrix()
        b = fdm.buildRHSVector()
        t , t2d= fdm.solveLinearSystem(A, b)
        ax.cla()
        image=ax.imshow(t2d,cmap='jet')
        
        return image
        
    def animate(self):
        fig = plt.figure()
        ax = fig.gca()
        animation = FuncAnimation(fig, self.create_frame, frames=10, fargs=(ax,))
        animation.save('animation.mp4', writer='ffmpeg', fps=1)




if __name__ == "__main__":
    
    class ParseDict(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):

            d = getattr(namespace, self.dest) or {}

            if values:
                if type(values) is not list:
                    values=[values]
                for item in values:
                    split_items = item.split("=")
                    key = split_items[
                        0
                    ].strip()  # we remove blanks around keys, as is logical
                    # print(split_items)
                    value = split_items[1]

                    d[key] = value

            setattr(namespace, self.dest, d)
            
    parser = argparse.ArgumentParser()
    parser.add_argument("--Nx",type=int)
    parser.add_argument("--Ny",type=int)
    parser.add_argument('--Bc',action=ParseDict,metavar="KEY=VALUE",nargs="+")
    parser.add_argument('--plot',type=bool)
    parser.add_argument('--animate',type=bool)
    
    args = parser.parse_args()
    Nx=args.Nx
    Ny=args.Ny
    boundary_cond=args.Bc
    if boundary_cond is None:
        raise ValueError('You have to specify the boundary_condition')
    resources_per_worker={k:int(v) for k,v in zip(list(boundary_cond.keys()),list(boundary_cond.values()))}
    plot=args.plot
    animate=args.animate
    
    fdm = FDM_Solver_2D_SteadyFlow(Nx=Nx, Ny=Ny, boundary_cond=boundary_cond)
    A = fdm.buildCoeffMatrix()
    b = fdm.buildRHSVector()
    t ,t2d= fdm.solveLinearSystem(A, b)
    
    if animate:
        fdm.animate()
    
    del A,b
    if plot:
        plot=fdm.plot(t)
    
    
        
        