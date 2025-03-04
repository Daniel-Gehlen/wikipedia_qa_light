# Wikipedia QA Light

## Overview
Wikipedia QA Light is a lightweight Python application that allows users to ask questions and receive answers based on Wikipedia articles. The application automatically finds the most relevant Wikipedia article based on the user's question, extracts relevant information, and presents the response along with citations.

## Technologies Used
- **Python**: Core programming language for the application.
- **PyQt5**: Provides the graphical user interface (GUI).
- **Wikipedia API (wikipedia)**: Fetches relevant articles and extracts their content.
- **Requests & BeautifulSoup**: Retrieves and parses article references for citation purposes.

## Features
- Automatic article retrieval based on the question.
- Extracts and displays relevant answers from Wikipedia articles.
- Provides citations from the article references.
- Simple and intuitive GUI using PyQt5.

## Installation
### Prerequisites
Ensure you have Python installed (recommended version 3.8+). Then, install the required dependencies:

```bash
pip install wikipedia-api requests beautifulsoup4 PyQt5
```

## Usage
Run the application using:
```bash
python wiki_responder.py
```

### How It Works
1. Enter a question in the text field.
2. Click the **Search** button.
3. The app will automatically find the best matching Wikipedia article.
4. It extracts a relevant answer and displays citations if available.

## Example
**Question:** "Who discovered gravity?"

**Response:**
```
# Answer for: Who discovered gravity?

**Answer:** Isaac Newton formulated the laws of gravity based on his observations.

**Source:** [Wikipedia Link]

**Cited References:**
- Reference 1
- Reference 2
```

## Future Improvements
- Enhance answer extraction with NLP techniques.
- Add multilingual support.
- Implement a more advanced question-answering model.

## License
MIT License

