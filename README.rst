=================
geometor-thompson
=================

Scholarly Digital Scriptorium Book Codex of **D'Arcy Wentworth Thompson's** *On Growth and Form* (**Cambridge University Press, 1st Edition, 1917**) paired with a **Dynamic Symmetry & Gnomonic Morphology Concordance** to **Jay Hambidge's** *The Elements of Dynamic Symmetry* (**Yale University Press, 1919–1920**).

Overview
--------

``geometor-thompson`` unites the physical-mathematical biology of D'Arcy Thompson with the constructive Euclidean proportion of Jay Hambidge across seven synchronized 3-track Book Codex units (*1917/1920 Text · Summary · Notes*):

1. **Unit I (`unit-1-magnitude`)**: *Prefatory Note, Epigraphs & Chapters I–IV* — Aquinas & Newton epigraphs, Galileo's Principle of Similitude & Square-Cube Law ($L^2$ vs. $L^3$), growth velocity curves, and cellular force fields.
2. **Unit II (`unit-2-cells-tissues`)**: *Chapters V–X* — Capillarity, Plateau's constant-mean-curvature surfaces, $120^\circ$ soap-film junctions (``X(13)`` in ``geometor/etc``, spread $s = 3/4$), the bee's rhombic dodecahedral cell & Maraldi tetrahedral angle $\arccos(-1/3) = 109^\circ 28' 16''$ (rational spread $s = 8/9$ in ``geometor/wildberger``), Kelvin's tetrakaidecahedron, and Haeckel's polyhedral Radiolaria.
3. **Unit III (`unit-3-equiangular-spiral`)**: *Chapters XI–XIII* — Descartes & Jakob Bernoulli's equiangular spiral ($r = a e^{\theta \cot\alpha}$), Aristotle & Hero's Theory of the Gnomon, the whirling-square golden rectangle ($\phi$) & Euclid IV.10 golden triangle, *Nautilus*, foraminifera, and horns.
4. **Unit IV (`unit-4-phyllotaxis`)**: *Chapter XIV* — Complete verbatim 1917 text of *On Leaf-Arrangement, or Phyllotaxis*: Schimper–Braun fractions, Fibonacci continued fractions converging to $\phi^{-2}$ ($137^\circ 30' 28''$), P. G. Tait's cylindrical parastichy lattices, and mechanical close-packing (historical companion to ``geometor/phyllotaxis``).
5. **Unit V (`unit-5-efficiency`)**: *Chapters XV–XVI* — Avian egg shell mechanics, Karl Culmann's Fairbairn crane & Hermann von Meyer's orthogonal trabecular trajectories in the human femur, and Claxton Fidler's cantilever vertebrate backbones.
6. **Unit VI (`unit-6-transformations`)**: *Chapter XVII & Epilogue* — Albrecht Dürer's proportion grids and Thompson's Theory of Transformations (Cartesian, oblique affine shear, radial, and coaxial-hyperbolic deformation meshes across Crustacea, *Argyropelecus* $\to$ *Sternoptyx*, *Diodon* $\to$ *Orthagoriscus*, *Archaeopteryx* $\to$ *Apatornis*, *Eohippus* $\to$ *Equus*, and primate skulls).
7. **Unit VII (`unit-7-dynamic-symmetry`)**: *Companion Concordance — Jay Hambidge (1919–1920)* — Root-rectangle compass unfolding ($\sqrt{1}, \sqrt{2}, \sqrt{3}, \sqrt{4}, \sqrt{5}$ with consecutive integer quadrances $Q = 1\dots 5$), Euclid Book X commensurability in square, orthogonal reciprocal diagonals, whirling squares, and A. H. Church's sunflower phyllotaxis.

Usage
-----

.. code-block:: bash

   # Verify SHA-256 digests of 1917 Cambridge & 1919-1920 Yale primary sources
   uv run --no-sync geometor-thompson verify

   # Regenerate 11 standalone .euclid-graphic SVG plates
   uv run --no-sync python scripts/build_figures.py

   # Compile all 26 synchronized :layout: book RST files
   uv run --no-sync geometor-thompson compile

   # Run test suite, linter, and Sphinx Book Codex build
   uv run --no-sync pytest
   ruff check src scripts tests
   publish build

License & Copyright Attestation
-------------------------------

Code, SVG constructions, and scholarly commentary are licensed under the MIT License. Primary texts derive strictly from the **1917 Cambridge University Press First Edition** and **1919–1920 Yale University Press** editions (100% Public Domain worldwide); Thompson's 1942 2nd edition and Bonner's 1961 abridgement are strictly excluded.
