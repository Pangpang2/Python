import os
from datetime import datetime

from git import Repo
from robot.run import run


if __name__ == '__main__':

    # git clone with credential
    git_url = 'git@git.internetbrands.com:QAAutomation/DF_BP_Automation.git'
    git_branch = 'QAA-31451'
    username = 'git'
    rsa_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'id_rsa').replace('\\', '/')

    git_repro_dir = '.\\workspace\\BP_Support_Tool_' + datetime.now().strftime("%m%d%Y_%H%M%S")

    env = {"GIT_SSH_COMMAND": 'ssh -i {identify} -l {username}'.format(identify=rsa_file, username=username)}
    repo = Repo.clone_from(git_url, git_repro_dir, branch=git_branch, env=env)

    print "clone done: " + git_repro_dir

    # run test
    result = run(git_repro_dir, suite='supportTool', test='testTranslateFile', outputdir="output",
                 variable=["browser:chrome",
                           "env:stg",
                           "client_username:ibexcxautxgqde",
                           "file_name:ibexcxautxgqde_2019-08-19_01_48_01_665.xml.gz",
                           "remote:http://qaaew707-vm.carsdirect.win:4444/wd/hub"])

    print 'run tests done:' + str(result)
