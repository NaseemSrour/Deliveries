# Deliveries
Building a culture-specific (& generic) delivery services for our hometown.

<h2>Quick Setup:</h2>

How to run on your local machine:<br>
You need to create a virtual environment (venv) in your project directory, so instead of installing on your own machine, install in a Python's virtual env, by
cd-ing to a directory to make a virtual env, and:<br>

> python -m venv your-new-venv-name.

Activate the virtual environment by performing the following command inside your project directory:<br>

On Windows:<br>
> your-venv-folder\Scripts\activate.bat <br><br>

On Unix/MacOS: <br>
> source your-venv-folder/bin/activate 

This'll create a directory in your project directory, with the name of your venv.<br>
You'd probably want to ignore this folder within git, rather than <b>not</b> adding it everytime you use <i>git add .</i><br>
This can be done by an <i>.gitignore</i> file, but then you'd need to commit this file, and maybe you don't want to share<br>
this file with others, so instead instead of adding <i>.gitignore</i> to itself, it is better to just add the venv folder<br>
to <b>.git/info/exclude</b>, in your root Git repository, hidden.

Open it with your favourite text editor and append:
> /you-venv-name


Next, use the requirements file located in the repo, while the venv is activated, and:

python -m pip install -r requirements.txt
