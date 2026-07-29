# -*- coding: utf-8 -*-
"""
Hidden Home Secrets — book content.

All prose here is original. It is built on the methods covered on the channel,
expanded with the practical detail a video cannot carry (ratios, dwell times,
failure modes, safety limits).

Deliberately absent: the research citations and market-research figures that
appear in the video scripts. They could not be verified, and unverifiable
sourced claims do not belong in a paid product. Mechanisms are explained in
plain terms instead, and cost figures are presented as honest estimates.
"""

BOOK = {
    "title": "Hidden Home Secrets",
    "subtitle": "The $1 Bathroom & Cleaning Field Guide",
    "byline": "Hidden Home Secrets",
    "channel_url": "https://www.youtube.com/@hiddenhomesecrets1",
    "site": "hiddenhomesecrets.com",
    "contact": "hello@hiddenhomesecrets.com",
}

# ----------------------------------------------------------------------------
# FRONT MATTER
# ----------------------------------------------------------------------------

WHY_THIS_BOOK = [
    "Walk down the cleaning aisle and count the bottles aimed at one room. Bowl "
    "cleaner. Tank tablets. Rim blocks. Odour spray. Grout foam. Carpet foam. "
    "Six products, six price tags, and a bathroom that still smells by Thursday.",

    "That is not a hygiene failure on your part. It is what happens when the "
    "product is built to treat the surface you can see and nothing underneath "
    "it. The stain lifts, the smell fades, and three days later both are back "
    "because the thing actually causing them was never touched.",

    "This book is about the layer underneath. Once you know what a bowl ring is "
    "actually made of, what makes a bathroom smell after it has been cleaned, "
    "and why a carpet stain returns a week later, the fixes stop looking like "
    "folk remedies and start looking obvious. Most of them cost about a dollar.",

    "Nothing here needs a special order, a rented machine, or a service call. "
    "Everything is a supermarket, pharmacy, or laundry-aisle item you have "
    "walked past for years.",
]

HOW_TO_USE = [
    "Read Part I first. It is short, and it is the part that makes every method "
    "after it make sense. If you skip it, the rest reads like a list of tricks. "
    "If you read it, it reads like a system.",

    "After that, go where your problem is. Each entry is self-contained: what "
    "the situation is, what to do about it, an insider detail, and what it "
    "saves you.",

    "Where a method has a limit, the limit is stated. Where something can go "
    "wrong, it says so. A cleaning method that only works in some houses is "
    "more useful when you know which houses.",

    "The reference section at the back is the part you will actually keep "
    "coming back to: the troubleshooting table, the shopping list, and the "
    "maintenance calendar. Print those.",
]

SAFETY_NOTE = [
    "Three rules run through this entire book, and they matter more than any "
    "single method in it.",

    "Never mix cleaning products. Not bleach and vinegar, not bleach and "
    "ammonia, not bleach and anything acidic. These combinations produce toxic "
    "gas in an enclosed bathroom. If you have used one product, flush and "
    "ventilate before reaching for another.",

    "Test on a hidden patch first. Grout, natural stone, vinyl, and carpet all "
    "vary. A corner behind the door tells you in ten minutes what a whole floor "
    "would tell you too late.",

    "Wear gloves for anything strongly alkaline or acidic, and open a window. "
    "Washing soda at pH 11.4 is not dangerous, but it will dry and irritate "
    "skin over a long contact, and nobody enjoys getting it in an eye.",
]

# ----------------------------------------------------------------------------
# PARTS AND ENTRIES
# ----------------------------------------------------------------------------
# Each entry: kicker, title, hook, fix (list of paragraphs), tip, saves

