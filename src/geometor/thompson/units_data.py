"""Structured unit definitions, Hambidge 1919–1920 primary texts, and scholarly apparatus tracks."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UnitSpec:
    """Complete specification for one 3-track synchronized unit in `docsrc/growth_and_form/`."""

    slug: str
    short_title: str
    title: str
    rubric: str
    chapters_1917: tuple[str, ...]
    summary_body: str
    notes_body: str
    custom_en_body: str = ""


_HAMBIDGE_1920_EN_BODY = """.. _hambidge-1920-foreword:

I. Static and Dynamic Symmetry in Nature and Greek Art
------------------------------------------------------

.. rubric:: Jay Hambidge — *Dynamic Symmetry: The Greek Vase* (Yale University Press, 1920, Foreword) & *The Diagonal* (Vol. I, No. 1, Nov. 1919, pp. 1–2)

.. folio:: Vase pp. 7–8
   :page: 7

Some twenty years ago, the writer, being impressed by the incoherence of modern design and convinced that there must exist in nature some correlating principle which could give artists a control of areas, undertook a comparative study of the bases of all design, both in nature and in art. This labor resulted in the determination of two types of symmetry or proportion, one of which possessed qualities of activity, the other of passivity. For convenience, the active type was termed :term:`dynamic symmetry <dynamic-symmetry>`, the other, :term:`static symmetry <static-symmetry>`. It was found that the passive was the type which was employed most naturally by artists, either consciously or unconsciously; in fact, no design which would be recognized as such—unless, indeed, it were dynamic—would be possible without the use, in some degree, of this passive or static type. It is apparent in nature in certain crystal forms, radiolaria, diatoms, flowers and seed pods, and has been used consciously in art at several periods.

The principle of dynamic symmetry is manifest in shell growth and in leaf distribution in plants. A study of the basis of design in art shows that this active symmetry was known to but two peoples, the Egyptians and the Greeks; the latter only having developed its full possibilities for purposes of art. The writer believes that he has now recovered, through study of natural form and shapes in Greek and Egyptian art, this principle for the proportioning of areas.

.. folio:: Diagonal p. 1
   :page: 1

The synthetic use of these design principles is simple. The Greeks probably used a string held in the two hands. The *Harpedonaptae* or rope-stretchers of Egypt had no other instrument for orientating and surveying or laying out temple plans. When temple and tomb building began, it became necessary to establish a right angle and lay out a full-sized plan on the ground. The right angle was determined by marking off twelve units on the rope, four of these units forming one side, three the other, and five the hypotenuse of the triangle, a method which has persisted to our day. This was the origin of the historic "cording of the temple." At some time during the Sixth or Seventh Century B.C. the Greeks obtained from Egypt knowledge of this manner of correlating elements of design. In their hands it was highly perfected as a practical geometry, and for about three hundred years it provided the basic principle of design for the finest art of the Classic period. Euclidean geometry (:cite:`euclid:elements`) gives us the Greek development of the idea in pure mathematics; but the secret of its artistic application completely disappeared. Its recovery has given us dynamic symmetry—a method of establishing the relationship of areas in design-composition.

.. _hambidge-1920-plant:

II. The Dynamic Symmetry of the Plant (Sunflower Phyllotaxis)
-------------------------------------------------------------

.. rubric:: Jay Hambidge — *The Diagonal* (Yale University Press, Vol. I, No. 1, Nov. 1919, pp. 3–7)

.. folio:: Diagonal pp. 3–5
   :page: 3

It has long been known that a peculiar series of numbers is connected with the phenomenon of the orderly distribution of the leaves of plants. The series is: $1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144$, etc. This is called a summation series from the fact that each term is composed of the sum of the two preceding terms. For those who may be interested in the subject from the botanical standpoint reference is made to the elaborate work of Professor :person:`A. H. Church <church>` of Oxford on *Phyllotaxis in Relation to Mechanical Laws* (:cite:`church:1904`). This series of numbers in reality represents the symmetry of the plant in the sense that the word is used as "analogy," which is its Greek meaning. From this series we obtain the entire machinery of dynamic symmetry, which applies not only to the architecture of the plant but to the architecture of man.

This summation series of numbers, because of its character, represents a ratio, i.e., it is a geometrical progression. This ratio may be obtained by dividing one term into another, such as $34$ into $55$. The series does not represent the phenomenon exactly, but only so far as it is representable by whole numbers. A much closer representation would be obtained by a substitute series where the cascade ratio is $: 1.618034\\dots$ (the golden ratio $\\phi = \\frac{1 + \\sqrt{5}}{2}$).

In the sunflower head used by Professor :person:`Church <church>` to exhibit the :term:`phyllotaxis` phenomena, the seed pods are distributed in a rhythmic, intersecting series of curves. Closer inspection shows that these curves are :term:`logarithmic or equiangular spirals <equiangular-spiral>` arrangeable in two intersecting systems winding in opposite directions (:term:`parastichies <parastichy>`). A normal sunflower disk five or six inches in diameter will exhibit $55$ curves winding in one direction and $89$ crossing them in the other; a smaller head exhibits $34$ and $55$; a very large head $89$ and $144$. Each cross-curve pair consists of two adjacent terms of the summation series, and the seeds themselves expand radially from the center by gnomonic enlargement so that their rhombic packing meshes preserve constant angular form from center to rim.

.. _hambidge-1920-root-five:

III. The Root-Five Rectangle and the Rectangle of the Whirling Squares
----------------------------------------------------------------------

.. rubric:: Jay Hambidge — *The Elements of Dynamic Symmetry*, Lesson I (*The Diagonal*, Vol. I, No. 1, Nov. 1919, pp. 15–17)

.. folio:: Diagonal pp. 15–17
   :page: 15

The basic shape derived from this summation ratio of plant growth and human proportion is a rectangle which has been given the name "root-five" (:term:`root-rectangle`). It is so called because the relationship between the end and side is as one to the square root of five, $1 : 2.2360\\dots$ ($1 : \\sqrt{5}$). As a length unit the end cannot be divided into the side of a root-five rectangle, because the square root of five is a never-ending fraction. We naturally think of such a relationship as irrational. The Greeks, however, said that such lines were *not* irrational in power, because they were :term:`commensurable or measurable in square <commensurable-in-square>`. This is really the great secret of Greek design. In understanding this measurableness of area instead of line the Greek artists had command of an infinity of beautiful shapes which modern artists are unable to use. The relationship between the end and side of a root-five rectangle is a relationship of area and not line, because as lengths one cannot be divided into the other, *but the square constructed on the end of a root-five rectangle is exactly one-fifth of the area of the square constructed on the side*.

