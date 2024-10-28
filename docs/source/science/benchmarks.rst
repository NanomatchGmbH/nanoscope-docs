.. _science_benchmarks:

Benchmarks
==========

Embedded Ionization Potential (IP) Benchmark
--------------------------------------------

**Benchmark Summary**

.. table::
   :align: center
   :widths: auto

   ================================  =====================================================
   **Aspect**                        **Details**
   ================================  =====================================================
   Simulated Property Benchmarked    Onset of IP distribution
   Size of Benchmark Set             16 organic materials made of OLED molecules
   Computational Method              Nanoscope software
   Reference Data Sources            Experimental PYS data from literature [a]_, [b]_, [c]_
   Accuracy Achieved                 Standard error of ~60 meV after offset correction
   Key Outcome                       Accuracy close to chemical accuracy
   Published In                      Reference [d]_
   ================================  =====================================================

**Overview**

Here we study **Nanoscope** accuracy in computing the **onset of ionization potential (IP) distributions** for organic
molecules embedded within organic materials by comparing our computational results with experimental data from the
literature [a]_, [b]_, [c]_ for 16 OLED materials.

The IP distribution of the OLED molecules embedded within the respecting organic materials was computed and
compared against *Photoelectron Yield Spectroscopy* (PYS) data from literature. For sake of consistency we use
experimental data derived with similar experimental setup, i.e. the
`AC3 <https://product.rikenkeiki.co.jp/english/ac/ac-3/>`_ setup provided by RIKEN.


*Initial Comparison*

The following figure shows onsets of the IP distributions computed with the *Nanoscope* vs. PYS values measured with AC3,
as reported in literature [a]_, [b]_, [c]_.

.. figure:: benchmarks/ip_results_SID.png
   :alt: IP comparison experiment theory
   :width: 80%
   :align: center

Within each dataset (indicated by different colors corresponding to references [a]_, [b]_, and [c]_), there is agreement
within 100 meV, except for the molecule tmbt.
However, systematic offsets were observed between datasets from different studies.

*Offset Correction*

To address these systematic offsets, we applied corrections based on the mean differences between datasets.
After this adjustment, a strong global correlation emerged:

.. figure:: benchmarks/ip_results_shifted_SID.png
   :alt: IP comparison experiment theory shifted
   :width: 80%
   :align: center

The combined data has a standard error of approximately 60 meV, which is below the experimental error of measurement of 75 meV.

For a comprehensive discussion of this benchmark, please refer to our publication [d]_.

**References**

.. [a] **Green data**: Chem. Phys. Rev. **2**, 031304 (2021); DOI: `10.1063/5.0049513 <https://doi.org/10.1063/5.0049513>`_

.. [b] **Blue data**: Adv. Sci. **8**, 2100586 (2021); DOI: `10.1002/advs.202100586 <https://doi.org/10.1002/advs.202100586>`_

.. [c] **Red data**: Adv. Optical Mater. **7**, 1900630 (2019); DOI: `10.1002/adom.201900630 <https://doi.org/10.1002/adom.201900630>`_

.. [d] **Full description of this benchmark**: SID Symposium Digest of Technical Papers, **55**: 607-610; DOI: `10.1002/sdtp.17597 <https://doi.org/10.1002/sdtp.17597>`_
