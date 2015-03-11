ang=30;
lc=0.01;
r=0.0125;
z=0.075;
Point(1) = {0, 0, 0, lc};
Point(2) = {r, 0, 0, lc};
Point(3) = {0, 0, r, lc};
Point(4) = {-r, 0, 0, lc};
Point(5) = {0, 0, -r, lc};
Circle(1) = {3, 1, 2};
Circle(2) = {2, 1, 5};
Circle(3) = {5, 1, 4};
Circle(4) = {4, 1, 3};
Line Loop(5) = {1, 2, 3, 4};
Plane Surface(6) = {5};
Extrude {0, z, 0} {
  Surface{6};
}
Physical Volume(29) = {1};
Mesh.Color.Points = {255,0,0};