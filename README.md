## Getting Started

### Prerequisites

- Python 3.6 or higher

### Installing

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/avatar-api.git
cd avatar-api
```

2. **Set up a virtual environment**

- On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

- On Unix or MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install the dependencies**

Instead of manually installing Flask and Pillow, you'll use the `requirements.txt` file, which lists these dependencies.

```bash
pip install -r requirements.txt
```

This command reads the `requirements.txt` file in your project directory and installs all the listed packages along with their dependencies.

### Running the Application

To start the Flask application, use:

```bash
python app.py
```

Or, if you're on Unix/MacOS and Python 3 is not the default version:

```bash
python3 app.py
```

Then, access the API by navigating to `http://127.0.0.1:5000/avatar/<initials>` in your web browser, replacing `<initials>` with the initials for which you want to generate an avatar.

## Deployment

Refer to Flask's [deployment options](https://flask.palletsprojects.com/en/2.0.x/deploying/) for guidance on deploying the application to a live system.

[Reading Blog Article](https://www.pykit.org/simple-avatar-generation-api-guide/)
