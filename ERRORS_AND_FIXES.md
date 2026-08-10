# Project Errors and Fixes

This file lists the real errors in the project and exactly what to fix.

## 1) Wrong import in Streamlit startup file

File:
- [Agentic_Agent/main.py](Agentic_Agent/main.py)

Problem:
```python
from piplimimg import entryPoint
```

This is wrong because the file is inside the package `Agentic_Agent`.
The correct import is:
```python
from Agentic_Agent.piplimimg import entryPoint
```

Why this matters:
- Python may throw `ModuleNotFoundError: No module named 'piplimimg'`
- The app cannot start correctly when run as a package

Solution:
- Replace the import line with the package-qualified version above

---

## 2) Gemini API key mismatch between files

Files:
- [Agentic_Agent/main.py](Agentic_Agent/main.py)
- [Agentic_Agent/model.py](Agentic_Agent/model.py)
- [.env](.env)

Problem:
- The sidebar writes to `GEMINI_API_KEY`
- The model reads `GEMINI_NEW_API_KEY`
- The environment file also uses `GEMINI_NEW_API_KEY`

This creates a mismatch.

Example from the app:
```python
os.environ["GEMINI_API_KEY"] = key
```

Example from the model:
```python
api_key = os.getenv("GEMINI_NEW_API_KEY")
```

Why this matters:
- The key is not consistently loaded
- Gemini returns:
  `API key not valid. Please pass a valid API key.`
- Error type: `INVALID_ARGUMENT` / `API_KEY_INVALID`

Solution:
- Use one variable name everywhere
- Recommended option:
```env
GEMINI_API_KEY=your_valid_google_key_here
```
- Then read it in code with:
```python
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GEMINI_NEW_API_KEY")
```

---

## 3) The actual runtime error is an invalid Google key

This is the key error shown by Gemini:

```text
Error calling model 'models/gemini-2.5-flash-lite' (INVALID_ARGUMENT): 400 INVALID_ARGUMENT.
API key not valid. Please pass a valid API key.
```

This is not always a code bug.
It usually means one of these is true:
- the key is expired
- the key is copied incorrectly
- the key belongs to a different Google product or project
- the app is using an old stale value

Solution:
- Generate a fresh Gemini API key from Google AI Studio
- Put it in [.env](.env) as `GEMINI_API_KEY`
- Restart the app completely

---

## 4) Earlier package import problem with LangChain splitter

File:
- [Tools/Rag/system_setup.py](Tools/Rag/system_setup.py)

Problem:
The project previously used:
```python
from langchain.text_splitter import RecursiveCharacterTextSplitter
```

This is wrong for the installed package.
The correct package is:
```python
from langchain_text_splitters import RecursiveCharacterTextSplitter
```

Why this matters:
- It causes import failure like:
  `ModuleNotFoundError: No module named 'langchain.text_splitter'`

Solution:
- Use `langchain_text_splitters`

---

## 5) Environment variable naming for embedding model

Files:
- [Agentic_Agent/main.py](Agentic_Agent/main.py)
- [Tools/Rag/system_setup.py](Tools/Rag/system_setup.py)
- [Tools/Rag/retrive.py](Tools/Rag/retrive.py)

Problem:
The project uses `EMBADDING_MODEL_SENTENCE` (misspelled) in several places.

Example:
```python
os.getenv("EMBADDING_MODEL_SENTENCE")
```

This is not always fatal, but it can create confusion and missing value issues.

Solution:
- Keep one consistent name, such as:
```env
EMBEDDING_MODEL_SENTENCE=sentence-transformers/all-MiniLM-L6-v2
```
- Then read that variable everywhere

---

## 6) The reason the app still shows the same error

Even after creating a new key, you may still get the same error if:
1. the app is still running with the old environment
2. the key is stored under the wrong variable name
3. you did not restart Streamlit after editing [.env](.env)
4. the key itself is invalid or expired

---

## Recommended fix order

1. Fix the import in [Agentic_Agent/main.py](Agentic_Agent/main.py)
2. Fix the key variable names in [.env](.env) and [Agentic_Agent/model.py](Agentic_Agent/model.py)
3. Use a fresh valid Gemini key
4. Restart the app
5. Test again

---

## Quick final answer

The main error is not just one thing.
The project had 3 important issues:

1. wrong import path
2. wrong key variable name
3. invalid/expired Google API key

The most important error you see in the browser is:
`API key not valid. Please pass a valid API key.`

That means your Gemini key is being rejected by Google.
