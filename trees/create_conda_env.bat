call deactivate trees
conda remove --name trees --all
conda create --name trees python=3.6.1
call activate trees
#conda install -c cogsci pygame
pip install pygame
#conda install pyopengl 
pip install pyopengl
conda install numpy