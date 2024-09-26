# NWA-Pinball-Website
![NWA Pinball Logo](/assets/NWAPinballFullSmallerBack.png)
This is the website for NWA Pinball, located in Rogers, AR.

## Django Superuser Credentials (for now)
To login as the superuser, these are the credentials:
- email: email@example.com
- username: admin
- password: seniorproject


## Requirements

- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/products/distribution) installed on your system.


## How to Run on Local Environment
Use the following command to create the enviroment from the `enviroment.yml` file:
```bash
conda env create -f environment.yml
```
Once the enviroment is created, activate it using the following command:
```bash
conda activate SeniorProject
```

## Fresh Install (instead of using `CondaEnv` contents)
### 1. Create and Activate Conda Environment

First, create a Conda environment with the required Python version:

```bash
conda create -n myenv python=3.9
```

### 2. Activate new Conda Environment

Activate the newly created Conda environment:
```bash
conda activate myenv
```

### 3. Install Dependancies

Install the dependencies using pip:
```bash
pip install -r requirements.txt
```

### 4. Apply Database Migrations

Run the following command to apply any pending migrations:
```bash
python manage.py migrate
```

### 5. Start the Development Server

Once the Conda environment is properly installed, launch the Django development server:
```bash
python manage.py runserver
```


## Adding/Modifying Assets
To get to the assets, navigate to the `static/` folder. Most of these icons/SVG images can probably be removed to cut down on size once we're done.