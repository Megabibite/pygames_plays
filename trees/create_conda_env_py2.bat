rem call deactivate treespy2
rem conda remove --name treespy2 --all
conda create --name treespy2 python=2.7
call activate treespy2
#conda install -c cogsci pygame
pip install pygame
#conda install pyopengl 
pip install pyopengl
conda install numpy