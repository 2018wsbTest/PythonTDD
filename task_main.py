import task


def main():
    area = task.SurfaceArea(3)
    print(f"pole trójkąta: {area.triangle_surface_area(4):.2f}")
    print(f"pole kwadratu: {area.aquare_sourface_area():.2f}")
    print(f"pole prostokąta: {area.rectangle_sourface_area(12):.2f}")
    print(f"pole powierzchni ścian sześcianu: {area.cube_sourface_area():.2f}")
    print(f"Pole powierzchni owalu: {area.oval_sourface_area(10):.2f}")
    print(f"pole powierzchni ścian czworościanu foremnego: {area.tetrahedron_sourface_area():.2f}")
    print(f"pole powierzchni ścian czworościanu foremnego: {task.SurfaceArea(9).tetrahedron_sourface_area():.2f}")

    volume = task.Volume(4)
    print(f"objętość sześcianu: {volume.cube_volume():.2f}")
    print(f"objętość czworościanu foremnego: {volume.tetrahedron_volume():.2f}")
    print(task.Volume(2).cube_volume())
    print(task.Volume(2).tetrahedron_volume())
#
main()
print("\n=====================\n")
task.main()
