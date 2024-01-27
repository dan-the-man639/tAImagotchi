# Running the Backend

1. Go to Backend Directory

    ```bash
    cd backend
    ```

2. **Create and Activate a Virtual Environment **

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

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the backend, use the following command:

```bash
uvicorn main:app --reload
```

Once the application is running, it will be served at http://127.0.0.1:8000. You can access it using a web browser or any API testing tool.
