"""Structured chapter specifications and scholarly apparatus for On Growth and Form (1917)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UnitSpec:
    """Complete specification for one 3-track synchronized chapter in `docsrc/growth_and_form/`."""

    slug: str
    canonical_id: str
    order: int
    folio: str
    short_title: str
    title: str
    rubric: str
    chapters_1917: tuple[str, ...]
    summary_body: str
    notes_body: str
    legacy_anchor: str = ""
    custom_en_body: str = ""


UNITS: tuple[UnitSpec, ...] = (
    UnitSpec(
        slug="ch_01",
        canonical_id="Ch. I",
        order=1,
        folio="pp. v–vi, 1–15",
        short_title="Introductory",
        title="Prefatory Note, Epigraphs & Chapter I: Introductory",
        rubric="1917 Cambridge First Edition — Prefatory Note, Epigraphs & Chapter I (pp. v–vi, xvi, 1–15)",
        chapters_1917=("prefatory", "epigraphs", "ch-1"),
        legacy_anchor="growth-and-form-unit-1-magnitude-en",
        summary_body="""Overview of Chapter I (Prefatory Note, Epigraphs & Introductory)
----------------------------------------------------------------

Chapter I establishes the philosophical, mechanical, and physical foundations of :person:`D'Arcy Wentworth Thompson's <thompson>` *On Growth and Form* (:cite:`thompson:1917`):

1. **Prefatory Note & Epigraphs (pp. v–vi, xvi)**: Framing the treatise as "all preface," Thompson unites :person:`Stephen Hales <hales>`, :person:`St. Thomas Aquinas <aquinas>` (*De Potentia Dei*, Q. 3, a. 11, :cite:`aquinas:depot`), :person:`Sir Isaac Newton <newton>` (*Principia* Preface), and J. H. Jellett to argue that corporeal organic forms arise directly from physical forces acting on matter.
2. **Kant's Criterion of Physical Science (pp. 1–3)**: Answering :person:`Immanuel Kant's <kant>` dictum that chemistry and biology become strict sciences only insofar as mathematics enters them, Thompson calls for morphology to move beyond descriptive taxonomy to quantitative mathematical description.
3. **Efficient vs. Teleological Causation (pp. 4–8)**: While acknowledging the historical role of final causes and adaptation, Thompson critiques purely historical or teleological Darwinism when divorced from physical mechanics. Natural forms are governed by physical antecedents—matter moved, moulded, and conformed in obedience to dynamical laws.
4. **The Principle of Physical Causation (pp. 8–15)**: Thompson reviews the classical lineage of dynamical morphology from Anaxagoras, Empedocles, and :person:`Galileo <galileo>` through Swammerdam, :person:`Réaumur <reaumur>`, :person:`Moseley <moseley>`, and Roux, affirming that organic structures obey standard physical laws without invoking mystical vitalistic *entelechies*.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter I)
-------------------------------------------------------

1917 Edition Provenance & Epigraph Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **1917 First Edition Structure**: Verified directly against 300 DPI page scans of the 1917 Cambridge University Press imprint (`ongrowthform1917thom`), the First Edition opens with :person:`Stephen Hales's <hales>` *Vegetable Staticks* epigraph preceding the Prefatory Note (dated *University College, Dundee, December, 1916*) and places the celebrated triad of :person:`Aquinas <aquinas>`, :person:`Newton <newton>`, and J. H. Jellett on p. xvi immediately facing Chapter I (p. 1). (In the 1942 Second Edition—strictly excluded from this codex—Chapter I was heavily rewritten and split.)
* **Link to `geometor/aquinas` & `geometor/aristotle`**: Thompson's quotation from :cite:`aquinas:depot` (*"Cum formarum naturalium et corporalium esse non consistat nisi in unione ad materiam..."*, which he had earlier introduced in his 1911 Portsmouth British Association address, :cite:`thompson:1911`) anchors mathematical morphology in Aristotelian–Thomistic natural philosophy: physical agents transmuting matter suffice to account for natural configuration without appealing to vitalistic *entelechies*.
""",
    ),
    UnitSpec(
        slug="ch_02",
        canonical_id="Ch. II",
        order=2,
        folio="pp. 16–49",
        short_title="On Magnitude",
        title="Chapter II: On Magnitude",
        rubric="1917 Cambridge First Edition — Chapter II (pp. 16–49)",
        chapters_1917=("ch-2",),
        summary_body="""Overview of Chapter II (On Magnitude)