PARTS = [

# ============================================================ PART I
{
 "num": "PART I",
 "title": "What You Are Actually Fighting",
 "subtitle": "Four ideas that explain every method in this book",
 "intro": "Every recurring cleaning problem in a bathroom traces back to one of "
          "four things: a living film, an acid crystal, a mineral deposit, or a "
          "porous surface. Learn to tell them apart and you stop guessing at "
          "products.",
 "entries": [
  {
   "kicker": "FOUNDATIONS · THE RING",
   "title": "The Brown Ring Is Not Dirt",
   "hook": "You scrub it away on Sunday. By Wednesday there is a shadow of it "
           "again, and by the next weekend it is fully back. Scrubbing harder "
           "has never once made it last longer.",
   "fix": [
     "That ring at the waterline is two things layered together. Underneath is "
     "biofilm: a colony of bacteria that has bonded itself to the porcelain. On "
     "top of it, and trapped in it, are mineral deposits carried in by hard "
     "water. The brown colour usually comes from iron and manganese in the "
     "supply.",

     "Biofilm is the reason scrubbing is temporary. A brush removes the visible "
     "top layer, but the colony is anchored down in the microscopic pits of the "
     "glaze, below where bristles reach. What you removed was the part you "
     "could see. What stayed behind rebuilds, and a re-established colony comes "
     "back faster than the first one did because the anchor points are already "
     "there.",

     "This is also why a stronger product disappoints. Most bowl cleaners are "
     "built to kill on contact and rinse away. They do that well. But contact "
     "time in a toilet bowl is measured in seconds before dilution, and a "
     "surface kill leaves the anchored layer untouched.",

     "The methods that hold are the ones that either break the anchoring itself "
     "or change the surface so a new colony cannot get a grip. That is the "
     "whole logic behind Part II.",
   ],
   "tip": "If the ring returns in under a week, you have biofilm. If it takes a "
          "month and feels chalky, you have mineral scale. Different problem, "
          "different chemistry — see the troubleshooting table at the back.",
   "saves": "Understanding this one distinction is what stops the $6-a-fortnight "
            "rim-block habit: roughly $150 a year, per toilet.",
  },
  {
   "kicker": "FOUNDATIONS · ODOUR",
   "title": "Why The Smell Survives A Deep Clean",
   "hook": "The bathroom was scrubbed yesterday. This morning, walking in, it "
           "is there again — faint, sharp, unmistakable. Nothing looks dirty.",
   "fix": [
     "Urine that reaches a surface starts breaking down within minutes. Bacteria "
     "convert the urea in it to ammonia, which is the sharp note you notice "
     "first. That part is water soluble and mops away.",

     "The problem is what forms next. As the breakdown continues, uric acid "
     "crystals are left behind, and those are not water soluble. You can mop "
     "them, bleach them, and steam them, and they stay exactly where they are. "
     "They sit in anything porous within arm's reach of the toilet.",

     "Then humidity does the rest. On a warm morning or after a hot shower, "
     "moisture reactivates the crystals and they release odour into the room "
     "again. The cycle repeats indefinitely because nothing you have done has "
     "removed the source — only the smell it gave off that day.",

     "Bleach makes this especially confusing. Bleach is a disinfectant. It kills "
     "the bacteria producing the ammonia, so the room smells better for a few "
     "hours, but it leaves the crystals themselves intact. The fuel is still "
     "there. Only the flame went out.",
   ],
   "tip": "Uric acid crystals are acidic. That single fact is why an alkaline "
          "compound dissolves them and a disinfectant does not. Part IV is "
          "built entirely on it.",
   "saves": "Stops the air-freshener and plug-in cycle, commonly $60 to $110 a "
            "year, that was never going to fix anything.",
  },
  {
   "kicker": "FOUNDATIONS · WATER",
   "title": "The Mineral Layer Underneath Everything",
   "hook": "White crust on the tap. A chalky rim that feels rough. A flush that "
           "has quietly weakened over three years without you noticing the day "
           "it changed.",
   "fix": [
     "Most homes are on hard water, meaning dissolved calcium and magnesium are "
     "carried in with every litre. Every flush leaves a trace of it behind at "
     "the waterline. Individually the deposit is invisible; over months it "
     "builds into scale you can feel with a fingernail.",

     "Scale matters beyond appearance. It builds inside the small jet holes "
     "under the rim, narrowing them and weakening the flush. It builds on the "
     "flapper seat in the tank, stopping the rubber from sealing properly, "
     "which makes the toilet run intermittently and waste water.",

     "Scale is alkaline-forming and mineral. That means acid dissolves it and "
     "alkaline products largely do not. This is the exact opposite of the uric "
     "acid problem, which is why one product cannot sensibly do both jobs.",

     "Get this the wrong way round and you will conclude a perfectly good method "
     "does not work. Vinegar on biofilm underwhelms. Baking soda on heavy scale "
     "underwhelms. Each is fine at its own job.",
   ],
   "tip": "Drag a fingernail across the ring. If it scrapes off gritty and "
          "pale, treat it as scale and reach for acid. If it smears and is "
          "brown or pink, treat it as biofilm.",
   "saves": "Clearing jet-hole scale restores flush force, which is usually the "
            "real fix for a toilet you were about to call a $150 plumber about.",
  },
  {
   "kicker": "FOUNDATIONS · SURFACES",
   "title": "Porous, Non-Porous, And Why It Decides Everything",
   "hook": "Baking soda transformed one person's bathroom and did nothing at "
           "all in another's. Same product, same amount, opposite verdicts.",
   "fix": [
     "Porcelain is glazed and effectively non-porous. Odour does not live in it. "
     "Sprinkling a deodorising powder into the bowl accomplishes very little, "
     "because the bowl was never where the smell was coming from.",

     "Grout, caulk, unsealed tile, vinyl seams, and the floor around the toilet "
     "base are all porous. They absorb. Years of small splashes soak in and stay "
     "in. That is where the odour source actually sits, often several "
     "millimetres deep.",

     "This explains the contradictory reviews. The people for whom a method "
     "'did nothing' usually applied it to the porcelain. The people for whom it "
     "worked applied it to the grout — and gave it time.",

     "Contact time is the second half of the same point. A powder sitting dry on "
     "a surface for five minutes cannot travel down into grout. A solution, "
     "thinned enough to penetrate and left long enough to work, can. Method "
     "beats product almost every time.",
   ],
   "tip": "Before treating anything, ask whether the surface absorbs. If it "
          "does, you need a solution and time. If it does not, you need contact "
          "and technique.",
   "saves": "Prevents the most common wasted purchase in the book: the right "
            "product applied to the wrong surface.",
  },
 ],
},

# ============================================================ PART II
{
 "num": "PART II",
 "title": "The Toilet Bowl",
 "subtitle": "Removing the ring, then making it stop coming back",
 "intro": "Two separate jobs live in this part. The first is stripping what is "
          "already there. The second, and the one almost everyone skips, is "
          "changing the surface so the next colony cannot establish itself.",
 "entries": [
  {
   "kicker": "BOWL · THE RESET",
   "title": "The Hydrogen Peroxide Reset",
   "hook": "One bottle from the pharmacy, about a dollar, and thirty minutes of "
           "leaving it completely alone. This is the single highest-value "
           "method in the book.",
   "fix": [
     "Buy standard 3% hydrogen peroxide — the brown bottle, first-aid aisle. Do "
     "not buy a higher concentration; stronger is not better here and is "
     "considerably less pleasant to handle.",

     "Flush, and work while the bowl is still refilling so the water level is "
     "low and you are not immediately diluting everything. Pour roughly 240 ml "
     "(8 oz) directly under the rim, moving around the full circle so it runs "
     "down the entire inner surface rather than straight into the water.",

     "Now leave it. Minimum thirty minutes, an hour is better. Do not scrub "
     "during this time and do not flush. The faint fizzing is the peroxide "
     "reacting with organic material in the biofilm, and that reaction is doing "
     "the work your brush used to do badly.",

     "After the dwell, one pass with the brush at the waterline, then flush. On "
     "a bowl that has never had this done, the ring generally lifts completely "
     "rather than lightening. If a shadow remains, it is mineral scale rather "
     "than biofilm, and that needs the vinegar treatment later in this part.",
   ],
   "tip": "Peroxide degrades in light, which is why it is sold in an opaque "
          "brown bottle. Decant it into a clear spray bottle and you will have "
          "weak water within a fortnight. Keep it in the bottle it came in.",
   "saves": "About $1.10 a treatment against $6 to $9 for a bowl cleaner that "
            "buys you three days.",
  },
  {
   "kicker": "BOWL · MAINTENANCE",
   "title": "The Weekly Pour That Ends The Cycle",
   "hook": "The reset strips the bowl. This is the thirty-second habit that "
           "means you never have to do the reset again.",
   "fix": [
     "Once a week, pour roughly 120 ml (4 oz) of the same 3% peroxide into the "
     "bowl. No dwell time to manage, no scrubbing, no kneeling. Pour it, walk "
     "away, and flush next time you are in the room.",

     "The logic is population control rather than cleaning. A visible ring only "
     "appears once a colony reaches a certain density. A weekly dose keeps the "
     "population below that threshold permanently, so the ring never has the "
     "chance to form in the first place.",

     "Expect this to take a few weeks to prove itself. You are not watching "
     "something disappear; you are watching something fail to appear. After "
     "roughly two months of consistency, the waterline simply stays clear "
     "without brushing.",

     "Best time to do it is last thing at night, in the least-used bathroom "
     "first. Longer standing time before the next flush means more contact.",
   ],
   "tip": "Attach it to something you already do weekly — bin night, laundry "
          "day — rather than trying to remember it on its own. The method is "
          "easy; the consistency is the hard part.",
   "saves": "Roughly $15 a year in peroxide replaces $80 to $120 a year of bowl "
            "cleaners and tablets.",
  },
  {
   "kicker": "BOWL · THE BLIND SPOT",
   "title": "The Jet Holes Nobody Has Ever Cleaned",
   "hook": "Crouch down and look up under the rim with a phone torch. Almost "
           "nobody has ever done this. What is in there explains a great deal.",
   "fix": [
     "Under the rim is a ring of small angled holes where tank water enters "
     "during a flush. They point inward and upward, in a geometry a toilet "
     "brush physically cannot reach. In most homes they have never been "
     "touched.",

     "Two things accumulate in them. Mineral scale narrows the openings and "
     "progressively weakens the flush — a change slow enough that you adapt to "
     "it rather than notice it. Biofilm builds in the channels behind them, "
     "sheltered from every product you have poured in, because bowl cleaners "
     "drain into the water before they ever contact the channel.",

     "Clearing them takes an old toothbrush and about two minutes. Work the "
     "bristles up into each hole around the full circle. On a neglected toilet "
     "expect dark gritty material to come out. This is unpleasant and worth "
     "doing exactly once properly.",

     "Follow immediately with the peroxide reset so the newly exposed surface "
     "gets treated rather than simply re-colonised.",
   ],
   "tip": "If your bowl needs two flushes to clear and always has, this is "
          "usually why. It is almost never the toilet being old.",
   "saves": "Restoring flush power here is frequently the entire fix for a "
            "complaint people replace a $250 toilet over.",
  },
  {
   "kicker": "BOWL · THE BARRIER",
   "title": "The Baby Oil Barrier",
   "hook": "Everything so far removes what is there. This makes the surface "
           "itself hostile to what comes next, and takes ninety seconds.",
   "fix": [
     "Plain baby oil is refined mineral oil: colourless, odourless, chemically "
     "inert, and it does not react with water or feed bacteria. Worked into "
     "porcelain, it leaves a thin water-repellent film that sits in the "
     "microscopic pits where biofilm would otherwise anchor.",

     "Order matters absolutely. Clean first, seal second. Applying oil over an "
     "existing ring seals the problem in and wastes the effort entirely. Do the "
     "peroxide reset and the jet holes first, and only then do this.",

     "Flush to wet and cool the surface. Put about a teaspoon of baby oil onto "
     "a folded pad of toilet paper or a disposable cloth. Work it along the "
     "inner rim, pressing lightly into the channels around the jet holes, then "
     "down both sides toward the trap. You are coating, not polishing — a thin "
     "even film, never a visible pool sitting in the water.",

     "Flush again. The water drains but the film stays bonded, because oil and "
     "water do not mix. Re-coat roughly monthly.",
   ],
   "tip": "Use plain baby oil, not a scented, aloe, or 'moisturising' version. "
          "The additives are exactly the organic material you are trying to "
          "stop feeding the colony.",
   "saves": "A $3 bottle covers one toilet for around six months. Call it $6 a "
            "year against $80-plus of bowl products.",
  },
  {
   "kicker": "BOWL · SCALE",
   "title": "Vinegar, For Scale And Nothing Else",
   "hook": "Vinegar has a genuine job in this book. It is just not the job the "
           "internet keeps giving it.",
   "fix": [
     "White vinegar is roughly 5% acetic acid, and acid dissolves mineral scale. "
     "On the chalky, gritty, pale deposits that hard water leaves, it works "
     "properly and cheaply.",

     "On biofilm it underperforms badly. It is mildly acidic, and several of the "
     "organisms responsible for rust-coloured staining are entirely comfortable "
     "in mildly acidic conditions. This is the source of most 'vinegar did "
     "nothing' conclusions — right product, wrong problem.",

     "For a heavy scale ring: shut off the supply valve, flush to empty the "
     "bowl, then pour in enough undiluted white vinegar to cover the deposits. "
     "Leave it several hours or overnight, then brush and restore the supply. "
     "The scale should come away with almost no pressure.",

     "Treat this as a reset, not a routine. Once the existing scale is gone, "
     "the weekly peroxide pour and the monthly oil coat handle maintenance far "
     "more cheaply than a monthly vinegar soak ever will.",
   ],
   "tip": "Vinegar and hydrogen peroxide cancel each other out. Never combine "
          "them in one application. Use them in sequence — vinegar for the "
          "scale, flush thoroughly, peroxide for the biofilm.",
   "saves": "Around 40 cents of vinegar replaces a $9 descaling product, and "
            "unlike acid-based removers it will not etch the glaze.",
  },
  {
   "kicker": "BOWL · SAFETY",
   "title": "The Combinations That Send People To Hospital",
   "hook": "This is the shortest entry in the book and the only one where "
           "getting it wrong is genuinely dangerous.",
   "fix": [
     "Bleach and vinegar release chlorine gas. Bleach and ammonia release "
     "chloramine vapour. Both happen readily at household concentrations, and a "
     "bathroom is a small room that is frequently poorly ventilated.",

     "'I only used a little' is not protective. The reaction does not care about "
     "your intentions, and the early symptoms — burning eyes, coughing, tight "
     "chest — arrive after exposure has already happened.",

     "Assume any commercial cleaner may contain bleach unless the label says "
     "otherwise, and assume many contain ammonia. If you have used one product "
     "and want to try another, flush thoroughly, open a window, and leave the "
     "room for a while first.",

     "Nothing in this book requires mixing anything. Every method here is a "
     "single substance used on its own. Where two are used on the same surface, "
     "the instruction is always to flush in between.",
   ],
   "tip": "If you ever notice a sharp bite at the back of your throat while "
          "cleaning, leave the room and ventilate it. Do not stay to finish.",
   "saves": "Not a money entry. This one is the reason the rest of the book "
            "keeps to single-ingredient methods.",
  },
 ],
},

# ============================================================ PART III
{
 "num": "PART III",
 "title": "The Tank And Flush System",
 "subtitle": "The half of the toilet almost nobody ever opens",
 "intro": "Most people have never lifted the tank lid. Yet the tank is where "
          "odour originates, where scale quietly destroys hardware, and where a "
          "single monthly treatment does more than any product sold for the "
          "bowl.",
 "entries": [
  {
   "kicker": "TANK · THE SOAK",
   "title": "The Washing Soda Tank Soak",
   "hook": "One scoop, thirty minutes, two flushes. This treats the bowl, the "
           "tank, and the jet holes at the same time.",
   "fix": [
     "Washing soda is sodium carbonate — laundry aisle, around $4 a box. It is "
     "not baking soda and not laundry detergent. Check the label reads sodium "
     "carbonate, because the two soda products sit side by side and are "
     "constantly confused.",

     "The difference is not marginal. Baking soda sits around pH 8.3; washing "
     "soda around 11.4. The pH scale is logarithmic, so that is a difference of "
     "roughly a thousandfold in alkalinity, which is why one shifts hardened "
     "deposits in half an hour and the other does not.",

     "Dissolve one level scoop, about two tablespoons, into the tank water — the "
     "tank, not the bowl. This is the step everyone gets wrong. Leave it thirty "
     "minutes without flushing. The solution circulates over the flapper, the "
     "flapper seat, the overflow tube, and the fill valve housing, breaking "
     "down the scale and biofilm coating all of them.",

     "Then flush twice. The first pulls the solution down through the jet holes "
     "and across the waterline; the second rinses clear. Once a month is ample.",
   ],
   "tip": "Wear gloves and keep it off your skin for long contact. At pH 11.4 "
          "it is not corrosive, but it will dry and irritate skin, and it is "
          "genuinely unpleasant in an eye.",
   "saves": "Around $1 a treatment, roughly $11 a year, against $80 to $120 in "
            "bowl cleaners, tablets, and rim blocks.",
  },
  {
   "kicker": "TANK · HARDWARE",
   "title": "Why Blue Tablets Cost You A Flapper",
   "hook": "The tablet that promises months of clean is quietly working on your "
           "tank hardware the entire time.",
   "fix": [
     "In-tank tablets sit in standing water and release concentrated chemistry "
     "continuously, for weeks, directly against rubber and plastic components "
     "that were never designed for constant chemical exposure.",

     "The visible result is a flapper that hardens, loses flexibility, and stops "
     "sealing cleanly. The audible result is a toilet that runs intermittently "
     "between flushes, or a fill valve that cycles when nobody has used it. "
     "That running is water you are paying for continuously.",

     "Several manufacturers explicitly void warranty cover where in-tank "
     "chemical tablets have been used. That is worth knowing before you drop "
     "the next one in.",

     "A periodic soak is a different proposition entirely: a dilute solution for "
     "thirty minutes, once a month, then flushed away. The tablet is a "
     "permanent chemical residency. Duration is the whole difference.",
   ],
   "tip": "Lift the lid and look at your flapper now. Rubber that is stiff, "
          "cracked, or chalky is at end of life. Replacement is about $8 and "
          "ten minutes.",
   "saves": "Ends roughly $70 a year of tablets while extending a $8 part that "
            "otherwise fails early and wastes water daily.",
  },
  {
   "kicker": "TANK · PERFORMANCE",
   "title": "Getting The Flush Power Back",
   "hook": "It used to clear in one flush. Now it takes two, and you cannot "
           "name the week that changed.",
   "fix": [
     "A weak flush is usually a delivery problem, not a pressure problem. Water "
     "reaches the bowl through the jet holes under the rim and, on most models, "
     "a larger siphon jet at the bottom. Scale narrows all of them gradually.",

     "Work through it in order. First clear the jet holes mechanically with a "
     "toothbrush or a piece of wire. Then run the washing soda tank soak so the "
     "alkaline solution is pushed through the openings from the tank side. Two "
     "or three monthly treatments generally restore noticeably more force.",

     "Next check the tank water level. It should sit roughly 25 mm below the top "
     "of the overflow tube. Too low and every flush is underpowered regardless "
     "of how clean the passages are. The fill valve has an adjustment for this.",

     "If the level is right and the passages are clear and it still flushes "
     "poorly, you are looking at a partial blockage further down the trap, and "
     "that is a plunger or auger job rather than a chemistry one.",
   ],
   "tip": "Test after each step rather than doing all three at once. Otherwise "
          "you will never know which one actually mattered in your house.",
   "saves": "Avoids the $150 call-out and the $250 replacement for a toilet "
            "that was only ever partially blocked.",
  },
  {
   "kicker": "TANK · THE HONEST ANSWER",
   "title": "The Pumice Question",
   "hook": "This method circulates widely, including on this channel. It "
           "deserves a straight answer rather than an enthusiastic one.",
   "fix": [
     "The claim is that a lemon-sized chunk of raw pumice left in the tank "
     "suppresses biofilm — partly by holding the water mildly alkaline, partly "
     "by releasing fine particles that disturb the anchor points on the "
     "porcelain.",

     "The alkalinity half is reasonable. Pumice is mildly alkaline and a tank is "
     "a small closed volume, so a modest sustained pH shift is plausible, and it "
     "would genuinely be unfavourable to the organisms behind rust-coloured "
     "staining.",

     "The abrasion half is where honesty is required. The supporting evidence is "
     "forum reports, not testing. Deliberately introducing abrasive particles "
     "into a system whose seal depends on a soft rubber flapper is a real risk, "
     "and reassurance on that point is not the same as data. Manufacturers do "
     "not endorse it.",

     "If you want to try it, use a mesh bag — the aquarium type, around 50 "
     "cents. You keep the alkalinity effect while substantially limiting loose "
     "particles. Check the flapper every few months. If your toilet is old or "
     "the flapper is already stiff, skip this method entirely and use the "
     "monthly soak instead, which achieves the same end with no hardware risk.",
   ],
   "tip": "A $1 method that risks an $8 part and a running toilet is not "
          "automatically a bargain. The washing soda soak gets you there with "
          "nothing at stake.",
   "saves": "Listed for completeness, not recommended over the soak. The soak "
            "is the safer route to the same result.",
  },
  {
   "kicker": "TANK · LIMITS",
   "title": "When Cleaning Is Not The Answer",
   "hook": "Some symptoms are hardware. No amount of correct chemistry will "
           "touch them, and continuing to try wastes months.",
   "fix": [
     "A toilet that runs continuously or cycles on its own has a sealing "
     "failure. A soak may help if scale on the flapper seat is the cause, but "
     "perished rubber is perished rubber. Flapper, about $8. Fill valve, about "
     "$15. Both are ten-minute jobs with no specialist tools.",

     "Water on the floor around the base is not a cleaning problem. It is a seal "
     "or a supply-line issue and it will damage the subfloor if left. Stop "
     "cleaning it up repeatedly and find the source.",

     "A smell that is worst after the toilet has sat unused, and that no amount "
     "of surface work touches, points at the wax ring beneath the base rather "
     "than anything you can reach. That is covered in Part IV.",

     "Knowing where cleaning stops is part of the skill. The purpose of this "
     "book is to stop you buying products that were never going to work — and "
     "that includes not treating a $8 mechanical fault with $80 of chemistry.",
   ],
   "tip": "Put a few drops of food colouring in the tank and do not flush. If "
          "colour appears in the bowl within twenty minutes, the flapper is "
          "leaking. Cheapest diagnostic in this book.",
   "saves": "A silently running toilet can waste a startling volume of water "
            "daily. The part costs $8.",
  },
 ],
},

# ============================================================ PART IV
{
 "num": "PART IV",
 "title": "Killing Bathroom Odour At The Source",
 "subtitle": "The smell is not in the bowl, and it never was",
 "intro": "The single most common mistake in bathroom cleaning is treating the "
          "porcelain and ignoring everything porous around it. This part goes "
          "where the odour actually lives.",
 "entries": [
  {
   "kicker": "ODOUR · LOCATION",
   "title": "Five Places The Smell Actually Lives",
   "hook": "Before treating anything, know where to aim. Four of these five "
           "spots are routinely cleaned by nobody.",
   "fix": [
     "The floor grout, particularly within about half a metre of the toilet. "
     "Grout is porous, cement-based, and absorbs everything. In a bathroom that "
     "has smelled for years, deposits can sit several millimetres deep.",

     "The caulk bead where the toilet base meets the floor. It absorbs, it is "
     "almost never treated, and it sits at exactly the height that catches "
     "splash.",

     "The floor behind and beside the toilet — the strip between the pan and the "
     "wall that a mop reaches badly and a cloth reaches never. Years of small "
     "accumulation, undisturbed.",

     "The seat hinge points, where the plastic bracket meets the porcelain. Fine "
     "mist from flushing settles and pools in the gap. Most hinges unclip or "
     "unbolt for cleaning, and most people have never once removed them.",

     "The back of the tank where it meets the wall. Rarely reached, never dried, "
     "frequently the source of a smell people attribute to the drain.",
   ],
   "tip": "Do the torch test at night with the light off. Held at a low angle, "
          "a phone torch across the floor shows staining and residue that "
          "overhead lighting flattens out completely.",
   "saves": "Aiming correctly is what turns a $1.50 box of baking soda into a "
            "fix rather than another disappointment.",
  },
  {
   "kicker": "ODOUR · THE METHOD",
   "title": "The Alkaline Solution That Reaches The Crystals",
   "hook": "Baking soda sprinkled dry on a floor for five minutes does nothing. "
           "The same box, used correctly, ends a years-old smell.",
   "fix": [
     "Uric acid crystals are acidic. An alkaline compound neutralises them "
     "chemically rather than masking them — the crystals break down and there is "
     "nothing left to reactivate on a humid morning.",

     "Baking soda is the right compound at about pH 8.3 and around $1.50 a box. "
     "But dry powder cannot travel into grout. You need a solution thin enough "
     "to penetrate, and you need to help it get down.",

     "Mix roughly four tablespoons of baking soda into 500 ml of warm water with "
     "a single drop of dish soap. The soap is a surfactant: it breaks the "
     "water's surface tension so the solution wicks into the grout instead of "
     "beading on top. One drop, not a squeeze — more just creates foam you then "
     "have to rinse.",

     "Apply generously to grout, the caulk bead, and the floor around the base. "
     "Now leave it a minimum of thirty minutes, and longer on a bad case. "
     "Contact time is the entire game. Agitate with an old toothbrush along the "
     "grout lines, then wipe up rather than flooding the area with rinse water.",
   ],
   "tip": "A long-standing smell rarely clears in one pass. The surface layer "
          "neutralises first while deeper deposits keep releasing. Expect two "
          "or three treatments across a fortnight on a bathroom that has "
          "smelled for years.",
   "saves": "About 30 cents a treatment against $8 to $14 for an enzymatic "
            "odour spray.",
  },
  {
   "kicker": "ODOUR · THE MISTAKE",
   "title": "Why Baking Soda And Vinegar Together Is Theatre",
   "hook": "It fizzes dramatically. That fizz is the two ingredients destroying "
           "each other before either one has touched anything.",
   "fix": [
     "An acid and a base neutralise one another. Combine vinegar and baking soda "
     "in a bowl and you get carbon dioxide, water, and a little sodium acetate. "
     "The reaction is genuinely satisfying to watch and almost entirely useless "
     "as a cleaner.",

     "By the time the foam reaches your grout, both active ingredients have "
     "largely cancelled out. What is left is salty water doing a fraction of "
     "what either would have done alone.",

     "Used separately they are both genuinely useful, and they do opposite jobs. "
     "Vinegar's acidity dissolves mineral scale. Baking soda's alkalinity "
     "neutralises uric acid crystals. Combining them means getting neither.",

     "There is one narrow legitimate use: the physical fizzing action can help "
     "lift loose debris in a slow drain. That is mechanical agitation, not "
     "chemistry, and it is not what anyone means when they recommend the "
     "combination for cleaning.",
   ],
   "tip": "If a method's main appeal is that it looks impressive, be "
          "suspicious. The effective methods in this book are almost all "
          "visually boring — pour it, leave it, walk away.",
   "saves": "Stops the wasted vinegar, the wasted baking soda, and the wasted "
            "afternoon.",
  },
  {
   "kicker": "ODOUR · PREVENTION",
   "title": "Sealing Grout So It Stops Absorbing",
   "hook": "Neutralising deals with what is there. Sealing is what stops the "
           "next three years of it soaking in.",
   "fix": [
     "Grout absorbs because it is porous. A penetrating sealer closes those "
     "surface pores so liquid sits on top long enough to be wiped away instead "
     "of soaking in. A bottle runs $12 to $20 and covers a domestic bathroom "
     "floor several times over.",

     "Sequence is critical. Seal a floor that still holds uric acid deposits and "
     "you lock them in permanently. Neutralise thoroughly first, let the floor "
     "dry completely — a full day, longer in a humid bathroom — and only then "
     "seal.",

     "Application is undramatic. Apply along the grout lines with the bottle's "
     "applicator or a small brush, leave the stated dwell, then wipe the excess "
     "off the tile face before it dries. Skip that wipe and you get a hazy film "
     "that is tedious to remove.",

     "Re-seal every two to three years in a bathroom, sooner in a heavily used "
     "one. A drop of water on the grout tells you when: if it beads, the seal "
     "is intact; if it darkens the grout, it is time.",
   ],
   "tip": "Do this the same weekend you finish the neutralising treatments, "
          "while the floor is genuinely clean. Sealing a floor you have only "
          "mostly dealt with is worse than not sealing at all.",
   "saves": "A $15 bottle every few years against repeatedly re-treating a "
            "floor that keeps reabsorbing.",
  },
  {
   "kicker": "ODOUR · THE LIMIT",
   "title": "When It Is The Wax Ring",
   "hook": "Every surface is clean. The grout has been neutralised twice. The "
           "smell is still there. At this point stop cleaning.",
   "fix": [
     "The toilet sits on a wax gasket that seals the base to the floor drain "
     "flange. Over years it can compress unevenly, develop small gaps, or "
     "deteriorate. When it does, sewer gas migrates up around the base.",

     "That gas contains ammonia and hydrogen sulphide, which is why it reads as "
     "urine odour and misdirects people into cleaning for months. The source is "
     "underneath the toilet, so no surface treatment can reach it.",

     "The diagnostic is timing. If the smell is worst after the toilet has sat "
     "unused for a stretch — first thing in the morning, or returning from a "
     "trip — a failing seal is the likely cause, because gas concentrates when "
     "the bowl water has not refreshed.",

     "The part costs a few dollars. Fitting it means draining and lifting the "
     "toilet, which is a genuine job. Competent DIY territory if you are "
     "comfortable, and an entirely reasonable thing to pay a plumber for once, "
     "given the alternative is cleaning a smell that will never go away.",
   ],
   "tip": "Check for movement first. If the toilet rocks even slightly when you "
          "shift your weight on it, the seal is already compromised and this is "
          "almost certainly your answer.",
   "saves": "One correct diagnosis against years of products aimed at a smell "
            "that was never on the surface.",
  },
 ],
},

# ============================================================ PART V
{
 "num": "PART V",
 "title": "Floors, Grout And Carpet",
 "subtitle": "Out of the bathroom, same principles",
 "intro": "Carpet has its own failure mode, and it is the reason your stains "
          "come back. Understand wicking and the rest of this part follows.",
 "entries": [
  {
   "kicker": "CARPET · THE METHOD",
   "title": "The Shaving Foam Stain Lift",
   "hook": "A $2 can from the shaving aisle, and the stain does not come back "
           "next month. The reason has nothing to do with cleaning power.",
   "fix": [
     "Use plain white aerosol shaving foam. Not gel, not a moisturising formula, "
     "not one with aloe or a cooling agent. The cheapest can on the shelf is "
     "precisely the right one — the additives in the premium versions are what "
     "cause residue.",

     "Apply foam directly to the stain. Do not dilute it and do not wet the area "
     "first. Cover the stain with roughly 5 mm of foam and leave it thirty "
     "seconds. Two full minutes on a dried or set stain.",

     "Then blot, and blot properly, because technique matters more than product "
     "here. Take a clean white cloth — white, because coloured cloth can "
     "transfer dye into damp carpet. Press firmly straight down, lift straight "
     "up, move to a fresh section of cloth, repeat. Never rub and never scrub.",

     "Continue until the foam lifting onto the cloth comes up clean. No rinsing "
     "is needed; residual foam dissipates as the carpet dries. Because this is a "
     "product designed for skin, there is no need to keep children or pets off "
     "the area while it dries.",
   ],
   "tip": "Test on a hidden patch first — inside a wardrobe, under a sofa. This "
          "is safe on wool, nylon, and polyester, but test anyway. Ten minutes "
          "of caution against a visible patch in the middle of a room.",
   "saves": "About $2 a can, treating many stains, against $8 to $22 a bottle "
            "for products that manage four to six.",
  },
  {
   "kicker": "CARPET · THE CAUSE",
   "title": "Wicking: Why The Stain Came Back",
   "hook": "It vanished completely. Three days later it was back in exactly the "
           "same outline. You did nothing wrong — you used the wrong approach.",
   "fix": [
     "Carpet is three layers: the pile you see, the backing, and the pad "
     "beneath. Most liquid stains soak through all three. The stain you can see "
     "is the shallowest part of the problem.",

     "Flooding the area with cleaner pushes dissolved pigment further down into "
     "the backing and pad. The surface looks perfect while it is wet. Then, as "
     "the carpet dries from the bottom up, moisture carries that pigment back "
     "toward the surface and redeposits it. That is wicking, and it is why the "
     "outline reappears days later.",

     "Foam avoids this because it is structurally load-bearing. It sits on the "
     "pile rather than immediately soaking through, and the surfactants lift the "
     "staining compound up into the foam instead of driving it down. You then "
     "remove the foam. The backing never saturates, so there is nothing to wick "
     "back.",

     "The same logic explains why scrubbing fails. Scrubbing opens the fibre and "
     "spreads the stain sideways, turning a coin-sized mark into a plate-sized "
     "shadow. Press and lift. Never drag.",
   ],
   "tip": "If a stain has already come back once, it is in the pad. Expect two "
          "or three foam treatments spaced a day apart, each pulling up "
          "progressively less.",
   "saves": "Avoids the $35 machine hire that, used with too much water, makes "
            "wicking worse rather than better.",
  },
  {
   "kicker": "CARPET · PETS",
   "title": "Pet Accidents: Fresh Versus Set",
   "hook": "These are two completely different problems that happen to look "
           "identical, and the wrong method on the wrong one wastes both.",
   "fix": [
     "Fresh, within about fifteen minutes, is a stain problem. Blot up as much "
     "liquid as possible with a dry cloth first — this is the step that "
     "determines everything after it. Press hard, use fresh cloth repeatedly, "
     "get as much out as you physically can. Then apply foam as normal.",

     "Set and smelly is a uric acid problem, and foam will not touch it. Foam is "
     "a stain remover, not an odour eliminator. The crystals need either an "
     "enzymatic cleaner formulated to break them down, or the alkaline approach "
     "from Part IV.",

     "You can usually tell which you have. If it is visible but not especially "
     "smelly, treat as stain. If you can smell it before you can see it, "
     "particularly on a warm day, it is crystals and it has been there a while.",

     "Repeat offences at one spot are territorial marking reinforced by residual "
     "scent you cannot detect but the animal can. Until the odour source is "
     "genuinely eliminated rather than covered, the behaviour continues.",
   ],
   "tip": "Never use an ammonia-based cleaner on pet urine. Ammonia is one of "
          "the breakdown products of urine, so to the animal you have just "
          "marked the spot yourself.",
   "saves": "Correct diagnosis avoids repeatedly buying the wrong category of "
            "product at $10 to $20 a time.",
  },
  {
   "kicker": "FLOORS · GROUT",
   "title": "Floor Grout Beyond The Bathroom",
   "hook": "Kitchen and hallway grout goes grey gradually enough that you "
           "recalibrate to it. Compare against a cupboard corner sometime.",
   "fix": [
     "Outside the bathroom the problem is different: ground-in soil and grease "
     "rather than uric acid. That means the alkaline approach still works, but "
     "you want the stronger alkali. Washing soda, not baking soda.",

     "Two tablespoons of washing soda in 500 ml of warm water, applied along the "
     "grout lines, left fifteen to twenty minutes, then agitated with a stiff "
     "brush. Alkalinity converts greasy residue into something water-soluble, "
     "so it lifts rather than smearing.",

     "Work in sections of roughly a square metre and wipe up as you go. Let an "
     "alkaline solution dry on tile and you get a dull film that then needs its "
     "own cleaning pass.",

     "Gloves for this one. Repeated contact with a pH 11.4 solution will leave "
     "your hands dry and irritated in a way that is easy to avoid.",
   ],
   "tip": "Not for natural stone. Marble, limestone, and travertine are "
          "calcium-based and both strong alkali and acid will etch them. Stone "
          "needs a pH-neutral cleaner made for it.",
   "saves": "Roughly 50 cents a treatment against $10 to $15 for dedicated "
            "grout products, and considerably better on grease.",
  },
  {
   "kicker": "SURFACES · HARD WATER",
   "title": "Glass, Screens And Chrome",
   "hook": "The cloudy film on a shower screen is the same chemistry as the "
           "ring in your toilet, which means it takes the same answer.",
   "fix": [
     "Those white spots are mineral deposits left as water evaporates. They are "
     "not soap scum, although the two coexist happily. Because they are mineral, "
     "acid removes them and detergent largely does not.",

     "White vinegar, undiluted, in a spray bottle. On a screen, spray generously "
     "and leave ten to fifteen minutes — on a vertical surface it will run, so "
     "expect to reapply once or twice. A cloth soaked in vinegar and laid "
     "against the glass holds contact far better than spraying alone.",

     "Wipe, then rinse and dry with a squeegee or a microfibre cloth. The drying "
     "step is what stops the film reforming immediately, and it is the step "
     "everyone skips.",

     "Thirty seconds with a squeegee after each shower prevents essentially all "
     "of it. That is the entire maintenance regime, and it outperforms any "
     "product you can buy for the purpose.",
   ],
   "tip": "Keep vinegar off natural stone surrounds and away from any "
          "unlacquered brass fittings. On chrome and glass it is entirely "
          "safe.",
   "saves": "About 20 cents of vinegar against $7 to $12 for a limescale spray.",
  },
  {
   "kicker": "TECHNIQUE · THE BLOT",
   "title": "Press And Lift, Never Rub",
   "hook": "One technique underlies every fabric method in this part. Get it "
           "wrong and the best product available will still disappoint you.",
   "fix": [
     "Rubbing does three things, all bad. It spreads the stain outward, turning "
     "a small mark into a large faint one. It drives the staining compound "
     "deeper toward the backing. And on cut-pile carpet it distorts the fibre "
     "permanently, leaving a patch that catches light differently even once the "
     "stain is gone.",

     "Blotting does the opposite. Press straight down so the cloth contacts the "
     "full depth of the pile, hold for a couple of seconds, and lift straight "
     "up. Capillary action moves the liquid into the cloth. Move to a clean "
     "section and repeat.",

     "Use far more cloth than feels necessary. A saturated section stops "
     "absorbing and starts redepositing. Old white towels cut into squares are "
     "ideal — plentiful, and you can see progress on them.",

     "Work from the outside of the stain toward the centre. Working outward "
     "enlarges the affected area, which is the one thing you cannot undo later.",
   ],
   "tip": "Stand on the cloth. Body weight through a folded towel pulls far more "
          "liquid out of a pad than hand pressure ever will, which matters "
          "enormously on a fresh spill.",
   "saves": "Free. Frequently the difference between a stain lifting fully and "
            "a permanent shadow.",
  },
 ],
},

# ============================================================ PART VI
{
 "num": "PART VI",
 "title": "The $1 Ingredient Playbook",
 "subtitle": "What each one does, what it cannot do, and what it costs",
 "intro": "Five substances cover almost everything in this book. Knowing the "
          "boundaries of each is what stops you reaching for the wrong one and "
          "concluding the method was rubbish.",
 "entries": [
  {
   "kicker": "PLAYBOOK · OXIDISER",
   "title": "Hydrogen Peroxide, 3%",
   "hook": "The brown bottle. Around $1.10, pharmacy or supermarket. The single "
           "most useful item in this book.",
   "fix": [
     "Good for: biofilm in the toilet bowl, general bathroom disinfecting, "
     "organic stains, and mildew on non-porous surfaces. It works by releasing "
     "oxygen on contact with organic material, which breaks down both the "
     "organisms and the structures holding them in place.",

     "Not good for: mineral scale. It has no meaningful acid action, so the "
     "chalky deposits from hard water are untouched. That is vinegar's job.",

     "Handling: buy the standard 3% first-aid strength and keep it in its "
     "original opaque bottle, because light degrades it. Decanted into a clear "
     "spray bottle it becomes weak water within a couple of weeks. If you want "
     "to spray it, buy a spray cap that fits the original bottle.",

     "Never combine with vinegar in one application — they neutralise each "
     "other. Used in sequence with a flush between, they complement each other "
     "well. It can lighten some fabrics, so keep it off coloured textiles.",
   ],
   "tip": "Bubbling on contact tells you it is still active and that it has "
          "found organic material. A bottle that no longer fizzes on anything "
          "has expired.",
   "saves": "About $15 a year covers a bathroom that previously ran $80 to $120 "
            "in bowl products.",
  },
  {
   "kicker": "PLAYBOOK · ALKALI",
   "title": "Washing Soda Versus Baking Soda",
   "hook": "They sit side by side, look identical, and are constantly "
           "substituted for each other. They are not interchangeable.",
   "fix": [
     "Baking soda, sodium bicarbonate, pH around 8.3, roughly $1.50 a box. "
     "Mildly alkaline and gentle. The right choice for neutralising uric acid in "
     "grout and caulk, for deodorising, and for anywhere a gentle abrasive helps "
     "without risking the surface.",

     "Washing soda, sodium carbonate, pH around 11.4, roughly $4 a box. "
     "Aggressively alkaline. The right choice for the tank soak, for greasy "
     "floor grout, and for heavy soil. Because the pH scale is logarithmic, the "
     "difference in strength between them is around a thousandfold.",

     "Use the gentle one where contact with surfaces is prolonged or the surface "
     "is delicate. Use the strong one where you need deposits broken down in "
     "thirty minutes and you will rinse afterwards.",

     "Neither belongs on natural stone. Both are fine on porcelain, glazed tile, "
     "and cement grout. Gloves for washing soda as a matter of routine.",
   ],
   "tip": "Check the label rather than the front of the box. Brand names in this "
          "aisle are unhelpfully similar and the two products are shelved "
          "together deliberately.",
   "saves": "One $4 box of washing soda covers most of a year of monthly tank "
            "treatments.",
  },
  {
   "kicker": "PLAYBOOK · ACID",
   "title": "White Vinegar",
   "hook": "Genuinely useful and comprehensively over-recommended. It has one "
           "job and does it well.",
   "fix": [
     "Good for: mineral scale, hard-water spotting on glass and chrome, "
     "limescale in kettles and shower heads. Roughly 5% acetic acid, and acid is "
     "what dissolves calcium and magnesium deposits.",

     "Not good for: biofilm, uric acid odour, or grease. Several of the "
     "organisms behind rust-coloured staining tolerate mild acidity perfectly "
     "well. Most disappointment with vinegar comes from using it on a biological "
     "problem rather than a mineral one.",

     "Never on natural stone. Marble, limestone, and travertine are "
     "calcium-based, which means acid does not clean them — it dissolves them, "
     "leaving permanent dull etching.",

     "Never with bleach, which produces chlorine gas. Never with hydrogen "
     "peroxide in the same application, which simply wastes both.",
   ],
   "tip": "Contact time beats concentration. A vinegar-soaked cloth laid against "
          "a deposit for twenty minutes achieves far more than repeated "
          "spraying, which mostly runs off before it can act.",
   "saves": "Under 50 cents a treatment against $7 to $12 for a proprietary "
            "limescale product.",
  },
  {
   "kicker": "PLAYBOOK · SURFACTANT",
   "title": "Dish Soap, One Drop",
   "hook": "Rarely the active ingredient, frequently the reason the active "
           "ingredient reaches what it is supposed to reach.",
   "fix": [
     "Dish soap is a surfactant: it lowers water's surface tension. Water on its "
     "own beads on top of grout and fabric rather than sinking in. Add one drop "
     "and the same solution wicks down into the pores where the actual problem "
     "is.",

     "This is why the baking soda solution in Part IV specifies a drop of soap. "
     "The soap is not doing the neutralising. It is delivering the compound that "
     "does.",

     "One drop per 500 ml genuinely means one drop. More produces foam that has "
     "to be rinsed out, and residual soap in carpet or grout attracts soil, "
     "which leaves the area dirtier a month later than when you started.",

     "It also works alone on fresh grease before it sets, for the same reason it "
     "works on pans — grease is exactly what it was designed to lift.",
   ],
   "tip": "Use plain dish soap, not one with added bleach, hand moisturiser, or "
          "heavy fragrance. You want the surfactant and nothing else along for "
          "the ride.",
   "saves": "Effectively free, and it is often the difference between a method "
            "working and appearing not to.",
  },
  {
   "kicker": "PLAYBOOK · BARRIER",
   "title": "Mineral Oil",
   "hook": "The only entry here that is not a cleaner. It does not remove "
           "anything — it changes what the surface will accept next.",
   "fix": [
     "Plain baby oil is refined mineral oil: inert, odourless, and it does not "
     "react with water or feed bacteria. Its value is that it fills the "
     "microscopic pits in porcelain that biofilm needs in order to anchor.",

     "Only ever apply it to a genuinely clean surface. Over an existing ring it "
     "seals the problem in. Clean first, seal second, without exception.",

     "Keep it inside the bowl. Oil on a bathroom floor is a serious slip hazard, "
     "and oil on a seat is unpleasant for everyone. A thin film on the interior "
     "surfaces is the entire application.",

     "Use the plain version. Scented, aloe, and 'moisturising' variants contain "
     "organic additives, which is precisely the material you are trying to stop "
     "providing.",
   ],
   "tip": "Do not pour it into the bowl. A teaspoon on a cloth, wiped on, is "
          "the method. Pouring puts oil into the drain, which is neither useful "
          "nor good practice.",
   "saves": "A $3 bottle covers one toilet for around six months of monthly "
            "re-coating.",
  },
 ],
},
]

