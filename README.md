# SQL Assistant

# AI SQL Assistant

An AI-powered SQL assistant that enables users to query various data sources using natural language. This application is built with Streamlit for the interactive user interface, leveraging LangChain for powerful language model integrations, and utilizing OpenRouter for flexible API access to large language models.

## Project Overview

This project aims to simplify data interaction by allowing users to ask questions in plain English and receive SQL queries or data manipulations as results. It supports a variety of data sources, making it a versatile tool for data analysts, developers, and business users.

## Project Preview

https://connect-with-data.streamlit.app

## Features

-   **Natural Language to Query Conversion:** Translate natural language questions into executable SQL queries or data manipulation commands.
-   **Multi-Source Data Connectivity:** Seamlessly connect to and query data from:
    -   **Snowflake:** Securely connect using in-app credential inputs for user, password, account, warehouse, database, schema, and role.
    -   **MongoDB:** Connect via a provided connection string and database name.
    -   **MySQL:** Connect to your MySQL databases.
    -   **CSV/Excel Files:** Upload and query local CSV or Excel files.
    -   **Google Sheets:** Connect to public or shared Google Sheets.
-   **Interactive Streamlit Interface:** A user-friendly web application for inputting prompts, selecting data sources, and viewing results.
-   **Real-time Query Execution:** Execute generated queries against the selected data source and display results instantly.
-   **Dynamic Prompt Templates:** Utilizes `tpch_prompt.yaml` for structured prompt generation, enhancing LLM accuracy.
-   **Robust Error Handling:** Comprehensive error handling for connection issues, query execution failures, and API errors.

## Usage

1.  **Start the application:**
    ```bash
    streamlit run home.py
    ```

2.  **Access the application:**
    Open your web browser and navigate to `http://localhost:8501`.

3.  **Select Data Source:**
    Choose your desired data source (Snowflake, MongoDB, MySQL, CSV/Excel, Google Sheets) from the sidebar.

4.  **Configure Connection:**
    Provide the necessary connection parameters for your chosen data source. For Snowflake, you will enter credentials directly in the app.

5.  **Enter Your Query:**
    Type your natural language question into the input field.

6.  **Generate and Execute:**
    Click the "Generate Query and Execute" button to process your request and view the results in the "Results" tab.

## Project Structure

```
├── config/           # Application configuration files
├── data_connectors/  # Modules for connecting to various data sources```
├── prompts/          # LLM prompt templates (e.g., for TPC-H dataset)
```├── utils/            # Utility functions and helper modules
├── home.py           # Main Streamlit application entry point
├── openrouter_chat.py# Handles communication with OpenRouter API
├── requirements.txt  # Project dependencies
├── sql_assistant.py  # Core logic for the SQL assistant
├── sql_execution.py  # Manages query execution against connected databases
└── .gitignore        # Specifies intentionally untracked files to ignore
```

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and ensure they adhere to the project's coding standards.
4.  Submit a pull request with a clear description of your changes.