-------------------------------------

Chapter II develops the :term:`Principle of Similitude <similitude>` and :person:`Galileo's <galileo>` :term:`Square-Cube Law <square-cube-law>` (:cite:`galileo:1638`):

1. **Galileo's Scaling Bound (pp. 16–28)**: Surface area $S \\propto L^2$ while volume and weight $V \\propto L^3$. Linear enlargement therefore causes the ratio of surface to mass ($S/V \\propto L^{-1}$) to decrease, setting absolute upper limits to terrestrial animal dimensions and requiring bones to thicken disproportionately.
2. **Physical Scale Regimes (pp. 29–35)**: Absolute spatial scale partitions the living world into distinct physical regimes—gravity-dominated large vertebrates ($L^3$), surface-tension-dominated insects and protists ($L^2$), and Brownian-motion-governed bacteria and colloids.
3. **Locomotive Similitude & Froude's Law (pp. 35–49)**: Thompson proves that maximal jumping height and stride mechanics remain nearly scale-invariant across flea, kangaroo, and horse, and analyzes swimming and flight velocities via hydrodynamic similitude.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter II)
--------------------------------------------------------

Dimensional Scaling & Euclidean Similitude
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Link to `geometor/euclid` & `geometor/elements`**: Thompson's dimensional equations $S \\propto L^2$ and $V \\propto L^3$ rest directly on :person:`Euclid's <euclid>` Book VI (Props. 19–20, duplicate ratio of similar polygons) and Book XI (Prop. 33, triplicate ratio of similar parallelepipeds; :cite:`euclid:elements`, :cite:`heath:1908`).
* **Froude's Law & Locomotion**: Thompson's proof (pp. 29–35) that maximal jumping height remains nearly scale-invariant across organisms of differing sizes anticipates modern dimensional analysis and biomechanics.
""",
    ),
    UnitSpec(
        slug="ch_03",
        canonical_id="Ch. III",
        order=3,
        folio="pp. 50–155",
        short_title="The Rate of Growth",
        title="Chapter III: The Rate of Growth",
        rubric="1917 Cambridge First Edition — Chapter III (pp. 50–155)",
        chapters_1917=("ch-3",),
        summary_body="""Overview of Chapter III (The Rate of Growth)
--------------------------------------------

Chapter III investigates the temporal kinetics and differential velocity of growth across ontogeny:

1. **Growth Velocity & Stature Curves (pp. 50–85)**: Analyzes growth increments ($dL/dt$, $dW/dt$), Adolphe Quetelet's anthropometric stature data, and the characteristic sigmoid (autocatalytic S-shaped) growth trajectory.
2. **Periodicities & Environmental Modulations (pp. 86–120)**: Documents annual, seasonal, and diurnal growth rhythms in fish scales, molluscan shells, and tree rings.
3. **Differential Growth Gradients (pp. 121–155)**: Demonstrates that different anatomical axes possess distinct growth rates ($dx/dt \\neq dy/dt$), creating regional velocity gradients that drive morphological change over time.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter III)
---------------------------------------------------------

Differential Growth as the Dynamic Engine of Morphology
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Ontogenetic Foundation for Chapters XI and XVII**: Chapter III's demonstration of unequal axial growth gradients ($dx/dt \\neq dy/dt$) supplies the direct temporal foundation for both Chapter XI's gnomonic shell spirals (where marginal ratios remain constant) and Chapter XVII's coordinate deformation grids (where growth gradients vary continuously across space).
* **Link to Modern Allometry**: Thompson's velocity formulations directly anticipate Julian Huxley's 1932 quantitative allometry law ($y = b x^k$).
""",
    ),
    UnitSpec(
        slug="ch_04",
        canonical_id="Ch. IV",
        order=4,
        folio="pp. 156–200",
        short_title="The Internal Form and Structure of the Cell",
        title="Chapter IV: On the Internal Form and Structure of the Cell",
        rubric="1917 Cambridge First Edition — Chapter IV (pp. 156–200)",
        chapters_1917=("ch-4",),
        summary_body="""Overview of Chapter IV (The Internal Form and Structure of the Cell)
--------------------------------------------------------------------

Chapter IV investigates the physical mechanics of intracellular configuration and cell division:

1. **Mitotic Spindle & Karyokinetic Asters (pp. 156–175)**: Models the centrosomes, radiating astral rays, and mitotic spindle fibers through physical lines of force in the colloidal cytoplasm.
2. **Field Analogies (pp. 176–190)**: Compares karyokinetic figures with magnetic field lines (Faraday), electrostatic attractions, diffusion gradients (Leduc), and hydrodynamic streamlines.
3. **Colloidal Mechanics (pp. 191–200)**: Interprets protoplasmic structures as dynamic equilibria within viscous heterogeneous colloids subjected to localized surface-tension changes.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter IV)
--------------------------------------------------------

Lines of Force and Cytological Dynamics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Faraday–Maxwell Field Analogies**: Thompson applies classical electromagnetic and hydrodynamic potential theory to cell division, illustrating how mechanical stresses in a fluid colloid produce configurations identical to optical and electrical field lines.
* **Critique of Mechanistic Cytology**: Thompson argues that spindle fibers are not rigid solid skeletal threads, but transient lines of tension and molecular orientation within a dynamic colloidal sol-gel system.
""",
    ),
    UnitSpec(
        slug="ch_05",
        canonical_id="Ch. V",
        order=5,
        folio="pp. 201–276",
        short_title="The Forms of Cells",
        title="Chapter V: The Forms of Cells",
        rubric="1917 Cambridge First Edition — Chapter V (pp. 201–276)",
        chapters_1917=("ch-5",),
        legacy_anchor="growth-and-form-unit-2-cells-tissues-en",
        summary_body="""Overview of Chapter V (The Forms of Cells)
------------------------------------------

Chapter V applies capillary surface tension and minimal-surface geometry to solitary unicellular organisms:

1. **The Laplace–Young Law (pp. 201–220)**: Formulates the fundamental pressure equation $\\Delta P = T(1/R_1 + 1/R_2)$ governing fluid membranes under :term:`surface tension <surface-tension>` $T$.
2. **Plateau–Delaunay Surfaces of Revolution (pp. 221–250)**: Classifies the six axisymmetric surfaces of constant :term:`mean curvature <mean-curvature>`—plane, sphere, cylinder, :term:`catenoid`, :term:`unduloid`, and :term:`nodoid` (:cite:`plateau:1873`).
3. **Unicellular Morphology (pp. 251–276)**: Interprets the outlines of solitary protozoa (*Amoeba*, *Lagena*, ciliates, flagellates, and mammalian erythrocytes) as capillary equilibrium surfaces.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter V)
-------------------------------------------------------

Capillarity & Constant Mean Curvature Surfaces
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Link to `geometor/pappus`**: Connects classical Alexandrian isoperimetric theorems (:person:`Pappus <pappus>`, *Synagoge* Book V, :cite:`pappus:synagoge`) to physical surface-tension minimization in liquid membranes.
* **Delaunay's Roulettes**: Delaunay (1841) proved that surfaces of revolution with constant mean curvature are generated by rolling conic sections along an axis: an ellipse generates an unduloid, a hyperbola a nodoid, and a parabola a catenoid.
""",
    ),
    UnitSpec(
        slug="ch_06",
        canonical_id="Ch. VI",
        order=6,
        folio="pp. 277–292",
        short_title="A Note on Adsorption",
        title="Chapter VI: A Note on Adsorption",
        rubric="1917 Cambridge First Edition — Chapter VI (pp. 277–292)",
        chapters_1917=("ch-6",),
        summary_body="""Overview of Chapter VI (A Note on Adsorption)
---------------------------------------------

Chapter VI analyzes the physical chemistry of surface adsorption at fluid interfaces:

1. **The Gibbs–Thomson Principle (pp. 277–285)**: Explains the thermodynamic phenomenon whereby substances that lower :term:`surface tension <surface-tension>` spontaneously concentrate at the interface between two phases.
2. **Cell Membranes & Pellicles (pp. 286–292)**: Shows how surface adsorption accounts for the formation of cell membranes, protective pellicles, and localized mineral precipitation along cellular edges.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter VI)
--------------------------------------------------------

Interfacial Thermodynamics and Biological Deposition
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Thermodynamic Basis for Mineral Skeletogenesis**: Chapter VI bridges solitary fluid cells (Chapter V) and solid spicular skeletons (Chapter IX), demonstrating that physical adsorption at phase boundaries precedes biomineralization.
""",
    ),
    UnitSpec(
        slug="ch_07",
        canonical_id="Ch. VII",
        order=7,
        folio="pp. 293–345",
        short_title="The Forms of Tissues",
        title="Chapter VII: The Forms of Tissues, or Cell-Aggregates",
        rubric="1917 Cambridge First Edition — Chapter VII (pp. 293–345)",
        chapters_1917=("ch-7",),
        summary_body="""Overview of Chapter VII (The Forms of Tissues, or Cell-Aggregates)
------------------------------------------------------------------

Chapter VII establishes the geometry of cellular froths, minimal partition surfaces, and the bee's honeycomb:

1. **Plateau's Laws for Liquid Films (pp. 293–326)**: In planar networks, three partitions meet at $120^\\circ$ (:term:`Fermat–Torricelli point <fermat-torricelli-point>` `X(13)`), creating hexagonal arrangements. In 3D space, four edges meet at tetrahedral angles $\\arccos(-1/3) \\approx 109^\\circ 28' 16''$.
2. **The Bee's Cell & Honeycomb (pp. 327–336)**: Traces the mathematical history from :person:`Pappus <pappus>` and :person:`Kepler <kepler>` (:cite:`kepler:1611`) through :person:`Maraldi <maraldi>` (:cite:`maraldi:1712`), :person:`Maclaurin <maclaurin>` (:cite:`maclaurin:1743`), and :person:`Boscovich <boscovich>` (:cite:`boscovich:1760`), proving that the :term:`rhombic dodecahedron <rhombic-dodecahedron>` cap with :term:`Maraldi angle <maraldi-angle>` minimizes wax area through physical soap-film tension.
3. **Parenchyma & Kelvin's Foam (pp. 336–345)**: Examines Plateau's wire-cube soap film (Fig. 134) and :person:`Lord Kelvin's <kelvin>` space-filling 14-hedral :term:`tetrakaidecahedron` (:cite:`kelvin:1887`).
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter VII)
---------------------------------------------------------

