ls
ls ~
mkdir ~/.ssh
cd ~/.ssh
touch authorized_keys
cat ~/hello.pub>authorized_keys
logout
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
logout
conda --version
rm Miniconda3-latest-Linux-x86_64.sh
pip install jupyter
conda create --name py3_study python=3.7
conda activate py3_study
pip install ipykernel numpy matplotlib scikit-learn pandas tabulate tqdm
python -m ipykernel install --name py3_study --display-name "Py3 study" --user
python
touch run_jupyter.sh
echo "jupyter notebook --no-browser --port 8001 --ip 0.0.0.0">run_jupyter.sh
chmod +x run_jupyter.sh
echo "jupyter notebook --no-browser --port 8069 --ip 0.0.0.0">run_jupyter.sh
jupyter notebook --generate-config
ls
vim run_jupyter.sh
chmod +x run_jupyter.sh
jupyter notebook --generate-config
pip install jupyter
jupyter notebook --generate-config
chmod +x run_jupyter.sh
jupyter notebook password
tmux
pip install numpy matplotlib numba seaborn bokeh
conda create --name py3_study python=3.8

ls
vim py3_study.yaml
git add py3_study.yaml
git commit -m "config file"
git push
git push -u origin master
git push -u origin main
git remote add origin https://github.com/victorismaelreeves/DataScience.git
git push
git push --set-upstream origin master
pbcopy < py3_study.yaml
cat file > /dev/clipboard
cat file > py3_study.yaml
cp py3_study.yaml ~/project_repo
ls
vim py3_study.yaml
conda env export >> py3_study.yaml
vim py3_srudy.yaml
vim py3_study.yaml
cp py3_study.yaml ~/project_repo
echo "jupyter notebook --no-browser --port 8005 --ip 0.0.0.0">run_jupyter.sh
tmux
logout
jupyter notebook --port 8005 --no-browser
ssh-keygen -t ed25519 -C "dr.vreeves@gmail.com"
pbcopy < ~/.ssh/id_ed25519.pub
vim ~/.ssh/id_ed25519.pub
ssh -T git@github.com
ssh git@github.com:victorismaelreeves/DataScience.git
git remote set-url origin git@github.com:victorismaelreeves/DataScience.git
git remote add origin git@github.com:victorismaelreeves/DataScience.git
echo "# DataScience" >> README.md
git init
git add README.md
git commit -m "first commit from remote"
git branch -M main
git remote add origin git@github.com:victorismaelreeves/DataScience.git
git push -u origin main
git config --global user.name "victorismaelreeves
git config --global user.name "victorismaelreeves"
git config --global user.email "dr.vreeves@gmail.com"
mkdir project_repo
cd project_repo/
git init
echo "# project_repo" >> README.md
git add -A
git commit -m "first remote commit"
git remote add origin https://github.com/victorismaelreeves/DataScience.git
git push -u origin master
git remote oprigin
git push origin master
vim py3_study.yaml
ls
git add .
git commit -m "config file"
git push origin master
ls
vim py3_study.yaml
git add .
git commit -m "config file"
git push origin master
cd ..
echo "ssh -N -f -L localhost:7001:localhost:8 my_new_machine">port_forward_remote_machine.sh
vim .ssh/config
cd .ssh/
ls
cd ..
ls
rm port_forward_remote_machine.sh
touch run_jupyter.sh
echo "jupyter notebook --no-browser --port 8005 --ip 0.0.0.0">run_jupyter.sh
ls
vim run_jupyter.sh
chmod +x run_jupyter.sh
jupyter notebook --generate-config
jupyter notebook password
tmux 
python --version
logout
tmux
git clone https://github.com/girafe-ai/software-development-for-ds.git
ls
git commit -m lattest
git push .
git add .
git commit -m latest
git push
git push --set-upstream origin master
git pull
git pull remote origin master
git branch --set-upstream-to=origin/<branch> master
git pull master
git pull DataScience
git pull https://github.com/victorismaelreeves/DataScience.git
git add .
git commit -m latest
git push
git pull
git pull origin master
git pull origin master --allow-unrelated-histories
git add .
git mergetool
git checkout
git checkout .
git commit -m "using theirs"
git pull origin master
git add .
ls
git checkout
git checkout Msoftware-development-for-ds
git checkout software-development-for-ds
git add git add filename.c
git add software-development-for-ds
git pull origin master
git add software-development-for-d
git add software-development-for-ds
git commit -m "all"
git pull origin master
git pull origin master  --allow-unrelated-histories
git commit -m "all"  --allow-unrelated-histories
git add software-development-for-ds  --allow-unrelated-histories
git push
git push origin master
git add .
git status
git commit -m "test"
git push
git push origin master
git status
git add -A
git status
ls
git status
git add 
git add .
git status
git add .
git status
ls 
ls software-development-for-ds/
