import vtkplotlib as vpl
from stl.mesh import Mesh

# TODO: Slice by layer
def meshFullSTL():
    # path = vpl.data.get_rabbit_stl()
    path = 'Gengar_-_mesh_fixed.stl'

    mesh = Mesh.from_file(path)

    vpl.mesh_plot(mesh)
    vpl.view(camera_position=[160, 800, 400], focal_point=[0, 0, 0], up_view=[-1, -1, 1])
    #camera_position=[600, 600, 500]
    #, camera_direction=[0, -15, 1]
    #vpl.reset_camera()
    #vpl.show()
    vpl.save_fig("image.jpg", pixels=(600,600), off_screen=True)

    vpl.close()

if __name__ == '__main__':
    meshFullSTL()