Rational Trigonometry of Soap Films (`geometor/etc` & `geometor/wildberger`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **2D Triple Junctions (`X(13)` & Spread $s = 3/4$)**: Three co-planar soap films meet at the Fermat–Torricelli point `X(13)`. In Rational Trigonometry, the $120^\\circ$ angle has exact rational :term:`spread` $s = \\sin^2(120^\\circ) = 3/4 \\in \\mathbb{Q}$.
* **3D Maraldi Angle (Spread $s = 8/9$)**: Four liquid edges meeting at a spatial foam vertex subtend $\\theta = \\arccos(-1/3) \\approx 109^\\circ 28' 16''$. Since $\\cos^2\\theta = 1/9$, the Maraldi angle has exact rational spread $s = 8/9$.
* **Connection to `geometor/pacioli`**: Kepler's rhombic dodecahedron has face diagonal ratio $1 : \\sqrt{2}$, linking soap froth directly to classical polyhedra and Hambidge's root-two rectangle.
""",
    ),
    UnitSpec(
        slug="ch_08",
        canonical_id="Ch. VIII",
        order=8,
        folio="pp. 346–410",
        short_title="The Forms of Tissues (continued)",
        title="Chapter VIII: The Forms of Tissues (continued)",
        rubric="1917 Cambridge First Edition — Chapter VIII (pp. 346–410)",
        chapters_1917=("ch-8",),
        summary_body="""Overview of Chapter VIII (The Forms of Tissues, continued)
----------------------------------------------------------

Chapter VIII extends minimal surface partition laws to dividing embryonic and plant tissues:

1. **Sachs's Orthogonal Law (pp. 346–370)**: Demonstrates that newly formed dividing cell walls meet preexisting boundary walls at right angles ($90^\\circ$).
2. **Errera's Minimal-Area Rule (pp. 371–390)**: Shows that cellular cleavage partitions adopt minimal surface areas consistent with boundary constraints.
3. **Embryological Cleavage Patterns (pp. 391–410)**: Analyzes 2-cell, 4-cell, 8-cell, and 16-cell cleavage geometries in dividing eggs, cambium, and cork parenchyma as physical capillary equilibrium states.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter VIII)
----------------------------------------------------------

