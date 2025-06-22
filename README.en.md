<p align="right">
  <a href="README.md">🇧🇷 Versão em Português</a>
</p>

# 🏆 OBI Level 2 - Solutions

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OBI-Nível%202-2EA44F?style=for-the-badge&logo=codeforces&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Concluído-00C853?style=for-the-badge&logo=check-circle&logoColor=white"/>
  <br>
  <img src="https://img.shields.io/badge/Algoritmos-FF6B6B?style=for-the-badge&logo=code&logoColor=white"/>
  <img src="https://img.shields.io/badge/Lógica-4A90E2?style=for-the-badge&logo=braintree&logoColor=white"/>
  <img src="https://img.shields.io/badge/Competição-FFD700?style=for-the-badge&logo=trophy&logoColor=white"/>
</p>

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=40&pause=1000&color=2EA44F&center=true&vCenter=true&random=false&width=1000&height=100&lines=Brazilian+Informatics+Olympiad;Level+2+Solutions" alt="Typing SVG" />
</div>

---

## 📚 Table of Contents

- [About the Project](#about-the-project)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Problems & Examples](#problems--examples)
- [Technical Highlights](#technical-highlights)
- [How to Run](#how-to-run)
- [Tests](#tests)
- [License](#license)
- [Author](#author)
- [Suggestions for Future Improvements](#suggestions-for-future-improvements)

---

## 📋 About the Project

> This repository gathers commented and optimized solutions for the challenges of the Brazilian Informatics Olympiad (OBI) Level 2 - Phase 1 (2025), developed in Python. The focus is on clarity, efficiency, and best practices in competitive programming.

✨ **Highlight:** Demonstrates skills in logic, simulation, list manipulation, and optimization, making it ideal for portfolios and GitHub highlights.

🔗 Learn more about OBI: [olimpiada.ic.unicamp.br](https://olimpiada.ic.unicamp.br)

---

## 🚀 Technologies Used

- ![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
- Algorithms and programming logic
- Basic data structures

---

## 🗂️ Project Structure

```text
obi-nivel2-solucoes/
│
├── 📄 festa_junina.py      # Solution for Problem 1: Festa Junina
├── 📄 dieta_garfield.py    # Solution for Problem 2: Garfield's Diet
├── 📄 cafeteria.py         # Solution for Problem 3: Cafeteria
└── 📄 grafico_barras.py    # Solution for Problem 4: Bar Chart
```

---

## 🎯 Problems & Examples

<details>
<summary><b>1️⃣ Problem 1 - Festa Junina</b></summary>

- **Description:** Calculate the minimum total distance Luísa needs to walk to visit the supermarket and the store, in any order, and return to school.
- **Difficulty:** ⭐⭐
- **Complexity:** O(1)
- **Solution:** [`festa_junina.py`](festa_junina.py)

**Sample input:**

```text
10
5
13
```

**Sample output:**

```text
16
```

</details>

<details>
<summary><b>2️⃣ Problem 2 - Garfield's Diet</b></summary>

- **Description:** Calculate how many calories Garfield can still consume without exceeding the daily limit, given the meal history.
- **Difficulty:** ⭐⭐⭐
- **Complexity:** O(N)
- **Solution:** [`dieta_garfield.py`](dieta_garfield.py)

**Sample input:**

```text
3 2000
65 15 20
40 20 25
50 10 35
```

**Sample output:**

```text
655
```

</details>

<details>
<summary><b>3️⃣ Problem 3 - Cafeteria</b></summary>

- **Description:** Check if it is possible to prepare a drink with the desired amount of milk, given the cup volume and coffee doses.
- **Difficulty:** ⭐⭐⭐
- **Complexity:** O(C/D)
- **Solution:** [`cafeteria.py`](cafeteria.py)

**Sample input:**

```text
130
150
200
30
```

**Sample output:**

```text
S
```

</details>

<details>
<summary><b>4️⃣ Problem 4 - Bar Chart</b></summary>

- **Description:** Generate a text-based bar chart from the popularity of toys.
- **Difficulty:** ⭐⭐⭐⭐
- **Complexity:** O(N\*H)
- **Solution:** [`grafico_barras.py`](grafico_barras.py)

**Sample input:**

```text
4
4 2 5 3
```

**Sample output:**

```text
0 0 1 0
1 0 1 0
1 0 1 1
1 1 1 1
1 1 1 1
```

</details>

---

## ✨ Technical Highlights

- ✅ Solving real logic and simulation problems
- ✅ Efficient manipulation of lists and data structures
- ✅ Well-commented and organized code, following Python best practices
- ✅ Input/output examples for easy understanding and testing

---

## 💻 How to Run

<p align="center">
  <img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Windows"/>
  <img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Linux"/>
  <img src="https://img.shields.io/badge/macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="macOS"/>
</p>

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GersonResplandes/obi-nivel2-solucoes.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd obi-nivel2-solucoes
   ```
3. **Run any of the solutions:**
   ```bash
   python festa_junina.py
   # or
   python dieta_garfield.py
   # or
   python cafeteria.py
   # or
   python grafico_barras.py
   ```

---

## ✅ Tests

To run automated tests (coming soon):

```bash
pytest tests/
```

---

## 📄 License

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&logo=license&logoColor=white" alt="License"/>
</p>

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## 👨‍💻 Author

<p align="center">
  <img src="https://img.shields.io/badge/GitHub-GersonResplandes-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/>
  <img src="https://img.shields.io/badge/LinkedIn-GersonResplandes-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=500&size=20&pause=1000&color=2EA44F&center=true&vCenter=true&random=false&width=600&height=50&lines=Developed+by+GersonResplandes" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://profile-counter.glitch.me/obi-nivel2-solucoes/count.svg" alt="Visitor Counter"/>
</p>

---

## 💡 Suggestions for Future Improvements

- [ ] Add automated tests for each solution
- [ ] Include GIFs or images illustrating the execution of the algorithms
- [ ] Provide the problem statements in Markdown format
- [ ] Create a GitHub Pages site for a visual presentation of the project
- [ ] Add support for other languages (C, C++, Java)
- [ ] Include detailed complexity analysis for each solution
- [ ] Improve input/output examples with more test cases

---
