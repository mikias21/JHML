class(volcano)
#
# [1] "matrix"

dim(volcano)
#
# [1] 87 61

typeof(volcano)
#
# [1] "double"

library(rgl)

#
# volcano is a matrix that stores z values. Make this
# fact more explicit:
#
z <- volcano

#
# Two vectors that contain the «meters» from the zero point.
# A cell in the grid is 10x10 meters, so we need to multiply
# the vectors by 10:
#
x <- 10 * (1:nrow(z)) # Should that not be ncol?
y <- 10 * (1:ncol(z)) # Should that not be nrow?

z_min = min(z)

z_diff = max(z) - z_min + 1

height_to_color <- terrain.colors(z_diff)

colors <- height_to_color[ z - z_min + 1 ];

open3d() # rgl.open()
# rgl.bg(color='white');
par3d(windowRect=c(34, 57, 727, 707))
surface3d(x, y, z, color=colors); # rgl.surface


view3d(
  userMatrix = matrix(
    c(
      0.972062767 , -0.1212740 , -0.2009648 , 0 ,
      0.234625295 ,  0.4775052 ,  0.8467230 , 0 ,
      -0.006723508 , -0.8702192 ,  0.4926187 , 0 ,
      0.000000000 ,  0.0000000 ,  0.0000000 , 1
    ),
    nrow  = 4,
    byrow = TRUE
  )
)

# rgl.bringtotop()


# Reduce the resolution
Volcano <- volcano[seq(1, nrow(volcano), by = 3),
                   seq(1, ncol(volcano), by = 3)]


par(mfrow = c(3, 3), mar = c(2, 2, 2, 2))
persp(Volcano)
persp(Volcano, theta = 40, phi = 40, col = "gold", border = NA, shade = 0.5)
persp3D(z = Volcano, clab = "m")
persp3D(z = Volcano, clab = "m", shade = 0.2)
persp3D(z = Volcano, facets = FALSE)
persp3D(z = Volcano, facets = FALSE, curtain = TRUE)
persp3D(z = Volcano, col = "white", shade = 0.5)
persp3D(z = Volcano, col = ramp.col(c("white", "black")), border = "black")
persp3D(z = Volcano, facets = FALSE, col = "darkblue")


par(mfrow = c(3, 3), mar = c(2, 2, 2, 2))
persp(Volcano)
persp(Volcano, theta = 40, phi = 40, col = "gold", border = NA, shade = 0.5)
persp3D(z = Volcano, clab = "m")
persp3D(z = Volcano, clab = "m", shade = 0.2)
persp3D(z = Volcano, facets = FALSE)
persp3D(z = Volcano, facets = FALSE, curtain = TRUE)
persp3D(z = Volcano, col = "white", shade = 0.5)
persp3D(z = Volcano, col = ramp.col(c("white", "black")), border = "black")
persp3D(z = Volcano, facets = FALSE, col = "darkblue")