# ----------------------------------------------------------------------------
# REFERENCE SECTIONS
# ----------------------------------------------------------------------------

TROUBLESHOOTING = [
    ("Ring returns within a week", "Biofilm, not removed at anchor",
     "Peroxide reset, then weekly pour"),
    ("Ring is pale, chalky, gritty", "Mineral scale from hard water",
     "Undiluted vinegar soak, several hours"),
    ("Smell returns after cleaning", "Uric acid in grout and caulk",
     "Alkaline solution, 30+ min contact"),
    ("Smell worst after no use", "Failing wax ring under base",
     "Replace wax ring — not cleanable"),
    ("Needs two flushes", "Scale in rim jet holes",
     "Toothbrush the holes, then tank soak"),
    ("Toilet runs intermittently", "Flapper not sealing",
     "Dye test; replace flapper (~$8)"),
    ("Carpet stain reappears", "Wicking from saturated pad",
     "Foam method, blot only, repeat"),
    ("Stain spread while cleaning", "Rubbing instead of blotting",
     "Press and lift, outside inward"),
    ("Cloudy shower screen", "Hard water mineral film",
     "Vinegar contact 15 min, then squeegee"),
    ("Grout grey and greasy", "Ground-in soil, not odour",
     "Washing soda solution, stiff brush"),
    ("Vinegar 'did nothing'", "Used on biological problem",
     "Match acid to scale, alkali to odour"),
    ("Baking soda 'did nothing'", "Dry powder, too little time",
     "Solution + surfactant, 30+ min"),
]