**Construction of the Root-Five Rectangle.** Draw a unit square $BC$ and bisect one side at $A$. Draw a line from $A$ to an opposite corner $B$ (having length $\\frac{\\sqrt{5}}{2}$) and use this line as a radius to describe a semicircle cutting the extended baseline at $D$ and $E$. Then $DE$ is twice the length of $AB$, namely $\\sqrt{5}$. Complete the rectangle on $DE$: it is composed of the central unit square $CB$ flanked by two reciprocal golden rectangles of width $\\frac{\\sqrt{5}-1}{2} = 0.6180\\dots$ ($\\sqrt{5} = 1 + 2 \\phi^{-1}$).

**The Rectangle of the Whirling Squares.** The root-five rectangle produces a great number of other shapes which are measurable in area with themselves and with the parent shape. The principal one of these is that which is called the :term:`rectangle of the whirling squares <whirling-square-rectangle>`. Draw a unit square $CB$, bisect its base at $A$, draw the diagonal radius $AB$ to an upper corner, and swing $AB$ down to $E$ on the extended baseline. Complete the rectangle $DE$: its ratio is $1 : \\frac{1 + \\sqrt{5}}{2} = 1 : 1.6180\\dots$, equal to the root-five rectangle minus one of its two flanking $0.6180$ rectangles.

**The Reciprocal and the Whirling Gnomons.** A process connected with the science of plan-making which was thoroughly understood by the Greeks was that of determining the :term:`reciprocal of a rectangle <reciprocal-rectangle>`. Briefly, the reciprocal of a rectangle is a similar shape, custom-scaled so that the *end* of the larger rectangle becomes the *side* of the smaller reciprocal. All Greek constructions for reciprocals depend upon the fundamental theorem that *the diagonal of a reciprocal always cuts the diagonal of the major shape at right angles* ($90^\\circ$).

In a whirling-square rectangle ($1 : \\phi$), the reciprocal has area $\\frac{1}{\\phi} = \\phi - 1 = 0.6180\\dots$, and the area in excess of the reciprocal is an exact unit square (:term:`gnomon`). If we draw a diagonal of the whole rectangle and a perpendicular diagonal of its reciprocal, and continue cutting off successive reciprocals inside the remainder, the cut-off squares $1, 2, 3, 4, 5, \\dots$ arrange themselves in a spiral whirling to infinity around the intersection pole or "eye" $O$—matching :person:`D'Arcy Thompson's <thompson>` gnomonic construction in Chapter XI (Fig. 252). Also, two whirling-square rectangles ($1.6180 + 1.6180 = 3.2360$) overlapping to the extent of a central unit square ($3.2360 - 1 = 2.2360$) reconstitute the parent $\\sqrt{5}$ rectangle!

.. _hambidge-1920-root-rectangles:

IV. The Root Rectangles ($\\sqrt{1}, \\sqrt{2}, \\sqrt{3}, \\sqrt{4}, \\sqrt{5}$) and Euclidean Commensurability in Square
--------------------------------------------------------------------------------------------------------------------------

.. rubric:: Jay Hambidge — *The Elements of Dynamic Symmetry*, Lesson II (*The Diagonal*, Vol. I, No. 1, Nov. 1919, pp. 18–21)

.. folio:: Diagonal pp. 18–21
   :page: 18

The area of a square described on the diagonal of a square is double the area of the smaller square. The rectangle obtained by taking the side of a unit square as end and its diagonal as side has ratio $1 : \\sqrt{2}$ ($1 : 1.4142\\dots$). The square on the end of this rectangle is one-half the area of the square on the side. The end and side of a root-two rectangle are incommensurable, not measurable one by the other. **They are, however, commensurable in square.** (See the Greek classification of incommensurables, :person:`Euclid <euclid>`, *Elements*, Book X, Def. 2, :cite:`euclid:elements`.)

For purposes of design the most important element of a rectangle is its diagonal. The area of the square upon the diagonal of any rectangle is equal to the areas of a square upon its end and a square upon its side. This important fact is the 47th proposition of the first book of :person:`Euclid <euclid>` and has been picturesquely described by :person:`Kepler <kepler>` as "a measure of gold."

.. picture:: /_static/figures/fig_hambidge_root_rectangles.svg
   :alt: Root-rectangle compass unfolding from unit square through sqrt(2), sqrt(3), sqrt(4), sqrt(5) with integer quadrances Q = 1..5, alongside perpendicular reciprocal diagonal intersection at E.
   :caption: **Dynamic Symmetry Root-Rectangle Unfolding and Reciprocal Orthogonality (Hambidge, *The Diagonal*, Vol. I, pp. 18–19).** Swinging each rectangle's diagonal down to the baseline unfolds $\\sqrt{1}, \\sqrt{2}, \\sqrt{3}, \\sqrt{4}=2, \\sqrt{5}$ with consecutive integer side quadrances $Q = 1, 2, 3, 4, 5$, while the reciprocal diagonal $CD$ meets the main diagonal $AB$ at $90^\\circ$.

By swinging the diagonal of the $\\sqrt{2}$ rectangle down to the baseline with a compass, we obtain the $\\sqrt{3}$ rectangle ($1 : 1.7320\\dots$), whose diagonal in turn yields $\\sqrt{4} = 2$ (composed of two unit squares), and the diagonal of the $1 : 2$ rectangle yields the $\\sqrt{5}$ rectangle ($1 : 2.2360\\dots$).

The element of the rectangle second in importance to the diagonal is the diagonal of a :term:`reciprocal <reciprocal-rectangle>`. The reciprocal of a rectangle is obtained by dividing the side into the end ($1 / \\sqrt{n}$):

* The reciprocal of a $\\sqrt{2}$ rectangle has ratio $1 / \\sqrt{2} = 0.7071\\dots$ and divides the parent $\\sqrt{2}$ rectangle into **two** equal similar $\\sqrt{2}$ rectangles.
* The reciprocal of a $\\sqrt{3}$ rectangle has ratio $1 / \\sqrt{3} = 0.5773\\dots$ and divides the parent $\\sqrt{3}$ rectangle into **three** equal similar $\\sqrt{3}$ rectangles.
* The reciprocal of a $\\sqrt{4}$ ($1 : 2$) rectangle has ratio $1 / 2 = 0.5000$ and divides the parent rectangle into **four** equal $1 : 2$ rectangles.
* The reciprocal of a $\\sqrt{5}$ rectangle has ratio $1 / \\sqrt{5} = 0.4472\\dots$ and divides the parent $\\sqrt{5}$ rectangle into **five** equal similar $\\sqrt{5}$ rectangles.

Three simple classical constructions establish the reciprocal of any dynamic rectangle: (1) applying a unit square on the end of the rectangle so its inner side cuts the main diagonal at $D$, determining the reciprocal end; (2) erecting a perpendicular $BC$ to the main diagonal $AB$ at vertex $B$; or (3) describing a semicircle on the end of the rectangle cutting the main diagonal at $C$ (Euclid III.31), from which the line through $C$ from the opposite end corner traces the diagonal of the reciprocal.

