# 📘 Quiz Generator API Documentation

## Overview
This API provides endpoints to generate, manage, and download quizzes based on categories and commands.  
It supports **multiple languages** (`en`, `ar`) and bilingual mode (`ar-en`, `en-ar`) and different output formats (`html`, `tex`, `md`,`txt`,`json`).  

The backend is powered by **FastAPI** and uses a `QuizBuilder` class for quiz generation.

---

## Base URL
```
http://<host>:<port>/
```

---

## Endpoints

### 1. `GET /`
**Description:**  
Returns the homepage with a basic HTML interface.

**Response:**  
- `HTMLResponse` with `base.html` template.

---

### 2. `GET /quiz`
**Description:**  
Generates and displays a new quiz page.

**Response:**  
- `HTMLResponse` with quiz UI (`quiz.html`).  
- Includes available commands, categories, formats, and quiz IDs.

---

### 3. `GET /api/categories`
**Description:**  
Fetch all quiz categories with descriptions.

**Response (200):**
```json
{
   "encoding":{
      "short":"Encoding & number systems",
      "long":"Covers numeral bases, complements, character encoding, floating point representation, and data measurement units.",
      "commands":[
         {
            "name":"float",
            "short":"Floating-point representation",
            "long":"IEEE-754 floating-point conversion and analysis."
         },
      ]
   },
   "boolean algebra":{
      "short":"...",
   },
}
```

---

### 4. `GET /api/commands`
**Description:**  
Fetch all commands, optionally filtered by category.

**Query Parameters:**
- `category` *(string, optional)* → category name to filter.

**Responses:**
- **200 OK**
```json
{
   "float":{
      "category":"encoding",
      "short":"Floating-point representation",
      "long":"IEEE-754 floating-point conversion and analysis.",
      "example":"Represent 1.5 under the IEEE-754 standard.",
      "template":"encoding/float",
      "args":{
         "float":{
            "type":"float",
            "default":0,
            "label":"Float number"
         }
      }
   },
    ...
}
```

---

### 5. `GET /api/random-commands`
**Description:**  
Get N random commands, optionally filtered by category.

**Query Parameters:**
- `n` *(integer, default=3)* → number of commands.
- `category` *(string, optional)* → restrict randomization.

**Response (200):**

```json
{
"commands_list":{
  "complement":{
    "category":"encoding",
    "short":"Number complements",
     "long":"Exercises on complement to one and complement to two.",
     "example":"Represent the following number in signed value, 1's complement and 2's complement.",
     "template":"encoding/cp",
     "args":{ "number":{ "type":"integer", "default":-12, "label":"Number (decimal)"}}
     },
  "bcdx3":{}
... 
   }
}
```

---

### 6. `POST /submit`
**Description:**  
Process a quiz submission and generate a question + answer.

**Request Body (JSON):**
```json
{
  "category": "logic",
  "command": "nand",
  "args": {"inputs": 2},
  "select_random_values": true,
  "outformat": "html",
  "quizid": "",
  "download": false
}
```

**Responses:**

- **200 OK (JSON format)**
```json
{
  "command": "nand",
  "outformat": "html",
  "category": "boolean logic",
  "question": "Simplify NAND gate output...",
  "answer": "Result: ...",
  "args": {"inputs": 2},
  "quiztext": "",
  "download_url": "/download/tmp123.txt?outformat=html"
}
```

- **200 OK (HTML format)**  
Renders `result.html` with the quiz.

- **400 Bad Request**  
If category or command is invalid:
```json
{"detail": "Invalid command 'xyz'"}
```

---

### 7. `GET /download/{filename}`
**Description:**  
Download a generated quiz file.

**Path Parameters:**
- `filename` *(string, required)* → temporary file name.

**Query Parameters:**
- `outformat` *(string, default="txt")* → file extension.

**Response:**  
- `FileResponse` with quiz content, named `quiz.<outformat>`.

---

## Middleware

### Language Detection
The API automatically detects language via:
1. Query parameter `?lang=...`
2. `lang` cookie
3. `Accept-Language` request header  
Falls back to default: `ar-en`.

---

## Error Responses

- **400 Bad Request:** Invalid category or command.
- **404 Not Found:** Download file missing.
- **500 Internal Server Error:** Server-side failure.