Orthogonal Trajectories and Cleavage Geometry
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Physical Determination of Embryogenesis**: Thompson demonstrates that initial segmentation geometry in animal embryos is dictated by minimal area and orthogonal partition rather than preformed phylogenetic blueprints.
""",
    ),
    UnitSpec(
        slug="ch_09",
        canonical_id="Ch. IX",
        order=9,
        folio="pp. 411–487",
        short_title="Spicules and Spicular Skeletons",
        title="Chapter IX: On Concretions, Spicules, and Spicular Skeletons",
        rubric="1917 Cambridge First Edition — Chapter IX (pp. 411–487)",
        chapters_1917=("ch-9",),
        summary_body="""Overview of Chapter IX (On Concretions, Spicules, and Spicular Skeletons)
-------------------------------------------------------------------------

Chapter IX analyzes biomineralized skeletal architectures in sponges and Radiolaria:

1. **Sponge Spicules (pp. 411–440)**: Derives triradiate ($120^\\circ$) and tetraradiate ($109^\\circ 28'$) calcareous and siliceous :term:`spicule <spicule>` forms from crystallization within intercellular Plateau borders.
2. **Haeckel's Radiolaria (pp. 441–470)**: Reinterprets :person:`Ernst Haeckel's <haeckel>` *Challenger* Radiolaria (:cite:`haeckel:1887`) through spherical foam configurations and regular polyhedral wire-frames.
3. **Euler's Polyhedral Theorem on Spheres (pp. 471–487)**: Proves that a closed convex spherical cage cannot consist solely of hexagons, refuting Haeckel's claim regarding *Aulonia hexagona*.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter IX)
--------------------------------------------------------

Euler's Polyhedral Law & Radiolarian Topology (`geometor/euclid` & `geometor/pacioli`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Topological Proof against Pure Hexagon Spheres**: For any 3-valent spherical mesh ($3V = 2E$) with Euler characteristic $\\chi = 2$, $\\sum_{k \\ge 3} (6 - k) F_k = 12$. Because $(6 - 6) = 0$, hexagons contribute nothing to curvature defect: every closed hexagonal mesh *must* contain at least 12 pentagons.
* **Link to `geometor/euclid` Book XIII**: Bridges Platonic regular solids directly to siliceous protozoan skeletons (:cite:`pacioli:1509`).
""",
    ),
    UnitSpec(
        slug="ch_10",
        canonical_id="Ch. X",
        order=10,
        folio="pp. 488–492",
        short_title="A Parenthetic Note on Geodetics",
        title="Chapter X: A Parenthetic Note on Geodetics",
        rubric="1917 Cambridge First Edition — Chapter X (pp. 488–492)",
        chapters_1917=("ch-10",),
        summary_body="""Overview of Chapter X (A Parenthetic Note on Geodetics)
-------------------------------------------------------

Chapter X provides a compact mathematical analysis of helical spiral structures on cylindrical walls:

1. **Geodesics on Cylinders (pp. 488–490)**: Explains that the shortest path between two points on a cylinder is a regular helix.
2. **Plant Thickenings & Algae (pp. 490–492)**: Analyzes spiral thickenings in wood vessels and the helical chloroplast ribbons of *Spirogyra* as elastic geodesics minimizing bending energy.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter X)
-------------------------------------------------------

Differential Geometry of Cylindrical Geodesics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Elastic Strain Energy Minimization**: Demonstrates that mechanical fibers under uniform longitudinal tension or torsion follow geodesic helices on cylindrical surfaces.
""",
    ),
    UnitSpec(
        slug="ch_11",
        canonical_id="Ch. XI",
        order=11,
        folio="pp. 493–586",
        short_title="The Logarithmic Spiral",
        title="Chapter XI: The Logarithmic Spiral",
        rubric="1917 Cambridge First Edition — Chapter XI (pp. 493–586)",
        chapters_1917=("ch-11",),
        legacy_anchor="growth-and-form-unit-3-equiangular-spiral-en",
        summary_body="""Overview of Chapter XI (The Logarithmic Spiral)
-----------------------------------------------

Chapter XI presents the geometric centerpiece of *On Growth and Form*—the theory of the equiangular spiral and gnomonic self-similarity:

1. **The Logarithmic Spiral (pp. 493–507)**: Contrasts the Archimedean spiral ($r = a\\theta$, :cite:`archimedes:spirals`) with the :term:`equiangular spiral <equiangular-spiral>` of :person:`Descartes <descartes>` and :person:`Jakob Bernoulli <bernoulli-jakob>` ($r = a e^{\\theta \\cot\\alpha}$, :cite:`bernoulli:1692`).
2. **Hero's Theory of the Gnomon (pp. 508–514)**: Recovers :person:`Aristotle's <aristotle>` (*Categories* 15a30, :cite:`aristotle:cat`) and :person:`Hero of Alexandria's <hero>` (*Definitiones* 58, :cite:`hero:def`) doctrine of the :term:`gnomon`: terminal accretion preserving shape requires gnomonic growth.
3. **Whirling Squares & Golden Triangles (pp. 515–530)**: Illustrates gnomons on the $\\sqrt{2}$ rectangle, the :term:`whirling-square golden rectangle <whirling-square-rectangle>` ($1 : \\phi$), and :person:`Euclid's <euclid>` IV.10 :term:`golden triangle <golden-triangle>`.
4. **Helicospiral Shells (pp. 531–586)**: Develops Canon :person:`Henry Moseley's <moseley>` 3D helicospiral parameters $(\\alpha, \\beta, \\gamma)$ for turbinated gastropods, bivalves, and *Nautilus* (:cite:`moseley:1838`).
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XI)
--------------------------------------------------------

