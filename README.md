# Virtual Tech School
Virtual Tech School is a community aiming to help everyone get started, learn and grow together in our fast paced industry. By everyone, we mean EVERYONE!

This is a repository for our community's website. Following are the steps for running it locally in your system -

### 1. Creating a Virtual Environment
After cloning the repository, navigate into the repository through command line terminal / command prompt and create a virtual environment with the following command -

`python -m venv venv`

We have used **Python3.11.x** for this application. You can check the version of python in your system by running -

`python --version`

**Note** - Python 3 might be accessible in some devices with `python3` command, therefore your command to create the virtual environment becomes - `python3 -m venv venv`

**Note** - Sometimes, you may get an error while trying to create a virtual environment, returning a **non-zero exit status 1**. In that case, checkout the solution [here](https://stackoverflow.com/questions/24123150/pyvenv-3-4-returned-non-zero-exit-status-1). After this, the above command should run as intended.

### 2. Sourcing the Virtual Environment
Once the virtual environment is created, source it with -

`source venv/bin/active`

**Note** - The above command will work in Linux and MacOS, but for windows, try the below command -

`venv\Scripts\activate.bat`

### 3. Sourcing Environment Variables
**For MacOS/Linux -** Create a file called `dev.env` and add the following inside that file -
```
export FLASK_DEBUG=true
export SERVICE_URL=http://localhost:5000
```
Source the above file with - `source dev.env`

**For Windows -** Create a file called `dev.bat` and add the same contents as above in the file. Source it with - `dev.bat`

### 4. Installing Libraries and Dependencies
For installing dependencies and libraries, run -

`pip install -r requirements.txt`

### 5. Starting the server
To start the server, run -

`python manage.py run`

The website should now be hosted on `http://localhost:5000`. Feel free to contribute in our website, or let us know if you have any improvements in mind on our [discord server](https://discord.gg/EYB8tQxjxH).

## Connect with our mentor
<a href="https://twitter.com/apoorvtwts">
    <img width="30px" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg" />
</a>&ensp;
<a href="https://www.linkedin.com/in/apoorv-goyal-a17103158/">
    <img width="30px" src="https://www.vectorlogo.zone/logos/linkedin/linkedin-icon.svg" />
</a>&ensp;
<a href="https://www.youtube.com/c/ApoorvGoyalMain">
    <img width="30px" src="https://i.pinimg.com/originals/46/02/cb/4602cbc18967da9c1eba7452905cd99b.png" />
</a>&ensp;
<a href="https://www.instagram.com/intellectualspirits/">
    <img width="30px" src="https://www.vectorlogo.zone/logos/instagram/instagram-icon.svg" />
</a>&ensp;
<a href="https://apoorvgoyal.hashnode.dev/">
    <img width="30px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1611902473383/CDyAuTy75.png?auto=compress" />
</a>&ensp;
<a href="https://github.com/apoorv-on-git">
    <img width="30px" src="https://www.vectorlogo.zone/logos/github/github-icon.svg" />
</a>

## Join Virtual Tech School
<a href="https://discord.gg/EYB8tQxjxH">
    <img width="30px" src="https://www.vectorlogo.zone/logos/discordapp/discordapp-tile.svg" />
</a>&ensp;
<a href="https://twitter.com/virtechschool">
    <img width="30px" src="https://www.vectorlogo.zone/logos/twitter/twitter-official.svg" />
</a>&ensp;
<a href="https://virtualtechschool.hashnode.dev/">
    <img width="30px" src="https://cdn.hashnode.com/res/hashnode/image/upload/v1611902473383/CDyAuTy75.png?auto=compress" />
</a>