This strange power of modulation possessed by dynamic symmetry is shown in the symmetry of the plant. Professor :person:`Church <church>`, in describing the phyllotaxis of the sunflower, speaks of the change in cross-curve numbers from the flowers lowest on the stalk to those highest and mentions the pairs $(13, 21)$, $(21, 34)$, $(34, 55)$, $(55, 89)$; these combinations all produce the same ratio, and modulate seamlessly within the root-five and whirling-square system.
"""


UNITS: tuple[UnitSpec, ...] = (
    UnitSpec(
        slug="unit-1-magnitude",
        short_title="I. Magnitude & Growth",
        title="Unit I: Mathematical Morphology, Magnitude, and Rate of Growth",
        rubric="1917 Cambridge First Edition — Prefatory Note, Epigraphs & Chapters I–IV (pp. v–vi, 1–200)",
        chapters_1917=("prefatory", "epigraphs", "ch-1", "ch-2", "ch-3", "ch-4"),
        summary_body="""Overview of Unit I (Prefatory Note & Chapters I–IV)
---------------------------------------------------

Unit I establishes the philosophical, dimensional, and physiological foundations of :person:`D'Arcy Wentworth Thompson's <thompson>` *On Growth and Form* (:cite:`thompson:1917`), reproducing verbatim the Prefatory Note, the 1917 Scholastic-mechanical epigraphs, and Chapters I–IV:

1. **Prefatory Note & Epigraphs (pp. v–vi, xvi)**: Framing the treatise as "all preface," Thompson unites :person:`Stephen Hales <hales>`, :person:`St. Thomas Aquinas <aquinas>` (*De Potentia Dei*, Q. 3, a. 11, :cite:`aquinas:depot`), and :person:`Sir Isaac Newton <newton>` (*Principia* Preface) to argue that corporeal organic forms arise directly from physical forces acting on matter.
2. **Chapter I — Introductory (pp. 1–15)**: Answering :person:`Immanuel Kant's <kant>` dictum that chemistry and biology become strict sciences only insofar as mathematics enters them, Thompson critiques purely historical or teleological Darwinism when divorced from physical mechanics and efficient causes.
3. **Chapter II — On Magnitude (pp. 16–49)**: Develops the :term:`Principle of Similitude <similitude>` and :person:`Galileo's <galileo>` :term:`Square-Cube Law <square-cube-law>` (:cite:`galileo:1638`). Because surface areas (muscle cross-section, bone strength, gill/gut absorption, wing area, capillary :term:`surface tension <surface-tension>`) vary as $L^2$ while mass and weight vary as $L^3$, absolute spatial scale partitions the living world into distinct physical regimes—gravity-dominated vertebrates, capillarity-dominated insects and protists, and Brownian-motion-governed cocci.
4. **Chapter III — The Rate of Growth (pp. 50–155)**: Investigates growth velocity curves ($dL/dt$, $dW/dt$), Quetelet's human stature curves, autocatalytic S-shaped trajectories, seasonal periodicities, and differential growth gradients—the temporal engine that drives Chapter XVII's coordinate deformations.
5. **Chapter IV — On the Internal Form and Structure of the Cell (pp. 156–200)**: Models the mitotic spindle, centrosomes, and karyokinetic asters via physical lines of force (magnetic, electrostatic, osmotic, and hydrodynamic tension fields) within the protoplasmic colloid.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit I)
----------------------------------------------------

1917 Edition Provenance & Epigraph Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **1917 First Edition Structure**: Verified directly against 300 DPI page scans of the 1917 Cambridge University Press imprint (`ongrowthform1917thom`), the First Edition opens with :person:`Stephen Hales's <hales>` *Vegetable Staticks* epigraph preceding the Prefatory Note (dated *University College, Dundee, December, 1916*) and places the celebrated triad of :person:`Aquinas <aquinas>`, :person:`Newton <newton>`, and J. H. Jellett on p. xvi immediately facing Chapter I (p. 1). (In the 1942 Second Edition—strictly excluded from this codex—Chapter I was heavily rewritten and split.)
* **Link to `geometor/aquinas`**: Thompson's quotation from :cite:`aquinas:depot` (*"Cum formarum naturalium et corporalium esse non consistat nisi in unione ad materiam..."*, which he had earlier introduced in his 1911 Portsmouth British Association address, :cite:`thompson:1911`) anchors mathematical morphology in Aristotelian–Thomistic natural philosophy: physical agents transmuting matter suffice to account for natural configuration without appealing to vitalistic *entelechies*.

Dimensional Scaling & Euclidean Similitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Link to `geometor/euclid` & `geometor/elements`**: Thompson's dimensional equations $S \\propto L^2$ and $V \\propto L^3$ rest directly on :person:`Euclid's <euclid>` Book VI (Props. 19–20, duplicate ratio of similar polygons) and Book XI (Prop. 33, triplicate ratio of similar parallelepipeds; :cite:`euclid:elements`, :cite:`heath:1908`).
* **Froude's Law & Locomotion**: Thompson's remarkable proof (pp. 29–35) that maximal jumping height and stride mechanics remain nearly scale-invariant across flea, kangaroo, and horse anticipates modern biomechanical scaling and dimensional analysis.
* **Differential Growth as Precursor to Transformations**: Chapter III's demonstration that different anatomical axes possess distinct growth rates ($dx/dt \\neq dy/dt$) supplies the exact ontogenetic justification for both Chapter XI's :term:`gnomonic <gnomon>` shell spirals (where ratios of marginal growth remain constant) and Chapter XVII's :term:`method of coordinates <method-of-coordinates>` (where growth gradients vary smoothly across space).
""",
    ),
    UnitSpec(
        slug="unit-2-cells-tissues",
        short_title="II. Cells, Foams & Honeycomb",
        title="Unit II: Capillarity, Cellular Foams, the Bee's Cell, and Spicular Skeletons",
        rubric="1917 Cambridge First Edition — Chapters V–X (pp. 201–492)",
        chapters_1917=("ch-5", "ch-6", "ch-7", "ch-8", "ch-9", "ch-10"),
        summary_body="""Overview of Unit II (Chapters V–X)
----------------------------------

Unit II traces the geometry of :term:`surface tension <surface-tension>`, minimal area partitions, and biomineralized skeletons across six closely linked chapters of the 1917 First Edition (pp. 201–492):

1. **Chapter V — The Forms of Cells (pp. 201–276)**: Applies the Laplace–Young capillary law $\\Delta P = T(1/R_1 + 1/R_2)$ and :person:`Joseph Plateau's <plateau>` six axisymmetric surfaces of constant :term:`mean curvature <mean-curvature>`—plane, sphere, cylinder, :term:`catenoid`, :term:`unduloid`, and :term:`nodoid` (:cite:`plateau:1873`)—to solitary protists (*Lagena*, *Amoeba*, ciliates, trypanosomes, and red blood corpuscles).
2. **Chapter VI — A Note on Adsorption (pp. 277–292)**: Explains Gibbs–Thomson interfacial concentration at cell membranes, paving the way for localized pellicles, cell walls, and mineral spicule deposition along liquid edges.
3. **Chapter VII — The Forms of Tissues, or Cell-Aggregates (pp. 293–345)**: Establishes :term:`Plateau's laws <plateau-laws>` for 2D and 3D cellular froths:

   * Planar triple junctions meet at $120^\\circ$ (:term:`Fermat–Torricelli point <fermat-torricelli-point>` `X(13)`), yielding hexagonal epithelia.
   * **The Bee's Cell (pp. 327–336)**: Traces the two-century mathematical drama from :person:`Pappus <pappus>` and :person:`Kepler <kepler>` (:cite:`kepler:1611`) through :person:`Maraldi <maraldi>` (:cite:`maraldi:1712`), :person:`Réaumur <reaumur>`, :person:`König <koenig>`, :person:`Maclaurin <maclaurin>` (:cite:`maclaurin:1743`), and :person:`Boscovich <boscovich>` (:cite:`boscovich:1760`), demonstrating that the three-rhombus pyramidal cap of the honeycomb with :term:`Maraldi angle <maraldi-angle>` $\\arccos(-1/3) = 109^\\circ 28' 16''$ arises automatically from mutual compression and soap-film tension rather than geometric calculation by the bee.
   * **Parenchyma & Kelvin's Foam (pp. 336–345)**: Connects Plateau's wire-cube soap film (Fig. 134) to :person:`Lord Kelvin's <kelvin>` space-filling 14-hedral :term:`tetrakaidecahedron` (:cite:`kelvin:1887`).

