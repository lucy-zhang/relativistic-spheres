import pytest
import spheres, numpy as np, numpy.testing as nptest

class TestSphereIntersection(object):
    def test_sphere_two_intersections(self):
        sphere = spheres.Sphere(1, None, None, None)
        intersection = sphere.detect_intersection(spheres.Ray(np.array([0, 3, 0, 0]),
                                                              np.array([0, 2, 0, 0])))
        nptest.assert_almost_equal(intersection, np.array([1, 0, 0]))

    def test_sphere_no_intersection(self):
        sphere = spheres.Sphere(1, None, None, None)
        intersection = sphere.detect_intersection(spheres.Ray(np.array([0, 2, 0, 0]),
                                                              np.array([0, 2, 1, 0])))
        assert intersection is None

    def test_ray_pointing_other_direction(self):
        sphere = spheres.Sphere(1, None, None, None)
        intersection = sphere.detect_intersection(spheres.Ray(np.array([0, 0, 2, 0]),
                                                              np.array([0, 0, 3, 0])))
        assert intersection is None

    def test_ray_starts_inside_sphere(self):
        sphere = spheres.Sphere(1, None, None, None)
        intersection = sphere.detect_intersection(spheres.Ray(np.array([0, 0, 0, 0]),
                                                              np.array([0, 0, 2, 0])))
        nptest.assert_almost_equal(intersection, np.array([0, 1, 0]))


class TestLorentzBoost(object):
    def test_identity(self):
        beta = np.array([0, 0, 0])
        nptest.assert_almost_equal(spheres.lorentz_boost(beta),
                                   np.array([[1, 0, 0, 0],
                                             [0, 1, 0, 0],
                                             [0, 0, 1, 0],
                                             [0, 0, 0, 1]]))

    def test_x_boost(self):
        beta = np.array([0.6, 0, 0])
        nptest.assert_almost_equal(spheres.lorentz_boost(beta),
                                   np.array([[1.25, -0.75, 0, 0],
                                             [-0.75, 1.25, 0, 0],
                                             [0, 0, 1, 0],
                                             [0, 0, 0, 1]]))

    def test_y_boost(self):
        beta = np.array([0, 0.6, 0])
        nptest.assert_almost_equal(spheres.lorentz_boost(beta),
                                   np.array([[1.25, 0, -0.75, 0],
                                             [0, 1, 0, 0],
                                             [-0.75, 0, 1.25, 0],
                                             [0, 0, 0, 1]]))

    def test_z_boost(self):
        beta = np.array([0, 0, 0.6])
        nptest.assert_almost_equal(spheres.lorentz_boost(beta),
                                   np.array([[1.25, 0, 0, -0.75],
                                             [0, 1, 0, 0],
                                             [0, 0, 1, 0],
                                             [-0.75, 0, 0, 1.25]]))

    def test_xyz_boost(self):
        beta = np.array([0.5, 0.5, 0.5])
        nptest.assert_almost_equal(spheres.lorentz_boost(beta),
                                   np.array([[2, -1, -1, -1],
                                             [-1, 4/3., 1/3., 1/3.],
                                             [-1, 1/3., 4/3., 1/3.],
                                             [-1, 1/3., 1/3., 4/3.]]))