MISTAKES = [
    "Mixing bleach with vinegar, ammonia, or any acid. This produces toxic gas "
    "in a small room. There is no safe small amount.",
    "Scrubbing a toilet ring harder instead of changing the chemistry. The "
    "colony you cannot see is the one that brings it back.",
    "Treating the bowl for a smell that lives in the grout. Porcelain is "
    "non-porous; odour does not reside in it.",
    "Combining baking soda and vinegar for cleaning. The fizz is the two "
    "cancelling each other out before reaching the surface.",
    "Rubbing a carpet stain. It spreads the mark, drives it into the pad, and "
    "distorts the pile permanently.",
    "Flooding carpet with cleaner. Saturating the backing is what causes the "
    "stain to wick back days later.",
    "Applying baby oil over an existing ring. That seals the problem in rather "
    "than preventing the next one.",
    "Leaving in-tank tablets permanently. Continuous chemical contact hardens "
    "the flapper and can void warranty cover.",
    "Using acid on natural stone. Marble, limestone, and travertine are "
    "calcium-based and will etch permanently.",
    "Not allowing contact time. Nearly every method here fails at five minutes "
    "and works at thirty.",
]

MYTHS = [
    ("Bleach is the strongest option, so it must be the best.",
     "Bleach is a disinfectant. It kills bacteria but leaves uric acid crystals "
     "and mineral scale entirely intact — which is why a bleached bathroom can "
     "smell again within hours."),
    ("Baking soda and vinegar together make a powerful cleaner.",
     "They neutralise each other. Used separately they do two different and "
     "genuinely useful jobs; combined they mostly produce salty water."),
    ("A stronger product will finally fix the recurring ring.",
     "Strength is not the constraint. Contact time and reaching the anchored "
     "layer are. A dollar of peroxide left for an hour beats a $9 spray given "
     "thirty seconds."),
    ("Hard water stains and toilet rings are the same problem.",
     "One is mineral and needs acid. The other is biological and needs an "
     "oxidiser. Treating both the same way is why one of them never clears."),
    ("If a natural method were any good, it would be sold commercially.",
     "Commodity substances cannot be patented or branded, and something you buy "
     "twice a year is a poor business model. That is an economic fact, not "
     "evidence about whether it works."),
    ("A clean-looking toilet is a clean toilet.",
     "The jet holes under the rim are invisible without a torch and are almost "
     "never cleaned. They are usually the worst surface in the room."),
]

