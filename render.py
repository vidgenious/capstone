import vtkplotlib as vpl
from stl.mesh import Mesh

# TODO: Slice by layer
def meshFullSTL():
    # path = vpl.data.get_rabbit_stl()
    path = 'Gengar_-_mesh_fixed.stl'

    mesh = Mesh.from_file(path)

    vpl.mesh_plot(mesh)
    vpl.view(camera_direction=[-1, 1, 1])
    vpl.reset_camera()
    #vpl.show()
    vpl.save_fig("image.jpg", pixels=(600,600), off_screen=True)

    vpl.close()

if __name__ == '__main__':
    meshFullSTL()
