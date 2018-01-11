call deactivate trees
conda remove --name trees --all
conda create --name trees python=3.5
call activate trees
conda install -c cogsci pygame
conda install pyopengl