Gnomonic Self-Similarity Across `geometor/aristotle`, `geometor/euclid`, and `geometor/divine`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Whirling Squares and Dynamic Symmetry**: Directly anticipates :person:`Jay Hambidge's <hambidge>` Dynamic Symmetry (:cite:`hambidge:1920-diagonal`, 1919–1920).
* **Why *Nautilus* Is Not Golden**: Thompson clarifies that *any* constant ratio of tangential to radial growth produces an equiangular spiral; *Nautilus* has $\\alpha \\approx 80^\\circ$, not $\\phi$.
""",
    ),
    UnitSpec(
        slug="ch_12",
        canonical_id="Ch. XII",
        order=12,
        folio="pp. 587–611",
        short_title="Spiral Shells of the Foraminifera",
        title="Chapter XII: The Spiral Shells of the Foraminifera",
        rubric="1917 Cambridge First Edition — Chapter XII (pp. 587–611)",
        chapters_1917=("ch-12",),
        summary_body="""Overview of Chapter XII (The Spiral Shells of the Foraminifera)
---------------------------------------------------------------

Chapter XII examines discrete chambered accretion in rhizopod shells:

1. **Pulsatile Growth (pp. 587–598)**: Shows how discrete periodic protoplasmic droplets harden by :term:`surface tension <surface-tension>` into rectilinear (*Nodosaria*), biserial (*Textularia*), and helicoid chamber series.
2. **Logarithmic Chamber Sequences (pp. 599–611)**: Demonstrates that successive chamber volumes form geometric progressions matching continuous equiangular spirals (*Rotalia*, *Globigerina*, *Nummulites*).
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XII)
---------------------------------------------------------

