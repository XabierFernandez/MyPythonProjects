from math import cos, sin, radians

a=-179.7232970

b=-0.2066000

c=0.8562000


w, h = 3, 3;
Matrix = [[0 for x in range(w)] for y in range(h)] 
c1 = cos(radians(a));
s1 = sin(radians(a))
c2 = cos(radians(b))
s2 = sin(radians(b))
c3 = cos(radians(c))
s3 = sin(radians(c))

Matrix[0][0] = c1 * c2
Matrix[0][1] = s1 * c3 + c1 * s2 * s3
Matrix[0][2] = s1 * s3 - c1 * s2 * c3

Matrix[1][0] = -s1 * c2
Matrix[1][1] = c1 * c3 - s1 * s2 * s3
Matrix[1][2] = c1 * s3 + s1 * s2 * c3

Matrix[2][0] = s2
Matrix[2][1] = -c2 * s3
Matrix[2][2] = c2 * c3

print(s1*s2)
print(-c1*s2)
print(-c3*s1 - c1*c2*s3)
print(-c1*s3 - c2*c3*s1)
print(-c3*s2)
print(s2*s3)

print(c3*s1*s2 - c1*s3)
print(s1*s3 - c1*c2*s2)
print(c1*s2*s3 - c3*s1)
print(-c2*s1)
print(-s2)
print(-c2*s3)



