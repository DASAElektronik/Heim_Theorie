# NORM-1989-ALPHA-ETA-CROSSREF

Date: 2026-09-06. Decision ID: `NORM-1989-ALPHA-004`.

Checkpoint status: worker and main-agent source reads complete; critic pending.

## Source chain and bounded decision

1989 B59 (PDF page 9 / printed page 18) uses eta_(2,2), eta_(1,1),
eta_(1,2) without a local definition. The same document's PDF page 3 /
printed page 12, paragraph immediately before B8, explicitly names eta_(q,k),
vartheta and eta and says they remain as in (IX). It also states eta_(1,0)=eta
and vartheta_(1,0)=vartheta.

The referenced 1982 PDF page 5 (IX) writes eta_qk with the body
`pi / [pi^4+(4+k)*q^4]^(1/4)`. Thus the 1989 reference-chain normalization is:

```text
eta_(q,k) = eta_k_q(k=k, q=q)
eta_(1,1) = eta_k_q(k=1, q=1)
eta_(1,2) = eta_k_q(k=2, q=1)
eta_(2,2) = eta_k_q(k=2, q=2)
eta = pi/(pi^4+4)^(1/4)
vartheta = 5*eta + 2*sqrt(eta) + 1
```

The eta/vartheta bodies occur in the earlier 1982 (V), PDF page 3; IX itself
prints the indexed eta body, not the complete vartheta definition. The IGW
continuation statement supports this inheritance, but its locator is imprecise
for vartheta. Preserve that provenance qualification.

Do not overwrite the different 1982 ALPHA local eta_kq ordering. The source
itself changes subscript order between blocks. The 1989 kq alternative remains
an explicit counterfactual sensitivity calculation, not a source default.

## Evidence and review

- `alpha_audit/reviews/SOURCE_REVIEW_2026-09-06.md`: independent worker image read.
- Main agent directly inspected 1982 pages 3-5 and 1989 pages 3 and 9.
- `alpha_audit/reviews/MATH_REVIEW_2026-09-06.md`: mathematical/implementation review.

This decision concerns the IGW reference chain only. Neither closeness to a
printed alpha value nor closeness to CODATA selects the index order. A new
transcription or physical derivation is not claimed.
