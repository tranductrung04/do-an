# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build and Compile

This is a LaTeX report project. The main entry point is `main.tex`.

When running Python scripts or Python package commands, always use the repository virtual environment at `venv` rather than the system Python. For example, use `./venv/Scripts/python.exe <script>.py` on Windows/Git Bash.

Build the PDF from the repository root with:
```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The bibliography package is configured as `biblatex` with `backend=bibtex`, so use `bibtex main` rather than `biber main` unless the backend in `main.tex` is changed.

There is no application test suite or linter in this repository. Validation is done by compiling `main.tex` and checking the generated PDF/log output for LaTeX warnings or missing references.

## Code Architecture

- `main.tex` is the root document. It configures document class, Vietnamese UTF-8 support, page geometry, colors, captions, headers/footers, table-of-contents formatting, glossary printing, bibliography setup, and chapter inclusion.
- `cover.tex` contains the cover page and is included near the start of `main.tex` via `\subfile{cover}`.
- `Tu_viet_tat.tex` defines glossary/acronym entries loaded by `main.tex` before the document body.
- `Danh_sach_tai_lieu_tham_khao.bib` is the bibliography database used by `\addbibresource`; `main-blx.bib` is a generated biblatex helper file, not the source bibliography.
- `main.tex` includes `lstlisting` for code-listing formatting, but no `lstlisting.tex` file is currently present; add it or remove the include if compilation fails there.
- `chapter/` contains the report body as `subfiles`; edit chapter content there rather than in `main.tex` unless changing document structure or global formatting.
  - `0_1_starter.tex`: front-matter starter/acknowledgement text.
  - `1_introduction.tex`: Monolithic Architecture, Microservices Architecture, and Domain Driven Design background.
  - `2_architecture.tex`: E-Commerce microservices requirements, bounded contexts, services, APIs, databases, and system flows.
  - `3_ai_service.tex`: AI Service design for recommendation and product-advisory chatbot use cases.
  - `4_implement.tex`: implementation/design template sections for architecture, UI, database, build results, testing, and deployment.
- `img/` stores images currently present in the repository. `main.tex` also sets `\graphicspath{{figures/}{../figures/}}`, so figure references without paths are expected to resolve from a `figures/` directory if added.

## Packages and Conventions

- The document uses `\documentclass[a4paper,13pt,3p,twoside]{report}` and `\usepackage[utf8]{vietnam}` for Vietnamese text.
- Chapters are pulled in with the `subfiles` package; each chapter file should start with `\documentclass[../main.tex]{subfiles}` and wrap content in `\begin{document}` / `\end{document}`.
- References use `biblatex` with IEEE style and `backend=bibtex`.
- Glossary/acronym output uses `glossaries` with `\printnoidxglossaries`; entries belong in `Tu_viet_tat.tex`.
- The project color theme is defined in `main.tex` as `primary` (`HTML` value `d36d24`) and is reused for headings, captions, bullets, tables, and links.