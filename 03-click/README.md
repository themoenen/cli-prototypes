# Click prototype

### First time Installation

-   Make sure you have Python 3.10 or later running.
-   Install pipenv if not yet installed:

        pip3 install pipenv

-   Install the environment. This installs all dependencies from Pipfile.

          pipenv install

-   Visual Studio code:
    -   Open main.py or other python file
    -   If blue status bar at the bottom is not visible, turn it on: View/Appearance/Status Bar
    -   Click on python version on the right side of the status bar
    -   Select the pipenv environment that was created

<br><br>

### Run App

1.  Install & activate the virtual environment.

        pipenv shell

2.  Install the **ibmad** package.<br>
    _(This uses setup.py)_

        pip install --editable .

    Your CLI should return something like:

        Successfully installed ibmad-x.x.x

3.  You now should be able to access the IBM Accelerated Discovery CLI:

        ibmad