Discrete Gnomonic Accretion
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Discrete vs. Continuous Accretion**: Connects foraminiferal chamber sequences to discrete :term:`gnomon <gnomon>` units, modeling pulsatile growth through surface-tension droplet physics.
""",
    ),
    UnitSpec(
        slug="ch_13",
        canonical_id="Ch. XIII",
        order=13,
        folio="pp. 612–634",
        short_title="Horns, Teeth, and Tusks",
        title="Chapter XIII: The Shapes of Horns, and of Teeth or Tusks: with a Note on Torsion",
        rubric="1917 Cambridge First Edition — Chapter XIII (pp. 612–634)",
        chapters_1917=("ch-13",),
        summary_body="""Overview of Chapter XIII (The Shapes of Horns, Teeth, and Tusks)
----------------------------------------------------------------

Chapter XIII extends differential growth and spatial torsion to vertebrate accretionary structures:

1. **Horns of Sheep & Antelopes (pp. 612–624)**: Models curved and spiral horns through unequal longitudinal growth rates around the generative ring.
2. **Teeth & Tusks (pp. 625–630)**: Analyzes rodent incisors, elephant tusks, and the straight spiraled tusk of the narwhal.
3. **Theory of Torsion (pp. 631–634)**: Investigates 3D space curves, torsion $\\tau$, and shear deformation in biological helices.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XIII)
----------------------------------------------------------

