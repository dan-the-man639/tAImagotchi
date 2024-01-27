## Setting Up The Development Environment

Before running the application, you need to set up your development environment. Follow these steps to create a virtual environment and install the necessary dependencies.

1. **Go to Backend Directory**

    ```bash
    cd backend
    ```

2. **Create and Activate a Virtual Environment**

    - For Windows:
      ```cmd
      python -m venv venv
      .\venv\Scripts\activate
      ```

    - For macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install the Requirements**

    If you have a `requirements.txt` file, install the dependencies using:

    ```bash
    pip install -r requirements.txt
    ```

    If you need to create a `requirements.txt` file, first install your dependencies as usual (e.g., `pip install fastapi uvicorn`). Then, freeze your installed packages:

    ```bash
    pip freeze > requirements.txt
    ```

    This command will generate a `requirements.txt` file with all the installed packages and their versions, which is crucial for maintaining a consistent development environment.

## Running the Application

To run the backend, use the following command:

```bash
uvicorn main:app --reload
