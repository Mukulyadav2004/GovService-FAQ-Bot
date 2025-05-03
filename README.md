# GovService FAQ Bot (Illustrative Example)

## Purpose

This is a **simple, illustrative command-line FAQ bot** created as a conceptual example for a C4GT DMP 2025 proposal.

**Its primary goal is NOT to be a functional, production-ready chatbot, but rather to demonstrate:**

*   **Problem Decomposition:** Breaking down a task (answering FAQs) into smaller parts.
*   **Modular Structure:** Separating data (`faqs.json`) from logic (`faq_bot.py`).
*   **Data Handling:** Loading and using structured data (JSON).
*   **API Interaction Mindset:** Simulating the concept of fetching dynamic data (like processing times or fees) that would typically come from an external API.
*   **Basic Logic Flow:** Implementing a simple request-response loop.
*   **User-Centric Thinking:** Providing informative responses and handling unknown queries gracefully.

This project helps illustrate the thought process and structural approach applicable to more complex projects, like integrating offline ASR into the Sunbird ALL platform, even though the technology stack (simple Python script) is different from the target project's stack (Python backend, React frontend, ML models).

## Features

*   Answers predefined questions based on keyword matching.
*   Loads FAQs and keyword mappings from an external `faqs.json` file.
*   **Simulates** fetching dynamic data (e.g., processing times, fees) for relevant questions.
*   Provides a default response for unrecognized queries.
*   Simple command-line interface.

## Technology

*   Python 3 (Standard Library only - `json`, `random`, `time`)

## How to Run

1.  Ensure you have Python 3 installed.
2.  Save the files (`faq_bot.py`, `faqs.json`) in the same directory.
3.  Open a terminal or command prompt in that directory.
4.  Run the script:
    ```bash
    python faq_bot.py
    ```
5.  Ask questions related to passport application, status, cost, processing time, or documents.
6.  Type `quit` to exit.

## Structure

*   **`faq_bot.py`**: Contains the main Python code for the bot logic, including loading data, finding answers, simulating dynamic data fetching, and handling user interaction.
*   **`faqs.json`**: Stores the knowledge base:
    *   `keywords`: Maps user query keywords (lowercase) to internal response keys.
    *   `responses`: Contains the answer templates, including placeholders like `{placeholder}` for dynamic data. Includes a `default` response.
    *   `dynamic_data_providers`: Maps response keys to the *names* of functions in `faq_bot.py` that simulate fetching dynamic data.
*   **`README.md`**: This file.
*   **`.gitignore`**: Standard Python gitignore file.

## Limitations (Intentional for Simplicity)

*   **Very Basic Keyword Matching:** Uses simple substring checking, not sophisticated NLP.
*   **No Real API Calls:** Dynamic data is simulated within the script.
*   **No Context/Memory:** Doesn't remember previous parts of the conversation.
*   **Limited Knowledge:** Only knows about the few topics defined in `faqs.json`.
*   **No Error Handling for Simulated APIs:** Assumes the simulator functions always succeed.

## Relevance to C4GT DMP Sunbird ALL Project

This example demonstrates foundational skills transferable to the C4GT project:
*   Structuring application logic.
*   Handling data inputs and outputs.
*   Designing components that interact (even if simulated here, represents the frontend calling the backend).
*   Focusing on delivering specific functionality based on requirements.