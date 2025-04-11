# Programming in Theoretical Chemistry

[![Deploy](https://github.com/mitric-lab/programming_tc_ss24/workflows/Deploy/badge.svg)](https://github.com/mitric-lab/programming_tc_ss24/actions/workflows/deploy.yml)

Repository for the master course "Programming in Theoretical Chemistry"
in summer term 2025 at the University of Würzburg.

## Required Preprocessors
- [mdbook-admonish](https://github.com/tommilligan/mdbook-admonish)
- [mdBook-KaTeX](https://github.com/lzanini/mdbook-katex)
- [mdbook-numeq](https://github.com/yannickseurin/mdbook-numeq)
- [mdbook-chapter-zero](https://github.com/xmiaocat/mdbook-chapter-zero)

```bash
cargo install mdbook-admonish --version 1.15.0
mdbook-admonish install .
cargo install mdbook-katex --version 0.6.0
cargo install mdbook-numeq --version 0.3.0
cargo install --git https://github.com/xmiaocat/mdbook-chapter-zero#e50441d
```
