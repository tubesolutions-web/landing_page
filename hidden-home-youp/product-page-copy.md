# Hotmart Product Page Copy — Hidden Home Secrets Field Guide

Everything below is ready to paste into the Hotmart product listing. Keep the
wording consistent with the landing page so buyers see the same promise twice.

---

## Product name

```
Hidden Home Secrets — The $1 Bathroom & Cleaning Field Guide
```

## Short description (cards, embeds, search results)

```
43 pages, 31 methods. The dollar-store fixes that actually hold — with the exact ratios, dwell times, and limits a video never has room for.
```

---

## Full description

```
Your bathroom has a recurring problem, and the cleaning aisle has a recurring product for it. That is not a coincidence.

The ring at your waterline is not dirt. The smell that comes back after you have scrubbed everything is not coming from the bowl. The carpet stain that reappeared a week later never actually left. Once you know what is really going on underneath each of those, the fix is usually something that costs about a dollar and is already in your house.

This is every method I have, in one place, with the detail a video cannot carry.

WHAT YOU GET

✓ 31 methods, each with exact ratios, dwell times, and step order
✓ The hydrogen peroxide reset that lifts the ring instead of fading it
✓ The weekly 30-second pour that stops it ever coming back
✓ The rim jet holes nobody has ever cleaned — and what it does to your flush
✓ The monthly tank soak that treats the bowl, tank, and jets at once
✓ Where bathroom odour actually lives: grout, caulk, hinges, and the wax ring
✓ The $2 shaving foam carpet lift, and why flooding a stain makes it return
✓ Which jobs need acid, which need alkali, and why using the wrong one fails
✓ 6 reference charts, including the pH scale mapped to every method
✓ A 12-symptom troubleshooting table — find the symptom, read across
✓ 3 printable checklists plus a complete shopping list with typical prices
✓ Ten common mistakes and six myths, corrected

THE MATH

A 90-cent bottle of hydrogen peroxide, left to sit for half an hour, does what a $9 bowl spray does not — because contact time, not strength, is the constraint.

A $4 box of washing soda covers most of a year of monthly tank treatments. The in-tank tablets it replaces run $60 to $90 a year, and they harden the flapper while they work.

A $2 can of plain shaving foam treats dozens of carpet stains. The branded bottles beside it run $8 to $22 and manage four to six.

Across the whole book, the swap is roughly $50 a year of ordinary supermarket items in place of $250 to $400 of specialised products.

WHAT THIS IS NOT

It is not a list of hacks. Every method states its limits, including the ones that only work in some houses and the two the book tells you not to bother with. Where a problem is hardware rather than chemistry — a failing flapper, a deteriorated wax ring — it says so instead of selling you a method that was never going to work.

FORMAT

43-page PDF, delivered instantly after payment. Reads on any phone, tablet, or computer. The checklists print cleanly on standard paper. No subscription, no app, no account. Yours to keep.

GUARANTEE

7-day money-back guarantee, no questions asked.
```

---

## Settings checklist

Work down this list in the Hotmart product editor.

- [ ] **Price:** $49.99 USD
- [ ] **Product type:** Digital / ebook
- [ ] **File upload:** `Hidden Home Secrets.pdf` (43 pages, ~1.1 MB)
- [ ] **Cover image:** export page 1 of the PDF at 1200×1600 or higher
- [ ] **Delivery:** instant download on approved payment
- [ ] **Refund window:** 7 days, to match the guarantee stated everywhere else
- [ ] **Currency and regional pricing:** confirm what buyers outside the US see
- [ ] **Payment methods:** enable the ones shown on the landing page
- [ ] **Support email:** hello@hiddenhomesecrets.com
- [ ] **Copy the checkout URL** into `PAYMENT_URL` at the top of the script in
      `index.html` — until that is filled in, both buy buttons look normal but
      do nothing, and the reason is logged to the browser console only

---

## Two things to keep honest

**The strikethrough price.** The landing page shows $100 struck through above
$49.99. A struck-through price is a claim that the product was, or genuinely is,
offered at that figure. If it has never sold at $100, remove the strikethrough
and the "SAVE $50 TODAY" line — inventing a former price is a regulated
practice in both the US and the EU.

**The countdown.** `PROMO_END` is set to `"monthly"`, so the bar counts down to
the last second of each month and then rolls into the next one. That claims the
price changes at month end. If the Hotmart price never actually moves, the
countdown is decoration, and returning visitors will notice. Either vary the
price month to month, or set `PROMO_END = null` to hide the bar entirely.
