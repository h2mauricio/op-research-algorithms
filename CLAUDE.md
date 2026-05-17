# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Educational Operations Research repository for students learning to solve optimization problems using Gurobi. Content is delivered as Jupyter notebooks (Python). Requires a valid Gurobi academic license installed and activated before running any notebooks.

## Project Management

This project uses `uv` for Python environment and dependency management.

```bash
uv sync                        # install dependencies
uv add <package>               # add a new dependency
uv run jupyter notebook        # launch Jupyter
uv run jupyter nbconvert --to notebook --execute notebooks/<name>.ipynb  # run a notebook headlessly
```

## Key Dependency

- **gurobipy** — the Gurobi Python API. Import pattern used throughout: `from gurobipy import *`
- Gurobi must be installed system-wide with an active academic license (`gurobi.lic`).

## Notebook Conventions

Each notebook follows a two-stage modeling pattern:
1. **Hardcoded model** — variables, objective, and constraints written explicitly for clarity.
2. **Decoupled model** — data separated into lists/dicts, model rebuilt with `quicksum` and `addConstrs` for generality.

This progression is intentional for pedagogical purposes; preserve it when adding new examples.

## Repository Structure

```
notebooks/   # one .ipynb per OR problem/topic
prompt.md    # project intent notes (superseded by this file)
```
