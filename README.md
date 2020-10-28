# Automater

Automator is a simple script to make the process of creating a repository faster. 

With this, you will be coding your project in much less time. Automater creates a folder in your Desktop and then another folder called Github. 
Once the folder is created, the script goes ahead and creates a folder with the name given. 

### Note: This is made for Windows and thus, won't be working with MacOs.

For this to work, the file should be cloned on your "Users" folder. If not, the script won't work. 

## Set up
1. Once the cloning has been complete, make sure that you add a .json file called <strong>credentials.json</strong> in the folder Automater with your **TOKEN** and **username**. 

### Note: The script runs with PyGitHub, therefore, to authenticate, you need a **GitHub token**. [Here's How](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)

2. The script is also made to run with **SSH keys**. You will thus need to enable SSH key on your account. 

## Running

1. To run the script, simply open your Command line and run the following: <code>automater "name_of_repository"</code>

2. Once it has run, all you have to do is head to your Desktop and open the folder GitHub and your new repository will be there. 

