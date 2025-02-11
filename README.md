# FastAPI Setup Guide

## Setting Up a Virtual Environment

```bash
python3 -m venv env
```

## Activating the Virtual Environment

```bash
source env/bin/activate
```

## Installing Dependencies

```bash
pip install fastapi uvicorn
```

## Running the FastAPI Application

```bash
uvicorn working:app --reload
```

## Deactivating the Virtual Environment

To deactivate the virtual environment, type:

```bash
deactivate
```

## API Documentation

Once the server is running, visit:

- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) - Interactive API documentation (Swagger UI)

## What Pydantic Does

Pydantic is used in FastAPI for data validation and serialization. It provides:

1. **Data Validation** - Automatically validates data types and constraints
2. **Type Hints** - Uses Python type annotations for schema definition
3. **Data Parsing** - Converts incoming data to proper Python types
4. **Schema Generation** - Creates JSON Schemas for API documentation
5. **Error Handling** - Provides detailed error messages for invalid data