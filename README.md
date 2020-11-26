# Pose Graph Optimization 
Done as part of Mobile Robotics course project at IIIT Hyderabad, fall 2020.
## Introduction
In a 2D world, a robot has 3 degrees of freedom, i.e. its pose in the world can be expressed by the state vector
. For the scope of this project, we are interested only in the robot's trajectory through the
world, and NOT in distinct landmarks or the surronding map of the environment, i.e. we are only interested in
"L"ocalization part of SLAM.
 Therefore, we can represent it as a graph where the vertices represent robot poses
and edges represent the spatial constraints between these poses. Such a map is generally called a pose graph.
wo different kinds of constraints are necessary for pose graph SLAM. The first are odometric constraints that
connect two successive states  via a motion model. Furthermore, in order to perform loop closing,
the robot has to recognize places it already visited before. This place recognition is also a part of the front-end
and provides the second type of constraint, the loop closure constraints. These constraints connect two not
necessarily successive poses.

## Contents
## Pose Graph Optimization for 1D SLAM 
* From scratch
* Using g2o and jax
## Pose Graph Optimization for 2D SLAM
* From scratch
* Using g2o and jax
## Derivation of Motion model geometrically


