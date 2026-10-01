# AI: SQL to ORM Refactoring and Security Analysis

## Task Overview

This task demonstrates the use of AI to refactor a procedural Python database application that uses MySQL Connector and raw SQL into a modern SQLAlchemy ORM implementation.

The objective is to improve abstraction, maintainability, readability, transaction management, and security while demonstrating how Python objects can represent database records through an ORM model.

## Files

### `initial_code.py`

Contains the original procedural implementation using MySQL Connector and SQL statements for database operations.

The original implementation demonstrates CRUD operations including:

- Creating a user
- Retrieving a user
- Updating a user's email
- Deleting a user
- Listing users

The original code uses parameterized SQL queries rather than unsafe string concatenation.

### `refactored_code.py`

Contains the refactored SQLAlchemy ORM implementation.

It demonstrates:

- A SQLAlchemy declarative `Base`
- A `User` ORM model
- Integer primary key
- Username and email fields
- Database constraints
- SQLAlchemy engine creation
- Environment-variable database configuration
- Table creation with `Base.metadata.create_all()`
- ORM session management
- Creating users
- Querying users
- Updating users
- Deleting users
- Listing users
- Commit and rollback handling
- SQLAlchemy 2.x ORM syntax

## Security Analysis

The SQLAlchemy ORM approach provides a structured abstraction for interacting with the database. ORM expressions and parameter binding reduce the risk of SQL injection compared with constructing SQL statements through unsafe string formatting.

The refactored implementation also demonstrates transaction handling with explicit commits and rollbacks. Database credentials should not be hard-coded in production applications; environment variables or a secure secrets manager should be used instead.

However, using an ORM does not automatically make an application completely secure. Developers must still validate input, manage credentials securely, configure appropriate database permissions, protect sensitive information, and follow secure coding practices.

## Maintainability Benefits

SQLAlchemy ORM provides an object-centric approach in which Python classes represent database tables and Python objects represent database records.

This improves abstraction because application code can work with Python objects rather than repeatedly constructing SQL statements. Centralized model definitions also make the application easier to understand, test, modify, and maintain as it grows.

## AI-Assisted Refactoring

The refactoring was performed using a comprehensive AI prompt requiring:

1. A SQLAlchemy declarative `User` model.
2. Database engine and session configuration.
3. Table creation.
4. User creation through an ORM session.
5. User querying through ORM expressions.
6. Complete CRUD operations.
7. Security analysis.
8. Maintainability and professional software engineering benefits.
9. A complete SQLAlchemy ORM example.

The AI response was reviewed to ensure that security claims were accurate and that ORM usage was not presented as a complete replacement for secure development practices.

## Assignment Deliverables

- Initial procedural database code
- Refactored SQLAlchemy ORM code
- README documentation
- AI execution screenshot and reflection are included in the accompanying Google Doc
