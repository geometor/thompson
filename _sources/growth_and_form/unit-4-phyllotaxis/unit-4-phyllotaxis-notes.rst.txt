:layout: book

.. _growth-and-form-unit-4-phyllotaxis-notes:

Unit IV: On Leaf-Arrangement, or Phyllotaxis — Notes & Concordance
==================================================================

.. rubric:: Critical Apparatus & GEOMETOR Cross-References — IV. Phyllotaxis

Scholarly Commentary & GEOMETOR Concordance (Unit IV)
-----------------------------------------------------

Direct Companion to `geometor/phyllotaxis` & `geometor/divine`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **From Tait (1872) and Thompson (1917) to Vogel (1979) and Turing (1952)**:

  * In `geometor/phyllotaxis`, planar capitula are modeled via Helmut Vogel's exact Fermat-spiral packing $r_n = c\sqrt{n},\; \theta_n = n \cdot \frac{2\pi}{\phi^2}$, where each seed occupies equal area $\pi c^2$ (a gnomonic area increment!).
  * :person:`Alan Turing <turing>` cited *On Growth and Form* in his 1952 morphogenesis paper (:cite:`turing:1952`) and left unfinished manuscripts specifically modeling cylindrical parastichy transitions $(m, n) \to (n, m+n)$ via reaction-diffusion inhibitor peaks implementing :person:`Hofmeister's <hofmeister>` gap-rule!

* **Why $\phi^{-2}$ Maximizes Packing Uniformity**: In `geometor/divine`, the golden ratio $\phi = [1; 1, 1, 1, \dots]$ has the smallest possible partial quotients ($a_k = 1$), making $\phi^{-2} = [0; 2, 1, 1, 1, \dots]$ the "most irrational" divergence angle in Hurwitz's Diophantine approximation sense. Rational angles $p/q$ stack primordia into $q$ radial spokes (orthostichies), wasting interstitial space; $\phi^{-2}$ avoids premature radial alignment across *all* scales simultaneously, so the visible contact parastichy pairs step cleanly up consecutive Fibonacci numbers $(5, 8) \to (8, 13) \to (13, 21) \to (21, 34) \to (34, 55) \to (55, 89)$ as apex radius grows relative to primordium size.
* **Bridge to Unit VII (Hambidge & Church)**: Both Thompson (pp. 646–650) and :person:`Jay Hambidge <hambidge>` (*The Diagonal*, Vol. I, No. 1, pp. 3–7, :cite:`hambidge:1920-diagonal`) draw directly on :person:`A. H. Church's <church>` Oxford sunflower plates (:cite:`church:1904`). Where Thompson emphasizes physical close-packing and cautions against mystical "sectio aurea" numerology, Hambidge translates Church's $(34, 55)$ and $(55, 89)$ log-spiral meshes into constructive Euclidean $\sqrt{5}$ and whirling-square area proportion.

Structured Concordance Loci in This Unit
----------------------------------------

**Schimper–Braun Fractions, Cylindrical Parastichy Lattices, and Golden Divergence** (*Ch. XIV (On Leaf-Arrangement, or Phyllotaxis)*, pp. 635–651)
   Demystifies botanical Fibonacci numbers through Bravais's cylindrical lattice, P. G. Tait's overlapping parastichy theorem, A. H. Church's equipotential spirals, and Hofmeister's mechanical apex rule.
   *Algebraic Invariants:* ``Δθ / 2π = 1 / φ² = (3 - √5)/2 ≈ 0.381966`` · ``F_{n+1} = F_n + F_{n-1}``

   * **geometor/phyllotaxis** (*Golden Angle 2π/φ², Cylindrical & Vogel Planar Parastichies*): Provides the verbatim 1917 historical foundation for geometor/phyllotaxis: continued-fraction convergents [0; 2, 1, 1, 1, ...] → φ⁻² and Tait's (m, n) → m + n lattice geometry.
   * **geometor/divine** (*Continued Fraction of φ & Fibonacci Convergents*): Explains why successive Fibonacci ratios F_k / F_{k+2} emerge automatically from mechanical close-packing without mystical teleology.
   * *Dynamic Symmetry Parallel:* The Diagonal (1919–1920), Vol. I, No. 1, pp. 1–7, 21 — A. H. Church's sunflower cross-curves (34/55, 55/89) as the biological fountainhead of Dynamic Symmetry