SAVINGS_TABLE = [
    ("Toilet bowl cleaner", "$80 – $120", "Peroxide", "~$15", "$65 – $105"),
    ("In-tank tablets", "$60 – $90", "Washing soda", "~$11", "$49 – $79"),
    ("Bathroom odour spray", "$60 – $110", "Baking soda", "~$6", "$54 – $104"),
    ("Carpet stain remover", "$40 – $80", "Shaving foam", "~$8", "$32 – $72"),
    ("Limescale spray", "$25 – $45", "White vinegar", "~$5", "$20 – $40"),
    ("Grout cleaner", "$20 – $40", "Washing soda", "~$4", "$16 – $36"),
]

CHECKLIST_WEEKLY = [
    "Pour 120 ml of 3% hydrogen peroxide into each toilet bowl",
    "Squeegee the shower screen after the last shower",
    "Wipe the floor behind and beside the toilet base",
    "Wipe the seat hinge points and the back of the tank",
    "Check the toilet is not running between flushes",
]

CHECKLIST_MONTHLY = [
    "Washing soda tank soak: one scoop, 30 minutes, two flushes",
    "Re-coat the bowl interior with a teaspoon of baby oil",
    "Toothbrush the rim jet holes and check flush strength",
    "Alkaline treatment on floor grout and the caulk bead",
    "Inspect the flapper for stiffness, cracking, or chalkiness",
    "Check for any movement or rocking in the toilet base",
]

