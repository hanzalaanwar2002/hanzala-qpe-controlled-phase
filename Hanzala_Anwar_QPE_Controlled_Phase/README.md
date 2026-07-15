# Quantum Phase Estimation for a Controlled-Phase Gate

**Student:** Hanzala Anwar  
**Course:** Master's Quantum Computing  
**Project option:** P2 - Quantum Phase Estimation

## Project summary
This repository implements QPE in Qiskit for `U = CP(phi)` with eigenvector `|11>`. It includes exact and non-exact phase experiments, a precision study, a simple noise model, and a discussion of logical versus transpiled complexity.

## Repository structure
- `notebooks/Hanzala_Anwar_QPE.ipynb` - Colab-ready implementation and experiments
- `src/qpe.py` - reusable circuit and decoding functions
- `report/main.tex` - Overleaf-ready report
- `report/references.bib` - bibliography
- `report/figures/` - add figures exported by the notebook
- `results/` - optional CSV outputs

## Run in Google Colab
1. Upload the notebook to Colab or open it from GitHub.
2. Run the dependency installation cell.
3. Run all cells in order.
4. Download the generated PNG and CSV files

## Reproducibility
The notebook fixes simulator and transpiler seeds. Package ranges are listed in `requirements.txt`.
