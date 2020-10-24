import os
os.system("python ./misc/g2o_to_kitti.py ./dataset/gt.g2o ./dataset/gt.kitti")
os.system("python ./misc/g2o_to_kitti.py ./dataset/edges-poses.g2o ./dataset/edges-poses.kitti")
os.system("python ./misc/g2o_to_kitti.py ./dataset/sphere.g2o ./dataset/sphere.kitti")
os.system("python ./misc/g2o_to_kitti.py ./dataset/intel.g2o ./dataset/intel.kitti")
os.system("python ./misc/g2o_to_kitti.py ./opt_backup.g2o ./dataset/opt.kitti")
os.system("evo_rpe kitti ./dataset/gt.kitti ./dataset/opt.kitti -v --plot --plot_mode xy")
os.system("evo_ape kitti ./dataset/gt.kitti ./dataset/opt.kitti -v --plot --plot_mode xy")
os.system("evo_traj kitti ./dataset/gt.kitti ./dataset/opt.kitti -v --plot --plot_mode xy")