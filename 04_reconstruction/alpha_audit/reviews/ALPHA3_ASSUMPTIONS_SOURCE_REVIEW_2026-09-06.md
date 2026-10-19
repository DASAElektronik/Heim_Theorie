# alpha3 coefficient assumptions in H004 — 2026-09-06

## Question and checked scope

Does the H004 construction force the coefficient choice used in alpha3, or
does it retain alternatives?  Read only H004 *Elementarstrukturen der Materie
II* (SHA-256 `F094F56EC81D22D17C21C93BA248705DD79100828B813C72682F6A6605593849`),
printed pp.270--275 / PDF 276--281, with p.278/PDF284 checked as the collected
(98c) result.  All pages 270--278 were visually read in
`tmp/pdfs/alpha3_book_origin/edm2-276.png`--`edm2-284.png`.  No claim is made
about unsearched parts of the work.

## What the text constructs before choosing A/B

1. On p.270--271 / PDF276--277, the zone factors alpha_j are to depend on
   q and k, not on the time-variable occupations.  For zone 3 the text
   **proposes** `alpha3(k,q)=f(k)-qF(k,q)`, `F=H+G`.
2. On p.271--272 / PDF277--278, the added requirements `f(1)=1` and
   `x delta f=(x-1)f` lead by the displayed integration to
   `k f(k)=exp(k-1)`.  Thus this term is fixed only conditional on those
   chosen functional requirements.
3. On pp.272--274 / PDF278--280, H and G are each introduced through a
   general additive *logarithmic variation* ansatz.  H has three coefficients
   A1,A2,A3; G has four B1,B2,B3,B4.  The metronic integrations turn the
   selected potential ratios and the X-ratio into logarithms multiplied by
   those coefficients.  This establishes the generic exponentiated product
   form; it does not, at that stage, supply numerical or k-dependent values
   for A_i/B_i.

The potential inputs themselves are not all deductions: p.274 says the G
identification of V_b with an e^(-1)-reduced minimal-condensation potential
can be assumed *spekulativ*.  The text also uses inductively proposed bounds
for the integrals.  The high-z argument for the Fibonacci-like X sequence
motivates the limit ratio Y=xi^2; it is a stated asymptotic/regime step, not
a condition that fixes the A/B coefficients.

## The source's explicit degree of freedom

Printed p.275 / PDF281 says that the constants A_i (i<=3) and B_r (r<=4)
**can be freely prescribed**.  It then makes the particular assignment

```text
A1=B1=B4=1,  2A2=2k+1,  2B2=B3=k,  A3=1-4k,
```

and immediately describes this fixation as optimally adjusted to the
empirical electron and proton data.  Nothing in the checked preceding general
logarithmic ansatz removes that stated freedom or derives these particular
numbers.  Under this *chosen* assignment, and with Y=xi^2, ordinary
exponentiation gives the H/G factors collected in (98c), p.278/PDF284:
`(1+sqrt(eta_qk))*(xi/eta_qk^2)^(2k+1)` and
`(2*xi*eta_qk)^k`.

## Bounded conclusion

The H004 assumptions constrain the architecture (alpha3=f-qF, F=H+G; chosen
potential arguments; logarithmic-product form) and conditionally derive
f(k).  They do **not**, in the examined passage, force the displayed
A_i/B_i assignment.  The author instead expressly marks it as a freely
specifiable, empirically adjusted choice.  This is a primary-source statement
about the local derivation; it neither supplies an alternative fit nor proves
that no additional constraint exists elsewhere in the work.
