import vtkplotlib as vpl
from stl.mesh import Mesh

# TODO: Slice by layer
def meshFullSTL():
    path = vpl.data.get_rabbit_stl()

    mesh = Mesh.from_file(path)

    vpl.mesh_plot(mesh)
    vpl.show()

if __name__ == '__main__':
    meshFullSTL()
