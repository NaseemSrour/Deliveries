# Deliveries
Building a culture-specific (& generic) delivery services for our hometown.

<h2>Quick Setup:</h2>

How to run on your local machine:<br>
<h3>Create a virtual environment:</h3>
You need to create a virtual environment (venv) in your project directory, so instead of installing libraries on your own machine,<br>install in a Python's virtual env, by
first cd-ing to your project's directory and creating a virtual env:<br>
In your command prompt:

> python -m venv your-new-venv-name.

This'll create a new directory in your project directory, with the name of your venv.<br>
This directory will store all the packages you install inside the virtual environment.
<br>
<h3>Activate the venv:</h3>

Activate the virtual environment by performing the following command inside your project directory:<br>

On Windows:<br>
> your-venv-folder\Scripts\activate.bat <br><br>

On Unix/MacOS: <br>
> source your-venv-folder/bin/activate 


You will probably want to ignore this folder within git, rather than <b>not</b> adding it everytime you use <i>git add .</i><br>
This can be done by a <i>.gitignore</i> file, but then you'd need to commit this file, and maybe you don't want to share<br>
this file with others, so instead of adding <i>.gitignore</i> to itself, it is better to just add the venv folder<br>
to <b>.git/info/exclude</b>, in your root Git repository, hidden.

Open it with your favourite text editor and append:
> /you-venv-name

<br>
<h3>Install requirements:</h3>
Next, use the requirements file located in the repo, while the venv is activated, and: <br>

>python -m pip install -r requirements.txt

<br>
<h3>Run the server:</h3>
CD into the server folder, and run: <br>

> server.py

When you're done working, you can deactivate the venv by simply running the following in the command prompt:
> deactivate