4. **Chapter VIII — The Forms of Tissues, continued (pp. 346–410)**: Derives Sachs's law of orthogonal cell-plate intersection and Errera's minimal-area cleavage partitions in dividing embryos, cambium, and cork.
5. **Chapter IX — On Concretions, Spicules, and Spicular Skeletons (pp. 411–487)**: Shows how sponge triradiate ($120^\\circ$) and tetraradiate ($109^\\circ 28'$) :term:`spicules <spicule>` crystallize within intercellular Plateau channels, and reinterprets :person:`Ernst Haeckel's <haeckel>` *Challenger* Radiolaria (:cite:`haeckel:1887`) via spherical foam geometry and Euler's polyhedral theorem.
6. **Chapter X — A Parenthetic Note on Geodetics (pp. 488–492)**: Explains helical thickenings in plant vessels and *Spirogyra* chloroplasts as geodesics minimizing elastic bending energy on cylindrical walls.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit II)
-----------------------------------------------------

Rational Trigonometry of Soap Films (`geometor/etc` & `geometor/wildberger`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **2D Triple Junctions (`X(13)` & Spread $s = 3/4$)**: Three co-planar soap films spanning vertices $A, B, C$ meet at the first Fermat–Torricelli–Steiner point `X(13)` catalogued in `geometor/etc`. In :person:`Wildberger's <euclid>` Rational Trigonometry (`geometor/wildberger`), the $120^\\circ$ equilibrium angle requires zero transcendental functions: its exact algebraic :term:`spread` is $s = \\sin^2(120^\\circ) = 3/4 \\in \\mathbb{Q}$.
* **3D Quadruple Junctions & the Maraldi Angle (Spread $s = 8/9$)**: Four liquid edges meeting at a spatial foam vertex—or the three rhombi meeting at the trihedral apex of the bee's cell (verified on 300 DPI scan p. 330, Fig. 132)—subtend $\\theta = \\arccos(-1/3) \\approx 109^\\circ 28' 16.39''$. Since $\\cos^2\\theta = 1/9$, the tetrahedral Maraldi angle has exact rational spread:

  $$s = 1 - \\cos^2\\theta = \\frac{8}{9}$$

  Each face of :person:`Kepler's <kepler>` :term:`rhombic dodecahedron` has short-to-long diagonal ratio $1 : \\sqrt{2}$ (diagonal :term:`quadrance` ratio $1 : 2$), linking Unit II directly to :person:`Jay Hambidge's <hambidge>` root-two rectangle in Unit VII!

Euler's Polyhedral Law & Haeckel's *Aulonia hexagona* (`geometor/euclid` & `geometor/pacioli`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Impossible Pure-Hexagon Spheres (Ch. IX, p. 473)**: One of Thompson's sharpest mathematical proofs refutes :person:`Haeckel's <haeckel>` claim that the radiolarian *Aulonia hexagona* builds a closed sphere of uniform hexagons. For any 3-valent convex polyhedral mesh ($3V = 2E$) satisfying Euler's formula $V - E + F = 2$, summing face degrees $F = \\sum F_k$ and $2E = \\sum k F_k$ gives the topological invariant:

  $$\\sum_{k \\ge 3} (6 - k) F_k = 12$$

  Because $(6 - 6) = 0$, hexagons contribute *nothing* to the curvature defect $12$: every closed hexagonal cage (whether radiolarian silica, viral capsid, geodesic dome, or $\\mathrm{C}_{60}$ fullerene) *must* incorporate pentagons (e.g., exactly $12$ pentagons when $k \\in \\{5, 6\\}$), bridging directly to Book XIII of `geometor/euclid` and Leonardo's polyhedra in `geometor/pacioli`.
""",
    ),
    UnitSpec(
        slug="unit-3-equiangular-spiral",
        short_title="III. Equiangular Spiral & Gnomons",
        title="Unit III: The Logarithmic Spiral, Hero's Gnomon, Foraminifera, and Horns",
        rubric="1917 Cambridge First Edition — Chapters XI–XIII (pp. 493–634)",
        chapters_1917=("ch-11", "ch-12", "ch-13"),
        summary_body="""Overview of Unit III (Chapters XI–XIII)
---------------------------------------

Unit III presents verbatim the geometric centerpiece of *On Growth and Form*—Chapter XI (*The Logarithmic Spiral*, pp. 493–586)—together with its companion chapters on Foraminifera (Chapter XII, pp. 587–611) and Horns, Teeth, and Torsion (Chapter XIII, pp. 612–634):

1. **Chapter XI — The Logarithmic Spiral (pp. 493–586)**:

   * Contrasts the uniform arithmetic spiral of :person:`Archimedes <archimedes>` ($r = a\\theta$, constant whorl width, changing shape; :cite:`archimedes:spirals`) with the geometric or :term:`equiangular spiral <equiangular-spiral>` of :person:`Descartes <descartes>` and :person:`Jakob Bernoulli <bernoulli-jakob>` ($r = a e^{\\theta \\cot\\alpha}$, constant tangent angle $\\alpha$, geometrically increasing whorl widths; :cite:`bernoulli:1692`).
   * **Theory of the Gnomon (pp. 508–514)**: Recovers :person:`Aristotle's <aristotle>` (*Categories* 15a30, :cite:`aristotle:cat`) and :person:`Hero of Alexandria's <hero>` (*Definitiones* 58, :cite:`hero:def`) doctrine of the :term:`gnomon`: whenever dead material (shell, horn, tooth, claw) grows by terminal accretion without remodeling older parts, preservation of geometric similarity requires each increment to be a gnomon to the existing form, generating an equiangular spiral.
   * Illustrates gnomonic subdivision on the $\\sqrt{2}$ rectangle (Fig. 251), the :term:`whirling-square golden rectangle <whirling-square-rectangle>` ($1 : \\phi$, Fig. 252), and :person:`Euclid's <euclid>` IV.10 :term:`golden triangle <golden-triangle>` ($36^\\circ\\text{–}72^\\circ\\text{–}72^\\circ$, Fig. 254).
   * Formulates the 3D helicospiral geometry of turbinated gastropods, bivalves, ammonite sutures, and *Nautilus* septa in three parameters $(\\alpha, \\beta, \\gamma)$ building upon Canon :person:`Henry Moseley <moseley>` (:cite:`moseley:1838`).

2. **Chapter XII — The Spiral Shells of the Foraminifera (pp. 587–611)**: Shows how discrete pulsatile protoplasmic extrusions harden by surface-tension equilibrium into linear (*Nodosaria*), textularian, and logarithmic (*Rotalia*, *Globigerina*, *Nummulites*) chamber sequences.
3. **Chapter XIII — The Shapes of Horns, and of Teeth or Tusks: with a Note on Torsion (pp. 612–634)**: Extends unbalanced axial growth gradients and spatial torsion ($\\tau$) to sheep and antelope horns, narwhal tusks, rodent incisors, nails, and beaks.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit III)
------------------------------------------------------

Gnomonic Self-Similarity Across `aristotle`, `euclid`, `divine`, and Hambidge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **1917 Folio Verification (pp. 509–512)**: Direct 300 DPI scan inspection of pp. 510–511 (`thompson_gnomon-530.png`, `531.png`) confirms Thompson's Greek citation `(σχηματογραφεῖν)` of Pythagorean figurate numbers alongside Figs. 251–254:

  * **Fig. 251**: Halving a $1 : \\sqrt{2}$ rectangle yields a $1/\\sqrt{2}$ gnomon (the exact principle of ISO paper sizes and :person:`Hambidge's <hambidge>` root-two reciprocal!).
  * **Fig. 252**: Removing nested unit squares from the golden rectangle $1 : \\phi$ ($\\phi = \\frac{1 + \\sqrt{5}}{2}$, :person:`Euclid <euclid>` II.11 & VI.30 in `geometor/euclid` and `geometor/divine`) leaves self-similar golden rectangles rotated by $90^\\circ$ ("whirling squares"), whose homologous vertices lie on an equiangular spiral around the intersection pole $O$ of perpendicular diagonals.
  * **Fig. 254**: Bisecting the $72^\\circ$ base angle of Euclid's IV.10 sublime triangle ($36^\\circ\\text{–}72^\\circ\\text{–}72^\\circ$) detaches an obtuse $108^\\circ\\text{–}36^\\circ\\text{–}36^\\circ$ gnomon while leaving a smaller $36^\\circ\\text{–}72^\\circ\\text{–}72^\\circ$ golden triangle.

* **Chronological Bridge to Jay Hambidge (1917 → 1919)**: Thompson published Chapter XI's "whirling squares" analysis in 1917 (drawing also on Sir Theodore Cook's *Curves of Life*, 1914); two years later, :person:`Jay Hambidge <hambidge>` systematized the whirling-square rectangle and its parent $\\sqrt{5}$ rectangle in *The Diagonal* (:cite:`hambidge:1920-diagonal`, Nov. 1919) as the cornerstone of Greek Dynamic Symmetry (Unit VII).

