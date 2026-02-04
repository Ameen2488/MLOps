# Module 1 Exercises: Foundations

**Objective**: Solidify your understanding of the MLOps Landscape and Project Lifecycle.
**Format**: Highly interactive. Try to answer before clicking "Reveal Answer".

---

## 🧠 Part 1: Rapid Fire Flashcards
*Test your intuition.*

<details>
<summary><b>Q1: What is the main difference between MLOps and Model Ops?</b></summary>
<br>
<b>Answer:</b>
MLOps covers the <b>end-to-end lifecycle</b> (Data -> Train -> Deploy -> Monitor).
ModelOps often refers specifically to the <b>operational management</b> of models in production (Governance, Cataloging) within a large enterprise.
</details>

<details>
<summary><b>Q2: True or False: You should always start with a Deep Learning model to ensure maximum accuracy.</b></summary>
<br>
<b>Answer:</b>
<b>False!</b> Always start with a <b>Dummy Baseline</b> (e.g., predicted mean) or a simple Heuristic. Then try a linear model. Deep Learning is the last resort due to complexity and cost.
</details>

<details>
<summary><b>Q3: What is "Technical Debt" in ML?</b></summary>
<br>
<b>Answer:</b>
It refers to the hidden cost of maintaining complex, entangled ML systems. For example, "Glue Code" (massive scripts to move data) or "Hidden Feedback Loops" (model training on its own stale predictions).
</details>

---

## 📝 Part 2: The "Broken" Startup (Scenario Analysis)
**Scenario**: You join "CatDetector.ai".
- **Bob (DS)** trains models on his laptop 💻.
- He emails the `.h5` file to **Alice (Backend)** 📧.
- Alice puts it in a folder on the server and restarts the API 🔄.
- There is no versioning of data ❌.

**Task**: Identify 3 Critical Risks and the MLOps Maturity Level.

<details>
<summary><b>🔻 Click to Reveal Diagnosis</b></summary>
<br>
<b>MLOps Level:</b> <b>Level 0 (Manual Process)</b>

<b>Critical Risks:</b>
1.  <b>Bus Factor</b>: If Bob's laptop dies, the ability to retrain is lost (No reproducible pipeline).
2.  <b>No Rollback</b>: If the new `.h5` file is bad, there's no git commit or registry to revert to the previous version easily.
3.  <b>Training-Serving Skew</b>: Bob's laptop environment (Python 3.9, numpy 1.21) might differ from Alice's server (Python 3.8, numpy 1.19), causing silent bugs.
</details>

---

## 🐛 Part 3: Fix the Workflow
**Task**: Propose the *minimum viable fix* for Bob and Alice using **Git** and **DVC**.

<details>
<summary><b>🔻 Click to Reveal Minimial Viable Fix</b></summary>
<br>
1.  <b>Git</b>: Bob pushes code (`train.py`) to GitHub. Alice pulls code.
2.  <b>DVC</b>: Bob tracks data (`dvc add data/`) and pushes to S3. Bob tracks the model (`dvc add model.h5`) and pushes to S3.
3.  <b>Workflow</b>:
    - Bob pushes code changes + `model.dvc` file.
    - Alice does `git pull` -> `dvc pull model.h5`.
    - No more emailing large files!
</details>
