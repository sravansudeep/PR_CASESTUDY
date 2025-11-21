# SRKW BISoN Analysis

Bayesian social network analysis of Southern Resident Killer Whales using hierarchical edge-weight estimation.

---

## Dataset

**22 whales, 89 dyadic contacts**

- `srkw_attributes.csv` - id, age, sex, asc, matriline
- `srkw_contacts_edgelist.csv` - contact counts between pairs

---

## Installation

```bash
pip install pymc arviz pandas numpy networkx matplotlib scipy statsmodels
```

---

## Usage

```bash
python srkw_bison_pipeline.py
```

Update file paths in script:
```python
ATTR_PATH = "path/to/srkw_attributes.csv"
CONTACT_PATH = "path/to/srkw_contacts_edgelist.csv"
```

---

## Methodology

**Stage 1:** Hierarchical Negative Binomial model for edge weights  
**Stage 2:** Propagate uncertainty to eigenvector centrality (200 draws)  
**Stage 3:** Regression: `centrality ~ age + sex`

---

## Results

### Regression Coefficients

| Predictor | Mean | 95% CI | Significant? |
|-----------|------|--------|--------------|
| Age | -0.007 | [-0.008, -0.006] | ✓ Yes |
| Sex (Male) | 0.000 | [0.000, 0.000] | No |
| Intercept | 0.295 | [0.274, 0.313] | - |

### Key Findings
- Matriarchal structure: Top whales all female
- Younger whales slightly more central
- Sex has no independent effect on **eigenvector centrality**

**Note:** Franks et al. (2021) found a significant sex effect (β = -9.99, males less central) using **node strength** as the dependent variable. Our analysis uses **eigenvector centrality**, which measures the quality of connections rather than quantity. This suggests:
- Sex affects *how many* connections (strength) 
- Sex does not affect *how central* connections are (eigenvector) 

---

## Outputs

**CSV:**
- `regression_coefficients.csv`
- `node_eigenvector_summary.csv`

**Plots:**
- `network_visualization.png` - Social network graph
- `eigenvector_ridgeline.png` - Posterior distributions per whale
- `regression_coefficients_plot.png` - Coefficient estimates

---

## Model Diagnostics

- R̂ < 1.01 for all parameters 
- ESS: 870 (alpha_0), 1133 (alpha_nb), 171 (sigma_u)

---

## Reference

Franks et al. (2021). Calculating effect sizes in animal social network analysis. *Methods in Ecology and Evolution*, 12(1), 33-41.

---

## License

Research and educational use.
