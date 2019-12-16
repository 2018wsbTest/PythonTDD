"""
Rozwiąż zadanie
Wykorzystując paradygmaty programowania obiektowego napisz program który będzie pozwalał na obliczanie pół i objętości figur płaskich oraz wielościanów.
* trójkąt
* kwadrat
* prostokąt
* sześcian
* ostrosłup foremny
* owal
"""

import math


class SurfaceArea():

    def __init__(self, basis):
        self.basis = basis
        self.height = 0
        self.side = 0

    def triangle_surface_area(self, height):
        self.height = height
        return 0.5*self.basis*self.height

    def aquare_sourface_area(self):
        return self.basis**2

    def rectangle_sourface_area(self, side):
        self.side = side
        return self.side*self.basis

    def cube_sourface_area(self):
        return (self.basis**2)*6

    def oval_sourface_area(self, side):
        self.side = side
        return math.pi*self.side*self.basis

    def tetrahedron_sourface_area(self):
        return (self.basis**2)*math.sqrt(3)


class Volume(SurfaceArea):
    def __init__(self, basis):
        super().__init__(basis)

    def cube_volume(self):
        return self.basis**3

    def tetrahedron_volume(self):
        return ((self.basis**3)*math.sqrt(2))/12


# area = SurfaceArea(3)
# print(f"pole trójkąta: {area.triangle_surface_area(4):.2f}")
# print(f"pole kwadratu: {area.aquare_sourface_area():.2f}")
# print(f"pole prostokąta: {area.rectangle_sourface_area(12):.2f}")
# print(f"pole powierzchni ścian sześcianu: {area.cube_sourface_area():.2f}")
# print(f"Pole powierzchni owalu: {area.oval_sourface_area(10):.2f}")
# print(f"pole powierzchni ścian czworościanu foremnego: {area.tetrahedron_sourface_area():.2f}")
#
# volume = Volume(4)
# print(f"objętość sześcianu: {volume.cube_volume():.2f}")
# print(f"objętość czworościanu foremnego: {volume.tetrahedron_volume():.2f}")

def main():
    area = SurfaceArea(3)
    print(f"pole trójkąta: {area.triangle_surface_area(4):.2f}")
    print(f"pole kwadratu: {area.aquare_sourface_area():.2f}")
    print(f"pole prostokąta: {area.rectangle_sourface_area(12):.2f}")
    print(f"pole powierzchni ścian sześcianu: {area.cube_sourface_area():.2f}")
    print(f"Pole powierzchni owalu: {area.oval_sourface_area(10):.2f}")
    print(f"pole powierzchni ścian czworościanu foremnego: {area.tetrahedron_sourface_area():.2f}")
    print(f"pole powierzchni ścian czworościanu foremnego: {SurfaceArea(9).tetrahedron_sourface_area():.2f}")

    volume = Volume(4)
    print(f"objętość sześcianu: {volume.cube_volume():.2f}")
    print(f"objętość czworościanu foremnego: {volume.tetrahedron_volume():.2f}")
    print(Volume(2).cube_volume())
    print(Volume(2).tetrahedron_volume())


#main()

