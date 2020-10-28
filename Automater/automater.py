import json
from github import Github
import sys
import os
import pathlib
from pathlib import Path
import time



class Automator:

    def __init__(self):
        with open(os.path.join(os.environ['userprofile'], r'automater\credentials.json')) as json_file:
            self.credentials = json.load(json_file)

        #Sign in to GitHub
        github = Github(self.credentials['TOKEN'])
        print('Connected to GitHub!')
        self.user = github.get_user()
        self.name = sys.argv[1]

        self.user.create_repo(name=self.name, private=True)
        print('Repository created!')


    def repo_connection(self):
        # Create repo
        new_path = os.path.join(os.environ['userprofile'], rf'desktop\github\{self.name}')
        os.chdir(new_path)
        print(os.getcwd())
        self.repo_remote = f'git@github.com:{self.credentials["username"]}/{self.name}.git'



        os.system(f'echo # {self.name} >> README.md')

        with open(os.path.join(os.environ['userprofile'], r'automater\commands.txt')) as commands_git:
            commands_git = [line.strip('\n') for line in commands_git]
            for command in commands_git:
                if "add origin" in command:
                    print(f'{command} {self.repo_remote}')
                    os.system(f'{command} {self.repo_remote}')
                    print(f"Setting remote to {self.repo_remote}")
                else:
                    pass
                    os.system(command)


if __name__ == "__main__":
    inst = Automator()
    inst.repo_connection()