Time-Invariance of Accretionary Shells
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Why *Nautilus* Is Not Golden**: Thompson carefully cautions against mystical claims that every mollusc shell has the golden ratio $\\phi$ as its whorl-expansion factor! Rather, *any* constant ratio of tangential to radial growth produces a genuine equiangular spiral $r = a e^{\\theta \\cot\\alpha}$: in *Nautilus pompilius* $\\alpha \\approx 80^\\circ$ ($e^{2\\pi\\cot\\alpha} \\approx 3.0\\text{–}3.2$), in *Planorbis* $\\alpha \\approx 85^\\circ$, and in flat opercula or *Haliotis* $\\alpha$ drops to $30^\\circ\\text{–}45^\\circ$. The invariant law is Hero's gnomon itself, of which $\\phi$ is the canonical discrete quadratic exemplar.
""",
    ),
    UnitSpec(
        slug="unit-4-phyllotaxis",
        short_title="IV. Phyllotaxis",
        title="Unit IV: On Leaf-Arrangement, or Phyllotaxis",
        rubric="1917 Cambridge First Edition — Chapter XIV (pp. 635–651, Complete Verbatim Text)",
        chapters_1917=("ch-14",),
        summary_body="""Overview of Unit IV (Chapter XIV — Complete Verbatim Text)
----------------------------------------------------------

Unit IV presents the complete, unabridged 1917 text of **Chapter XIV: On Leaf-Arrangement, or Phyllotaxis** (pp. 635–651), the direct historical companion to `geometor/phyllotaxis`:

