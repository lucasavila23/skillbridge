# Source ledger and reproduction

**Retrieved:** 2026-10-01. The estimate uses one external quantitative anchor.

## S1 — Official undergraduate enrolment dataset

- **Publisher:** Comunidad de Madrid; underlying source is the Ministry of
  Science, Innovation and Universities' *Estadística de Estudiantes Universitarios*.
- **Title:** *Estudiantes matriculados en estudios de Grado presenciales por universidad*.
- **Catalogue:** [dataset description](https://datos.gob.es/es/catalogo/a13002908-estudiantes-matriculados-en-estudios-de-grado-presenciales-por-universidad).
- **Data:** [official JSON download](https://datos.comunidad.madrid/dataset/a36fddce-c572-4312-ad02-3656cfcd470b/resource/b19b3d6b-058e-46b6-992f-32ec01967363/download/estudiantes-matriculados-en-estudios-de-grado-presenciales-por-universidad.json).
- **Metadata:** [publisher's catalogue API record](https://datos.comunidad.madrid/api/3/action/package_show?id=a36fddce-c572-4312-ad02-3656cfcd470b).
- **Saved copies:** [unaltered data JSON](sources/madrid-undergraduate-enrolment.json)
  and [unaltered metadata JSON](sources/madrid-undergraduate-enrolment-metadata.json).
- **License:** [Creative Commons Attribution 4.0](https://creativecommons.org/licenses/by/4.0/legalcode.es).
  The original files are unchanged; the table below extracts the latest-year
  rows, shortens their labels, and adds our sum and rounding.
- **Data period:** `Año = "2025"` means academic year **2024/25**, because the
  publisher uses the ending year. This is the latest year in the saved data.
- **Status:** all 18 selected rows say `Estado dato = "Provisional"`.
- **Dates:** the metadata's data-update field says **22-10-2025**; its catalogue
  modification timestamp is **2026-09-17**. A catalogue update does not make the
  observations 2026/27 enrolments.

| University label in the dataset, shortened | 2024/25 enrolments |
|---|---:|
| Internacional Villanueva | 1,581 |
| Diseño, Innovación y Tecnología (UDIT) | 2,195 |
| ESIC Universidad | 2,409 |
| Alfonso X el Sabio | 10,822 |
| San Pablo-CEU | 9,794 |
| Alcalá | 16,688 |
| Antonio de Nebrija | 6,538 |
| Autónoma de Madrid | 23,407 |
| Camilo José Cela | 11,156 |
| Carlos III de Madrid | 16,135 |
| Complutense de Madrid | 50,680 |
| Europea de Madrid | 15,491 |
| Francisco de Vitoria | 11,683 |
| Politécnica de Madrid | 28,405 |
| Pontificia Comillas | 10,710 |
| Rey Juan Carlos | 39,966 |
| Internacional de la Empresa | 1,218 |
| CUNEF Universidad | 2,829 |
| **Sum, calculated for this exercise** | **261,707** |
| **Rounded anchor used** | **260,000** |

### Coverage limits

The defensible observed quantity is the sum for these named institutions. The
metadata labels its geographic scope `Toda España`, and the individual rows
have no territory code or campus breakdown. We therefore use the institution
list as a **proxy for the Madrid regional undergraduate population**, not a
verified count of residents or all physical Madrid campuses. No unique-person
identifier is supplied, so cross-institution deduplication cannot be checked.

UNED, UDIMA and IE University do not appear as separate rows. Do not confuse
`Internacional de la Empresa` with IE University. IE operates in both Madrid and
Segovia ([IE's own campus description](https://www.ie.edu/our-spaces/)); neither
its full student body nor our IE interview sample can simply be added to this
anchor. Campus allocation and possible overlap need checking first. Other
out-of-region campuses associated with the listed institutions would likewise
need reconciliation. The model is deliberately approximate at this boundary.

The file covers undergraduate enrolments, rather than all university levels,
city population, annual entrants or graduates. It contains no subject-year
cross-tabulation, internship status, referral access or commitment rates.
Using it for 2026/27 assumes a stable order of magnitude since 2024/25.

### Reproduce the result

From the repository root:

```bash
python3 evidence-log/market-research/calculate.py
```

The calculator selects exactly the 18 distinct 2025 university rows, sums
`Valor`, rounds to the nearest 10,000, then applies the four assumptions. It
also prints the sensitivity cases used in the analysis. It never fetches data
or updates the saved evidence automatically.

SHA-256 of the saved data JSON:

```text
c2fb20853a5299c202938279b1751783f44a9584a36160a234050d7608dfceef
```

## Local evidence and reference material

| Material | Use in this exercise | Boundary |
|---|---|---|
| [Project scope](../../project-scope.md) and [Opportunity](../opportunity.md) | Establish the student-first market and software/web/data, years 2–4 framing | Older general market figures are not used as local prevalence estimates. |
| [Interview notes](../validation/interviews-2026-09-22.md), UV-S01 and UV-S02; [findings](../validation/findings-2026-09-22.md) | Identify experience, support and timing questions worth testing | Two teammate-reported IE accounts; no numeric adoption or regional prevalence estimate. |
| Same notes, UV-B01 and UV-B02; [Experiment Card](../experiment-card.md) | Keep current paid-project supply and business trust as separate open questions | No signed charter or deposit result was supplied; the business experiment threshold is not an observed market conversion rate. |
| User's attached piano-tuner screenshot, received 2026-10-01 | Reference for the sequence: round an anchor, expose assumptions, derive one challengeable number | Its population and piano assumptions are illustrative and do not enter our model. |

All four multipliers are analyst-selected assumptions. No external source or
synthetic persona response has been represented as evidence for those rates.
