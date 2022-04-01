import vtkplotlib as vpl
from stl.mesh import Mesh

# TODO: Slice by layer
def meshFullSTL():
    # a = import_stl("Gengar_-_mesh_fixed.stl")

    # # scad_render_to_file(a, "temp.scad")

    # # a = import_scad("temp.scad")

    # rotate

    # d = difference()(
    #     a,
    #     up(30)(back(50)(left(100)(cube(200))))
    # )    
    # print(type(cube(20)))
    # print(type(a))

    # rotate_extrude(180, 180, 180)(
    #     d
    # )

    # scad_render_to_file(d, "temp.scad")

    # # os.system("openscad {} -o {}".format("temp.scad", "result.stl"))
    # print("here")
    # # os.system("openscad -o result.stl temp.scad")
    # os.system("openscad --preview --imgsize=512,512 {} -o {}".format("temp.scad", "out.png"))

    # print("here")


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
