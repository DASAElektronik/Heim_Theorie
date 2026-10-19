# NORM-BOOK-ETA-INDEX-BRIDGE

Decision ID: `NORM-BOOK-ETA-001`. Date:2026-09-06.
Status: resolved for the local EDM2 definition chain; not an IGW emendation.

## Direct book evidence

EDM2 1996 scan, PDF272/printed266, explicitly defines the bridges
`eta_q0=eta_q` and `eta_1,0=eta`; k=0 is a formal external-field limit.
PDF273/printed267, equation(98), states

```text
eta_qk * fourth_root(pi^4+q^4*(4+k)) = pi
vartheta_qk = 5*eta_qk+2*sqrt(eta_qk)+1.
```

PDF308/printed302, (105), uses eta_1k in A_k. Thus the book chain has
first position q, second position k. Its A1/A2 inputs are (q1,k1)/(q1,k2).
The unindexed vartheta inherited from(29) remains at unindexed eta=eta_1,0;
it is not silently replaced by vartheta_11 or vartheta_12.

The eta-definition pages and the (105) passage were visually inspected by
the source agent; the main agent independently inspected printed266/267
and the previously checked(105) page. Full evidence:
`alpha_audit/reviews/ETA_CONFIGURATION_REVIEW_2026-09-06.md`.
Source hash: `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`.

## Mapping to existing arithmetic helper

The helper is explicitly named `eta_k_q(pi,k=...,q=...)`, independent of
source positional notation. Book eta_12 maps to k=2,q=1; eta_10 to k=0,q=1.
This source mapping no longer relies on a better fit to a printed alpha.

The resulting book(105), Y3=1 right-hand expression is mathematically the
same expression already evaluated in the explicitly separate IGW1982
swapped-index diagnostic. This does NOT relabel that IGW-local variant as
source-literal: IGW(V) prints eta_kq and IGW(IX) prints eta_qk. Those local
source differences remain recorded, and the first audit snapshots stay intact.

## What this decision does not resolve

No proof of the physical eta/k construction, of the charge/potential
averaging, or of Y3=1 follows from locating a definition. No original-edition
priority or historical numerical error mechanism is established.
The new evidence supersedes the earlier research gap only for the book's
local index chain, not the wider theory.
