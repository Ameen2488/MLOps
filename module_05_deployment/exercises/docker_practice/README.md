# Exercise: Docker Practice

**Objective**: Write a Dockerfile for a script.

## 📝 Steps

1. Create `script.py` which prints the OS name (`os.uname()`).
2. Write a `Dockerfile` using `python:3.9-slim`.
3. Build it: `docker build -t my-script .`
4. Run it: `docker run my-script`.