CHECKLIST_SHOPPING = [
    ("3% hydrogen peroxide", "Pharmacy / supermarket", "~$1.10"),
    ("Washing soda (sodium carbonate)", "Laundry aisle", "~$4.00"),
    ("Baking soda (sodium bicarbonate)", "Baking aisle", "~$1.50"),
    ("White vinegar", "Supermarket", "~$2.00"),
    ("Plain baby oil", "Pharmacy / baby aisle", "~$3.00"),
    ("Plain white shaving foam", "Shaving aisle", "~$2.00"),
    ("Plain dish soap", "Supermarket", "~$2.00"),
    ("Penetrating grout sealer", "Hardware store", "~$15.00"),
]

TOOLKIT = [
    "An old toothbrush, kept solely for rim jet holes",
    "A stiff narrow brush for grout lines",
    "White cotton cloths or cut-up white towels — never coloured",
    "A squeegee for glass and screens",
    "Rubber gloves for anything alkaline",
    "A spray bottle for vinegar (never for peroxide)",
    "A phone torch, for looking under the rim and across floors",
    "A measuring spoon kept with the cleaning supplies",
]

SEASONS = [
    ("SPRING", ["Deep-clean and neutralise all floor grout",
                "Re-seal grout if water no longer beads",
                "Full jet-hole clean on every toilet"]),
    ("SUMMER", ["Watch for humidity-driven odour returning",
                "Check wax ring seal if smell persists",
                "Increase screen squeegee habit"]),
    ("AUTUMN", ["Inspect and replace ageing flappers",
                "Descale shower heads and taps",
                "Full carpet check before doors close for winter"]),
    ("WINTER", ["Ventilate during and after cleaning",
                "Watch for condensation-driven mildew",
                "Maintain weekly peroxide pour without fail"]),
]