1. **Cylindrical vs. Discoidal Formulations (pp. 635–638)**: Unifies the cylindrical helical view of :person:`Schimper <schimper>`, :person:`Braun <braun>`, and the brothers :person:`Bravais <bravais>` (:cite:`bravais:1837`, fir-cones and palm stems) with the planar logarithmic-spiral capitulum view of :person:`A. H. Church <church>` (:cite:`church:1904`, sunflower heads).
2. **The Schimper–Braun Series & Continued Fractions (pp. 638–642)**: Analyzes the principal fractional divergences:

   $$\\frac{1}{2},\\; \\frac{1}{3},\\; \\frac{2}{5},\\; \\frac{3}{8},\\; \\frac{5}{13},\\; \\frac{8}{21},\\; \\frac{13}{34}, \\dots$$

   generated by the unit continued fraction $\\frac{1}{2 + \\frac{1}{1 + \\frac{1}{1 + \\dots}}}$, converging to $\\phi^{-2} = \\frac{3 - \\sqrt{5}}{2} \\approx 0.381966$ (the golden :term:`divergence angle <divergence-angle>` $137^\\circ 30' 28''$), alongside accessory Lucas/secondary series ($\\frac{1}{4}, \\frac{1}{5}, \\frac{2}{9}\\dots$).
3. **P. G. Tait's Cylindrical Parastichy Lattice (pp. 643–646, Fig. 325)**: Reproduces :person:`Peter Guthrie Tait's <tait>` 1872 geometric proof (:cite:`tait:1872`) that whenever a cylindrical point-lattice exhibits two intersecting contact-spiral families (:term:`parastichies <parastichy>`) of orders $m$ and $n$ winding in opposite directions, the next steeper intermediate family necessarily has order $m + n$—automatically generating the Fibonacci recurrence without assuming a single physical "genetic spiral."
4. **Critique of Teleology & Mechanical Close-Packing (pp. 646–651)**: Rejects Darwinian sunlight-optimization myths (noting deep-sea hydroids, subterranean bulbs, and tightly closed pine cones show identical Fibonacci numbers) in favor of :person:`Hofmeister's <hofmeister>` mechanical gap-rule (:cite:`hofmeister:1868`), Schwendener's mutual contact pressure, and Church's orthogonal log-spiral growth trajectories.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit IV)
-----------------------------------------------------

Direct Companion to `geometor/phyllotaxis` & `geometor/divine`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **From Tait (1872) and Thompson (1917) to Vogel (1979) and Turing (1952)**:

  * In `geometor/phyllotaxis`, planar capitula are modeled via Helmut Vogel's exact Fermat-spiral packing $r_n = c\\sqrt{n},\\; \\theta_n = n \\cdot \\frac{2\\pi}{\\phi^2}$, where each seed occupies equal area $\\pi c^2$ (a gnomonic area increment!).
  * :person:`Alan Turing <turing>` cited *On Growth and Form* in his 1952 morphogenesis paper (:cite:`turing:1952`) and left unfinished manuscripts specifically modeling cylindrical parastichy transitions $(m, n) \\to (n, m+n)$ via reaction-diffusion inhibitor peaks implementing :person:`Hofmeister's <hofmeister>` gap-rule!

* **Why $\\phi^{-2}$ Maximizes Packing Uniformity**: In `geometor/divine`, the golden ratio $\\phi = [1; 1, 1, 1, \\dots]$ has the smallest possible partial quotients ($a_k = 1$), making $\\phi^{-2} = [0; 2, 1, 1, 1, \\dots]$ the "most irrational" divergence angle in Hurwitz's Diophantine approximation sense. Rational angles $p/q$ stack primordia into $q$ radial spokes (orthostichies), wasting interstitial space; $\\phi^{-2}$ avoids premature radial alignment across *all* scales simultaneously, so the visible contact parastichy pairs step cleanly up consecutive Fibonacci numbers $(5, 8) \\to (8, 13) \\to (13, 21) \\to (21, 34) \\to (34, 55) \\to (55, 89)$ as apex radius grows relative to primordium size.
* **Bridge to Unit VII (Hambidge & Church)**: Both Thompson (pp. 646–650) and :person:`Jay Hambidge <hambidge>` (*The Diagonal*, Vol. I, No. 1, pp. 3–7, :cite:`hambidge:1920-diagonal`) draw directly on :person:`A. H. Church's <church>` Oxford sunflower plates (:cite:`church:1904`). Where Thompson emphasizes physical close-packing and cautions against mystical "sectio aurea" numerology, Hambidge translates Church's $(34, 55)$ and $(55, 89)$ log-spiral meshes into constructive Euclidean $\\sqrt{5}$ and whirling-square area proportion.
""",
    ),
    UnitSpec(
        slug="unit-5-efficiency",
        short_title="V. Eggs, Bone & Efficiency",
        title="Unit V: Hollow Structures, Culmann's Crane, and Mechanical Efficiency",
        rubric="1917 Cambridge First Edition — Chapters XV–XVI (pp. 652–718, Complete Verbatim Text)",
        chapters_1917=("ch-15", "ch-16"),
        summary_body="""Overview of Unit V (Chapters XV–XVI — Complete Verbatim Text)
-------------------------------------------------------------

Unit V reproduces verbatim **Chapter XV (*On the Shapes of Eggs, and of Certain Other Hollow Structures*, pp. 652–669)** and **Chapter XVI (*On Form and Mechanical Efficiency*, pp. 670–718)**:

1. **Chapter XV — On the Shapes of Eggs and Hollow Structures (pp. 652–669)**:

   * Refutes teleological myths that pyriform guillemot eggs evolved solely to spin in circles on cliff ledges; instead derives spherical, elliptical, oval, and conical bird-egg profiles from the Laplace membrane equilibrium equation:

     $$\\frac{T_n}{R_n} + \\frac{T_t}{R_t} = P_n$$

     under peristaltic muscular waves pushing the still-pliable shell membrane blunt-end-forward down the oviduct.
   * Extends axisymmetric elastic-shell mechanics to sea-urchin tests (*Echinus*, flattened fluid drop under gravity) and hydra/medusa bells.

2. **Chapter XVI — On Form and Mechanical Efficiency (pp. 670–718)**:

   * **Culmann's Crane & Meyer's Femur (pp. 679–688, Fig. 335)**: Chronicles the historic 1866 Zürich meeting between anatomist :person:`Hermann von Meyer <meyer>` (:cite:`meyer:1867`) and engineer :person:`Karl Culmann <culmann>` (:cite:`culmann:1866`), showing that the spongy :term:`trabeculae` of the human femur head align along the exact :term:`orthogonal principal stress trajectories <orthogonal-trajectories>` of a curved Fairbairn crane—eliminating shearing stress along bony struts and dynamically remodeling when fractures alter load lines (Wolff's Law).
   * **Vertebrate Backbones as Balanced Cantilever Bridges (pp. 694–718)**: Working directly with Dundee bridge engineer :person:`T. Claxton Fidler <fidler>` (:cite:`fidler:1887`), Thompson models quadruped, stegosaur, *Diplodocus*, and avian skeletons as two-armed cantilevers and Forth-Bridge reciprocal trusses where vertebral centra take compression and supraspinous ligaments take tension, concluding with streamlined fish contours (Parsons & Haushofer).
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit V)
----------------------------------------------------

Graphic Statics, Projective Reciprocity, and Trabecular Optimization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Link to `geometor/pappus` (Projective Polarity & Graphic Statics)**: :person:`Karl Culmann's <culmann>` *Die graphische Statik* (:cite:`culmann:1866`)—alongside Maxwell's and Cremona's reciprocal figures—was a direct 19th-century triumph of synthetic projective geometry (rooted in :person:`Pappus <pappus>` Book VII and Poncelet/von Staudt polarity). Force polygons and funicular polygons are projectively dual configurations!
* **Cauchy Stress Tensor & Orthogonal Lamellae**: At every interior point of a 2D loaded elastic continuum, the symmetric stress tensor $\\sigma$ diagonalizes along two mutually perpendicular principal directions ($\\mathbf{e}_1 \\perp \\mathbf{e}_2$, rational :term:`spread` $s = 1$) on which shear stress $\\tau_{12} = 0$. As verified on 300 DPI scan p. 682 (`thompson_femur-702.png`, Fig. 335), placing bony trabeculae strictly along the integral curves of $\\mathbf{e}_1$ (compression arch from medial shaft cortex to superior articular head) and $\\mathbf{e}_2$ (tension tie arching across the femoral neck from lateral cortex) achieves maximum structural stiffness per unit mass of calcium phosphate—anticipating modern Michell trusses and computational topology optimization by a century.
* **Dundee Engineering Collaboration**: Notice Thompson's warm tribute in the Prefatory Note and Chapter XVI (pp. 696–712) to his Dundee colleague :person:`Claxton Fidler <fidler>`, who passed away in 1917—the very year *On Growth and Form* appeared. Fidler's bending-moment diagrams transform the towering neural spines above the withers of the bison, horse, and *Titanotherium* into quantitative graphical statics.
""",
    ),
    UnitSpec(
        slug="unit-6-transformations",
        short_title="VI. Transformations & Epilogue",
        title="Unit VI: On the Theory of Transformations and Epilogue",
        rubric="1917 Cambridge First Edition — Chapter XVII & Epilogue (pp. 719–779, Complete Verbatim Text)",
        chapters_1917=("ch-17", "epilogue"),
        summary_body="""Overview of Unit VI (Chapter XVII & Epilogue — Complete Verbatim Text)
----------------------------------------------------------------------

Unit VI presents the crowning achievement of *On Growth and Form*—the complete verbatim 1917 text of **Chapter XVII (*On the Theory of Transformations, or the Comparison of Related Forms*, pp. 719–777)** and the **Epilogue (pp. 778–779)**:

1. **The Method of Coordinates in Morphology (pp. 719–735)**:

   * Elevates :person:`Descartes's <descartes>` coordinate geometry and :person:`Albrecht Dürer's <durer>` 1528 human-proportion grids (:cite:`durer:1528`) from descriptive measurement to comparative transformation: inscribing a type species in a rectangular net $(x, y)$ and deforming the coordinate lines into $(x', y') = (f(x, y), g(x, y))$ reveals harmonious global laws of differential growth.
   * Classifies canonical deformation families (verified on 300 DPI scans pp. 729–733):

     1. Uniform axial extension $(x, cy)$ turning circles into ellipses (cannon-bones of ox, sheep, giraffe, Fig. 354);
     2. Logarithmic/monotonic gradient spacing (dicotyledon leaf growth around a basal node, Fig. 355–358);
     3. :term:`Oblique affine shear <affine-shear>` $(x + y\\cot\\omega, y\\sin\\omega)$ (Fig. 357);
     4. Radial/polar fan coordinates (palmate and pedate leaves, *Helleborus*, Fig. 360–362);
     5. :term:`Coaxial-hyperbolic curvilinear nets <coaxial-transformation>`.

2. **Comparative Zoological & Palaeontological Transformations (pp. 736–777)**:

   * **Crustacea**: *Geryon*, *Corystes*, *Scyramathia*, *Paralomis*, *Lupa*, *Chorinus* carapaces (Figs. 366–371);
   * **Teleost Fishes**: *Argyropelecus Olfersi* $\\to$ *Sternoptyx diaphana* via $70^\\circ$ oblique shear (Figs. 373–374); *Scarus* $\\to$ *Pomacanthus* via coaxial circular arcs (Figs. 375–376); *Polyprion* $\\to$ *Pseudopriacanthus* $\\to$ *Scorpaena* $\\to$ *Antigonia*; and *Diodon* $\\to$ *Orthagoriscus mola* via coaxial-hyperbolic expansion (Figs. 381–382);
   * **Reptiles, Birds & Mammals**: Crocodilian skulls, *Archaeopteryx* $\\to$ *Apatornis* pelves (with Gerhard Heilmann's interpolated intermediates, Figs. 388–393), *Hyrachyus* $\\to$ *Aceratherium* rhinoceros skulls, *Eohippus* $\\to$ *Mesohippus* $\\to$ *Equus* equine crania (Figs. 401–402), and human, chimpanzee, and baboon cranial coordinates (Figs. 404–408).

3. **Epilogue (pp. 778–779)**: Closes with Thompson's unforgettable lyric meditation on Form and Number—linking :person:`Colin Maclaurin's <maclaurin>` honeybee, Philolaus the Pythagorean (`πάντα γα μὰν τὰ γιγνωσκόμενα`), Milton's golden compasses, James Joseph Sylvester, and Jean-Henri Fabre.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit VI)
-----------------------------------------------------

Projective & Diffeomorphic Geometry (`geometor/pappus` & `geometor/hilbert`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Morphology in the Spirit of Klein's Erlangen Program**: Just as :person:`David Hilbert <euclid>` (`geometor/hilbert`) and :person:`Pappus <pappus>` (`geometor/pappus`) study geometric properties invariant under affine, projective, or birational transformation groups, Thompson defines *taxonomic affinity* as equivalence under a smooth low-degree homeomorphism $(x, y) \\mapsto (x', y')$! Conversely, Thompson stresses a striking **topological negative theorem** (pp. 724, 774): no continuous transformation can map an invertebrate into a vertebrate or a teleost into a shark without tearing singularities—providing a mathematical criterion for discontinuous *bauplan* boundaries.
* **Modern Mathematical Descendants**: Chapter XVII (originally read before the Royal Society of Edinburgh in 1915, :cite:`thompson:1915`) directly fathered Julian Huxley's allometry ($y = b x^k$, 1932), Fred Bookstein's thin-plate spline morphometrics (biharmonic bending-energy minimization), and Alain Goriely's modern differential morphoelasticity.

1917 Cambridge Archival Folio Note (Multimodal Scan Verification)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Printed Page 748 Compositor Typo (`Fig. 474` for `Fig. 374`)**: Direct visual inspection of the 300 DPI page scan of the 1917 First Edition (`thompson_transforms-768.png`, printed p. 748, second line from bottom) reveals an authentic 1917 Cambridge University Press compositor slip: the text reads *"transferred to the oblique coordinates passes into the figure of Sternoptyx (Fig. 474)"* (there are only 408 figures in the 1917 edition, and *Sternoptyx diaphana* is printed immediately above on the same page as `Fig. 374.`). Faithful to Digital Scriptorium principles, the verbatim 1917 text preserves the historical reading while recording `[sic: Fig. 374]` here in the critical apparatus.
* **Epilogue Allusions Identified (pp. 778–779)**:

  * *"a certain mathematician"* ("Conterminous with space and coeval with time is the kingdom of Mathematics..."): **James Joseph Sylvester** (Presidential Address to Section A of the British Association at Exeter, 1869).
  * *"that old man eloquent, that wise student and pupil of the ant and the bee, who died but yesterday"*: the Provençal entomologist **Jean-Henri Fabre** (1823–1915, died October 1915 while Thompson was completing the 1917 manuscript), quoting Fabre's *Souvenirs entomologiques* hymn to Number.
""",
    ),
    UnitSpec(
        slug="unit-7-dynamic-symmetry",
        short_title="VII. Hambidge: Dynamic Symmetry",
        title="Unit VII: Dynamic Symmetry & Gnomonic Morphology — Jay Hambidge (1919–1920)",
        rubric="Yale University Press Public-Domain Companion — *The Diagonal* (Vol. I, 1919–1920) & *Dynamic Symmetry: The Greek Vase* (1920)",
        chapters_1917=(),
        custom_en_body=_HAMBIDGE_1920_EN_BODY,
        summary_body="""Overview of Unit VII (Jay Hambidge's *Elements of Dynamic Symmetry*, 1919–1920)
-------------------------------------------------------------------------------

Unit VII pairs *On Growth and Form* (1917) with scan-verified primary lessons from :person:`Jay Hambidge's <hambidge>` 1919–1920 Yale University Press publications—*The Diagonal* (:cite:`hambidge:1920-diagonal`, where *The Elements of Dynamic Symmetry* first appeared serially) and *Dynamic Symmetry: The Greek Vase* (:cite:`hambidge:1920-vase`):

1. **Static vs. Dynamic Symmetry**: Contrasts passive :term:`static symmetry <static-symmetry>` (regular polygons, rational grids, crystals, diatoms, and radiolarian polyhedra—Thompson's Chapters VII–IX) with active :term:`dynamic symmetry <dynamic-symmetry>` (shell spirals and botanical phyllotaxis—Thompson's Chapters XI–XIV).
2. **Botanical Phyllotaxis as Proportional Engine**: Draws on :person:`A. H. Church's <church>` Oxford sunflower capitulum diagrams (:cite:`church:1904`) to connect the Fibonacci summation series ($1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144\\dots$) to the asymptotic golden ratio $\\phi = \\frac{1 + \\sqrt{5}}{2} \\approx 1.618034$.
3. **Commensurability in Square (`Euclid Book X`)**: Highlights the Greek geometric key: although $1, \\sqrt{2}, \\sqrt{3}, \\sqrt{5}$ are linearly incommensurable, they are :term:`commensurable in square <commensurable-in-square>` (*dynamei symmetroi*, Euclid X Def. 2)—meaning the squares erected on their sides have exact integer area ratios $1 : 2 : 3 : 4 : 5$.
4. **Root-Rectangle Unfolding & Reciprocal Orthogonality**: Demonstrates compass unfolding of the $\\sqrt{2}, \\sqrt{3}, \\sqrt{4} = 2, \\sqrt{5}$ :term:`root rectangles <root-rectangle>` from the unit square, proves that every :term:`reciprocal rectangle <reciprocal-rectangle>` ($1/\\sqrt{n}$) divides its parent $\\sqrt{n}$ rectangle into $n$ congruent similar parts with perpendicular diagonals ($90^\\circ$), and constructs the :term:`whirling-square golden rectangle <whirling-square-rectangle>` ($1 : \\phi$) inside the $\\sqrt{5}$ rectangle ($\\sqrt{5} = \\phi + \\phi^{-1} = 1 + 2\\phi^{-1}$).
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Unit VII)
------------------------------------------------------

Exact Algebraic Bridge to `wildberger`, `euclid`, `divine`, and `thompson`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Greek *Dynamis* = Wildberger's Quadrance (`geometor/wildberger`)**: Hambidge's recovery of Greek *dynamis* ("square / power" in Plato's *Theaetetus* 147d–148b and :person:`Euclid <euclid>` Book X Def. 2, :cite:`euclid:elements`) translates with 100% algebraic precision into Rational Trigonometry (`geometor/wildberger`):

  * A rectangle of unit height ($Q_{\\text{end}} = 1$) and horizontal side $s_n = \\sqrt{n}$ has horizontal :term:`quadrance` $Q_n = n$.
  * By Pythagoras's Theorem ($Q_{\\text{diag}} = Q_{\\text{end}} + Q_n = 1 + n$), swinging the diagonal down to the baseline increments the side quadrance by **exact integer steps** $Q = 1 \\to 2 \\to 3 \\to 4 \\to 5$!
  * Moreover, for any rectangle of aspect ratio $r$ with main diagonal vector $(r, 1)$ and reciprocal rectangle of width $1/r$ with counter-diagonal vector $(1/r, -1)$, their dot product is:

    $$(r, 1) \\cdot \\left(\\frac{1}{r}, -1\\right) = 1 - 1 = 0$$

    proving algebraically for *every* ratio $r > 0$ that the diagonal of the reciprocal intersects the diagonal of the whole at exact perpendicular :term:`spread` $s = 1$ ($90^\\circ$)!

Unified Harmonic Identity of the $\\sqrt{5}$ and $\\phi$ Rectangles (`geometor/divine`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Exact $\\mathbb{Q}(\\sqrt{5})$ Decomposition**: Over the golden field $\\mathbb{Q}(\\phi)$ (`geometor/divine`), where $\\phi = \\frac{1+\\sqrt{5}}{2}$ and $\\phi^{-1} = \\phi - 1 = \\frac{\\sqrt{5}-1}{2}$, Hambidge's geometric dissections express three fundamental exact identities:

  $$\\sqrt{5} = 2\\phi - 1 = 1 + 2\\phi^{-1} = \\phi + \\phi^{-1}$$

  1. $\\sqrt{5} = 1 + 2\\phi^{-1}$: a central unit square flanked symmetrically by two vertical reciprocal golden rectangles;
  2. $\\sqrt{5} = \\phi + \\phi^{-1}$: a horizontal whirling-square rectangle ($\\phi$) joined to a vertical reciprocal golden rectangle ($\\phi^{-1}$);
  3. $2\\phi - \\sqrt{5} = 1$: two overlapping whirling-square rectangles sharing a central unit square!

* **Synthesis of Thompson and Hambidge**: Reading Thompson (1917) and Hambidge (1919–1920) side by side illuminates two complementary halves of classical morphology: Thompson proves *physically and differentially* why terminal accretion and apical close-packing generate gnomons, equiangular spirals, and Fibonacci parastichies, while Hambidge shows *synthetically and constructively* how straightedge and compass unfold those very gnomons into commensurable-in-square harmonic partitions.
""",
    ),
)
