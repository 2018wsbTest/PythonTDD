import unittest
import task


class TestStringMethods(unittest.TestCase):
    def test_triangle_surface_area(self):
        area = task.SurfaceArea(3).triangle_surface_area(4)
        self.assertEqual(area, 6)

    def test_aquare_sourface_area(self):
        area = task.SurfaceArea(4).aquare_sourface_area()
        self.assertEqual(area, 16)

    def test_rectangle_sourface_area(self):
        area = task.SurfaceArea(5).rectangle_sourface_area(3)
        self.assertEqual(area, 15)

    def test_cube_sourface_area(self):
        area = task.SurfaceArea(5).cube_sourface_area()
        self.assertEqual(area, 150)

    def test_oval_sourface_area(self):
        area = task.SurfaceArea(3).oval_sourface_area(10)
        self.assertEqual(area, 94.24777960769379)

    def test_tetrahedron_sourface_area(self):
        area = task.SurfaceArea(3).tetrahedron_sourface_area()
        self.assertEqual(area, 15.588457268119894)

    def test_cube_volume(self):
        volume = task.Volume(4).cube_volume()
        self.assertEqual(volume, 64)

    def test_tetrahedron_volume(self):
        volume = task.Volume(4).tetrahedron_volume()
        self.assertEqual(volume, 7.542472332656508)


if __name__ == '__main__':
    unittest.main()