FINAL_WORD = [
    "Almost nothing in this book is difficult. The methods are short, the "
    "ingredients cost about a dollar, and none of it requires a skill you do "
    "not already have.",

    "What it does require is a change in how you think about the problem. Stop "
    "treating what you can see. Ask what is underneath it, whether the surface "
    "absorbs, and whether you are matching acid to mineral and alkali to odour. "
    "Get that right and the correct method is usually obvious.",

    "The other half is contact time. Nearly every failure in household cleaning "
    "is a good method given thirty seconds when it needed thirty minutes. Pour "
    "it, leave it, walk away. The waiting is the work.",

    "Do the weekly pour and the monthly soak, and within two months the "
    "recurring problems in your bathroom stop being recurring. That is the "
    "whole promise of this book, and it costs about fifteen dollars a year.",
]

DISCLAIMER = [
    "This book is educational content covering common household cleaning "
    "methods. It is not professional plumbing, medical, or safety advice.",

    "Always test any method on a small hidden area before treating a full "
    "surface. Materials vary considerably between homes, and grout, natural "
    "stone, vinyl, and carpet in particular differ in how they respond.",

    "Never mix cleaning products that are not explicitly listed together here. "
    "Combining bleach with acids or with ammonia produces toxic gas. Every "
    "method in this book uses a single substance at a time.",

    "Where a task involves lifting a toilet, working on a supply line, or any "
    "other plumbing work you are not confident undertaking, engage a qualified "
    "plumber. Cost figures are estimates for general guidance and vary by "
    "region and retailer. Individual results vary.",
]
