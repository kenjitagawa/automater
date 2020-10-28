@echo off
goto :main

:git_readme

        echo ===================================

        echo Creating directory %~1...
        mkdir %1
        timeout /t 1 /nobreak > NUL
        cd %1
        echo Done!
        echo ===================================


        echo Connecting local repo to GitHub...
        echo Please wait...
        timeout /t 2 /nobreak > NUL

	    echo ===================================

	    echo Complete! Happy coding!


goto :eof



:main

    echo ===================================

    echo Creating repository on github!
    start "" /B python %userprofile%\automater\automator.py %1
    echo Done!

    cd %userprofile%\desktop
    echo Checking for Desktop folder "github"

    if exist github (goto opt_1) else (goto opt_2)

    :opt_1
        echo Folder "github" exists!
        cd github
        call :git_readme %~1

    goto :eof


    :opt_2
        echo Making directory...
        for
        mkdir github
        cd github
        call :git_readme %~1

    goto :eof

goto :eof







