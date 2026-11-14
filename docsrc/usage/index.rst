:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the Interactive Morphological Codex & Dynamic Symmetry Engine

The GEOMETOR edition of :cite:`Sir D'Arcy Wentworth Thompson (1917) <thompson_1917>` and :cite:`Jay Hambidge (1919–1920) <hambidge_1920_vase>` integrates verbatim fidelity to historical Cambridge and Yale printings with interactive reading tracks, theme-adaptive vector plates, and cross-repository concordance mappings.

Interactive Codex Features
--------------------------

1. Synchronized Reading Tracks
   Each of the seven units in *On Growth and Form* and the Dynamic Symmetry companion provides synchronized parallel tracks accessible from the book header bar:
   
   * **1917/1920 Primary Text:** Verbatim unabridged text from the 1917 Cambridge First Edition and Hambidge's 1919–1920 Yale publications.
   * **Summary:** Analytical overview, core mathematical formulations, and biological principles.
   * **Notes & Concordance:** Scholarly commentary, historical context (e.g. Aristotle's gnomon, Tait's phyllotaxis relation), and cross-links to sibling GEOMETOR treatises.

2. Primary-Source Folio Milestones
   Marginal page markers (such as ``[p. 1]``, ``[p. 201]``, or ``[p. 719]``) mark exact page boundaries of the 1917 Cambridge printing, linking directly to verified public-domain scans. Header **Folio** badges open the primary witness directly in a side drawer or new tab.

3. Interactive Diagrams & Deductive Links
   Throughout the text, morphological forms and geometric structures connect directly to formal definitions:
   
   * Eleven calibrated SVG plates illustrate cellular foams, Plateau's minimal surfaces, logarithmic spirals, Fibonacci parastichies, Culmann's crane trajectories, and Cartesian coordinate deformations.
   * Inline cross-references connect biological invariants to companion treatises like :cite:`Euclid's Elements <euclid:elements>` and :cite:`Pappus's Synagoge <pappus:synagoge>`.
   * Dynamic figures adapt automatically between light and dark reading themes.

4. Full-Text Search with In-Page Highlighting
   The sidebar search queries the entire unabridged text, chapter notes, and morphological registers. Search results append ``?highlight=`` to highlight matched terms directly in the rendered text.

5. Faceted Navigation & Collection Views
   Browse morphological topics, historical figures, and mathematical invariants via the sidebar index. Collection pages support switching between **Cards**, **Banners**, and **List** layout modes.

6. People, Bibliography & Glossary Tooltips
   Hovering over any naturalist, mathematician, or philosopher (:person:`Sir D'Arcy Wentworth Thompson <thompson>`, :person:`Jay Hambidge <hambidge>`, :person:`St. Thomas Aquinas <aquinas>`, :person:`Peter Guthrie Tait <tait>`), citation (:cite:`thompson_1917`, :cite:`hambidge_1920_vase`), or technical term (:term:`equiangular spiral <equiangular-spiral>`, :term:`gnomon <gnomon>`, :term:`phyllotaxis <phyllotaxis>`, :term:`method of coordinates <method-of-coordinates>`) displays an instant context card.

----

Command-Line & Python Verification API
--------------------------------------

In addition to web reading, the corpus includes command-line tools and Python modules for querying the concordance and verifying source integrity.

Command-Line Interface
~~~~~~~~~~~~~~~~~~~~~~

Inspect concordance entries and verify primary source checksums:

.. code-block:: bash

   # Display apparatus counts and tracked public-domain editions
   geometor-thompson summary

   # Verify SHA-256 digests of all 1917/1920 source witnesses
   geometor-thompson verify

   # Query cross-repository concordance entries
   geometor-thompson concordance --repo wildberger
   geometor-thompson concordance --search spiral

Python API
~~~~~~~~~~

Query the morphological apparatus directly from Python:

.. code-block:: python

   from geometor.thompson.concordance import load_apparatus, verify_sources_manifest

   # Verify 100% public domain primary witnesses
   verification = verify_sources_manifest()
   assert verification["all_valid"]

   # Inspect cross-repository concordance loci
   apparatus = load_apparatus()
   for entry in apparatus.by_unit("unit-3-equiangular-spiral"):
       print(f"{entry.topic}: {entry.chapter} (1917 pp. {entry.pages_1917})")