Spatial Kinematics of Accretionary Growth
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Differential Growth as Kinematic Torsion**: Unequal growth rates between opposite margins naturally produce curvature and torsion in rigid accretionary appendages.
""",
    ),
    UnitSpec(
        slug="ch_14",
        canonical_id="Ch. XIV",
        order=14,
        folio="pp. 635–651",
        short_title="Phyllotaxis",
        title="Chapter XIV: On Leaf-Arrangement, or Phyllotaxis",
        rubric="1917 Cambridge First Edition — Chapter XIV (pp. 635–651)",
        chapters_1917=("ch-14",),
        legacy_anchor="growth-and-form-unit-4-phyllotaxis-en",
        summary_body="""Overview of Chapter XIV (On Leaf-Arrangement, or Phyllotaxis)
-------------------------------------------------------------

Chapter XIV presents Thompson's classic analysis of botanical :term:`phyllotaxis`, continued fractions, and parastichies:

1. **Helical Stems vs. Discoidal Capitula (pp. 635–638)**: Unifies cylindrical stem phyllotaxis with planar sunflower inflorescences (:person:`Schimper <schimper>`, :person:`Braun <braun>`, :person:`Bravais <bravais>`, :cite:`bravais:1837`; :person:`Church <church>`, :cite:`church:1904`).
2. **Schimper–Braun Series & Continued Fractions (pp. 638–642)**: Analyzes the divergence series $1/2, 1/3, 2/5, 3/8, 5/13, 8/21, \\dots$ converging to the golden :term:`divergence angle <divergence-angle>` $\\phi^{-2} \\approx 0.381966$ ($137^\\circ 30' 28''$).
3. **P. G. Tait's Parastichy Lattice (pp. 643–646)**: Details :person:`Peter Guthrie Tait's <tait>` theorem (:cite:`tait:1872`) that intersecting $(m, n)$ contact :term:`parastichies <parastichy>` necessarily generate intermediate $m + n$ helices.
4. **Mechanical Close-Packing (pp. 646–651)**: Rejects mystical teleology in favor of :person:`Hofmeister's <hofmeister>` mechanical gap-rule (:cite:`hofmeister:1868`) and physical pressure.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XIV)
---------------------------------------------------------

Direct Companion to `geometor/phyllotaxis` & `geometor/divine`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **From Tait (1872) to Turing (1952) and Vogel (1979)**: Connects Thompson's 1917 formulation to modern mathematical phyllotaxis and :person:`Alan Turing's <turing>` reaction-diffusion morphogenesis (:cite:`turing:1952`).
* **Why $\\phi^{-2}$ Maximizes Packing Uniformity**: The golden ratio's partial quotients make it the most irrational divergence angle, preventing premature radial alignment across scales.
""",
    ),
    UnitSpec(
        slug="ch_15",
        canonical_id="Ch. XV",
        order=15,
        folio="pp. 652–669",
        short_title="Shapes of Eggs",
        title="Chapter XV: On the Shapes of Eggs, and of Certain Other Hollow Structures",
        rubric="1917 Cambridge First Edition — Chapter XV (pp. 652–669)",
        chapters_1917=("ch-15",),
        legacy_anchor="growth-and-form-unit-5-efficiency-en",
        summary_body="""Overview of Chapter XV (On the Shapes of Eggs and Hollow Structures)
--------------------------------------------------------------------

Chapter XV investigates the hydrostatic and mechanical forces shaping thin elastic shells:

1. **Egg Profiles & Laplace Equilibrium (pp. 652–664)**: Derives spherical, elliptical, oval, and conical bird egg contours from peristaltic muscular pressures shaping the pliable membrane via $T_n/R_n + T_t/R_t = P_n$.
2. **Sea-Urchin Tests & Medusae (pp. 665–669)**: Analyzes *Echinus* tests as flattened fluid drops under gravity, and applies axisymmetric membrane mechanics to jellyfish bells.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XV)
--------------------------------------------------------

Axisymmetric Membrane Statics
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Critique of Teleological Adaptation**: Thompson disproves the common adaptationist myth that guillemot eggs evolved pyriform shapes exclusively to roll in circles on cliffs, proving instead that peristaltic pressure acting on an elastic membrane naturally generates pyriform geometry.
""",
    ),
    UnitSpec(
        slug="ch_16",
        canonical_id="Ch. XVI",
        order=16,
        folio="pp. 670–718",
        short_title="Form and Mechanical Efficiency",
        title="Chapter XVI: On Form and Mechanical Efficiency",
        rubric="1917 Cambridge First Edition — Chapter XVI (pp. 670–718)",
        chapters_1917=("ch-16",),
        summary_body="""Overview of Chapter XVI (On Form and Mechanical Efficiency)
-----------------------------------------------------------

Chapter XVI explores biomechanical structural optimization, graphic statics, and skeletal architecture:

1. **Culmann's Crane & Meyer's Femur (pp. 670–693)**: Documents the historic connection between engineer :person:`Karl Culmann <culmann>` (:cite:`culmann:1866`) and anatomist :person:`Hermann von Meyer <meyer>` (:cite:`meyer:1867`), demonstrating that human femur head :term:`trabeculae` align along :term:`orthogonal principal stress trajectories <orthogonal-trajectories>`.
2. **Vertebrate Backbones as Cantilevers (pp. 694–712)**: Collaborating with Dundee engineer :person:`T. Claxton Fidler <fidler>` (:cite:`fidler:1887`), models quadruped and dinosaur skeletons as two-armed cantilever bridges.
3. **Streamlined Aquatic Forms (pp. 713–718)**: Analyzes hydrodynamic streamlines in fish and cetaceans.
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XVI)
---------------------------------------------------------

Graphic Statics & Principal Stress Trajectories (`geometor/pappus`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Link to Projective Duality**: Culmann's graphic statics roots stress trajectories in projective reciprocity (:person:`Pappus <pappus>`, *Synagoge* Book VII).
* **Cauchy Stress Diagonalization**: Trabeculae align along principal stress axes $\\sigma_1 \\perp \\sigma_2$, eliminating shear strain along bony struts.
""",
    ),
    UnitSpec(
        slug="ch_17",
        canonical_id="Ch. XVII",
        order=17,
        folio="pp. 719–779",
        short_title="Theory of Transformations",
        title="Chapter XVII: On the Theory of Transformations, or the Comparison of Related Forms",
        rubric="1917 Cambridge First Edition — Chapter XVII & Epilogue (pp. 719–779)",
        chapters_1917=("ch-17", "epilogue"),
        legacy_anchor="growth-and-form-unit-6-transformations-en",
        summary_body="""Overview of Chapter XVII & Epilogue (The Theory of Transformations)
-------------------------------------------------------------------

Chapter XVII and the Epilogue present the climax of *On Growth and Form*—the Method of Coordinates and the philosophy of mathematical morphology:

1. **The Method of Coordinates (pp. 719–735)**: Elevates :person:`Albrecht Dürer's <durer>` proportion grids (:cite:`durer:1528`) to dynamic transformations $(x', y') = (f(x, y), g(x, y))$, classifying :term:`affine shears <affine-shear>`, radial expansions, and :term:`coaxial transformations <coaxial-transformation>`.
2. **Comparative Phylogeny (pp. 736–777)**: Demonstrates global coordinate deformations across crustacean carapaces, teleost fishes (*Argyropelecus* to *Sternoptyx*, *Diodon* to *Orthagoriscus*), and reptile/mammalian skulls (:cite:`thompson:1915`).
3. **Epilogue (pp. 778–779)**: Thompson's lyric meditation linking Pythagorean philosophy, Milton's golden compasses, Sylvester, and Jean-Henri Fabre (:person:`Maclaurin <maclaurin>`).
""",
        notes_body="""Scholarly Commentary & GEOMETOR Concordance (Chapter XVII)
----------------------------------------------------------

Projective & Diffeomorphic Geometry (`geometor/pappus` & `geometor/hilbert`)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Erlangen Program in Morphology**: Defines taxonomic affinity as equivalence under smooth low-degree homeomorphisms.
* **Topological Negative Theorem**: Discontinuous morphological transitions cannot be bridged by continuous deformation without tearing singularities.
* **1917 Cambridge Archival Notes**: Identifies the authentic Cambridge typo (Fig. 474 for Fig. 374) and decodes Sylvester and Fabre allusions in the Epilogue.
""",
    ),
)
