# Batch 7 browser-render pass — companion notes

Scope: 30 held-back targets rendered via Claude in Chrome (the prompt said "33 rows"; the actual
target table contained 30 — all 30 were processed). One tab was reused throughout and closed at
the end. Worked sequentially, region priority NS → TN → rest, as instructed.

## What the browser could read that plain fetch could not

This is the main methodological finding, worth recording precisely for future batches:

- **Facebook and Instagram business pages render a usable public preview without login** for the
  overwhelming majority of targets — name/handle, category, bio/"About" text, street address, and
  (for FB) a "Details" block with phone/hours. This was true even for pages with zero reviews and
  under 500 followers. In this batch, roughly **20 of 30** targets were only resolvable this way;
  plain fetch would have returned an empty body for all of them.
- **The failure mode is not uniform.** Three distinct patterns showed up, and they mean different
  things:
  1. **"This content isn't available right now"** (Samson Martial Arts & Fitness, Kingsport BJJ's
     FB, Loyalty BJJ's FB, Alaska Samurai Arts' FB) — genuinely inaccessible to this session, not a
     login prompt. Tried the numeric page ID, `?locale=` variants, `profile.php?id=`, and the
     `m.facebook.com` mirror for one case (Samson) — all five URL forms returned the same message.
     This is **not** the same as a login wall and should not be coded as one; it behaves more like
     a dead or restricted page. Recorded as UNVERIFIED, not UNVERIFIED-LOGIN-WALL.
  2. **A genuine login/membership wall** — only one case fired this cleanly: the Facebook **group**
     (not page) for Dragon Martial Arts Colchester. The group's shell (name, member count, "Public
     group" label, creation date) rendered with no login prompt, but the actual post feed,
     Discussion tab, and Media tab all came back empty even though the group is marked "Public" —
     Facebook gates group *content* behind membership regardless of the group's visibility setting.
     This is the case the task brief anticipated ("cookie/login overlay with no content behind
     it") and it is coded UNVERIFIED-LOGIN-WALL.
  3. **Truncated-by-design bio text** — Foley's Martial Arts - Paradise's own FB bio literally ends
     mid-sentence ("Providing we") with no "See more" control present in the DOM. This is not a
     tool failure; it is how the business wrote the field. Worth distinguishing from case 1/2
     because re-fetching or waiting does not fix it.
- **Regular small-business websites failed almost as often as social pages, but for a different,
  very legible reason: expired/parked domains, not JS-rendering problems.** `chattanoogabjj.com`,
  `murfreesborobjj.com`, and `tribalbjj.com` (the last for a *different* Ohio... actually
  Oklahoma business) all resolve to the identical GoDaddy "This domain is registered, but may
  still be available" template, reachable at a literal `/lander` path. `kingsportbjj.com` resolves
  in DNS but serves a near-blank page with only a `consentmanager.net` cookie-warning icon and
  hidden honeypot fields — a parking-service signature. `alaskasamuraiarts.com` is a Namecheap
  domain-auction page. `parisgraciejiujitsuacademy.com` returns an unconfigured default vhost.
  `manimalathletics.com` and `foleysmartialarts.ca` both error out entirely. None of these needed
  JavaScript execution to diagnose — a plain fetch tool that returned *any* body text would have
  caught all of them; the reason the plain-fetch pass logged these as blank/empty is more likely
  that the tool treated a non-200 or template response as no-content rather than that the pages
  are JS-only. **Recommendation for future batches: a fetch tool that surfaces status codes and
  final redirected URL would resolve most of these without a browser at all** — the browser was
  essential for Facebook/Instagram, much less so for the plain domains, where its main value was
  letting a human-style read confirm "yes, this is really a parking page" via screenshot rather
  than guessing from a title tag.
- **DNS-first screening remained useful and cheap alongside the browser.** `alliancetnbjj.com`
  returned NXDOMAIN (Status 3) — conclusive, and it explains why the plain-fetch pass saw nothing;
  the business turned out to be very much alive under a different discoverable channel (its own
  Facebook page, which still links back to the dead domain). This is the clearest illustration in
  the batch of the rule that a dead URL doesn't mean a dead school.

## Marmac Athletics vs. Porters Lake — resolved

These are confirmed to be **two unrelated businesses**, as suspected:

- **Marmac Athletics** trades under that name alone. Its own Facebook page reads: "Recreational
  Kickboxing - Brazilian Jiu Jitsu - Qualified Professional Coaching..." at 36 Inglis Street,
  **Truro**, NS.
- The Porters Lake business's Facebook page (`facebook.com/averageday`) gives its own display name
  and handle as **"Porters Lake Brazilian Jiujitsu" / `porterslakebjj`** — nowhere does the page
  say "Mountain Jiu-Jitsu." That settles the naming ambiguity flagged in the addendum: the correct
  trade name is Porters Lake Brazilian Jiujitsu, not Mountain Jiu-Jitsu. Its address field reads
  only "5775 trunk 7" with no separate city string, consistent with Porters Lake being folded into
  the name itself.

## The two military-base decisions

Both **12 Wing Brazilian Jiu-Jitsu** (CFB Shearwater / Eastern Passage) and **Hero Grappling Club**
(CFB Halifax) are **DROP**, on the same basis: neither page, nor the fallback newspaper article for
12 Wing, states that civilians without base access can train there.

- 12 Wing's Instagram bio is just "Military Grapplers." The fallback Trident Newspaper article is
  from 2019 (now ~7 years stale), describes the club meeting in a base fitness centre, and gives
  only a `forces.gc.ca` contact for a coach who was, per the article, about to be posted elsewhere.
  No public-access statement anywhere.
- Hero Grappling Club's own Facebook page is the most explicit of the two about *not* being public:
  "The military grappling program at CFB Halifax under the PSP Grappling initiative." PSP
  (Personnel Support Programs) is CAF's internal morale/welfare program — the page describes itself
  in terms that assume a base-access audience.

Per the rule that a base club is not a directory listing unless public access is established
explicitly, and neither was, both are DROP.

## Login walls hit

Only one genuine login/membership wall was encountered: the **Dragon Martial Arts Colchester
County** Facebook *group*. See case 2 above. No other target hit a true login wall in the strict
sense — the several "content isn't available" cases behaved differently (see above) and were coded
UNVERIFIED rather than UNVERIFIED-LOGIN-WALL.

## Other notable findings worth flagging explicitly

- **Tribal BJJ is a wrong-region trap, not a Delaware school.** The stored domain and its Facebook
  page both belong to "Tribal Jiu-Jitsu" in **Ardmore, Oklahoma**, corroborated by an independent
  Oklahoma business-filings PDF. No Dover, DE business by that name exists as far as this pass
  could find.
- **A live domain-branding trap in Tennessee:** `johnsoncityjiujitsu.com` markets itself as
  "Tri-Cities Premier Jiu Jitsu Academy" at the top of the page, but its own body text, testimonials,
  and contact block are for a wholly different business — Ashburn Jiu Jitsu, in Ashburn, Virginia.
  Reading only the top of the page (or the title) would have produced a confidently wrong ADD for
  "Tri-Cities BJJ."
- **A same-name-different-province trap in New Brunswick:** the Instagram handle
  `@woodstockbjj.ca` — which looks exactly like what "Woodstock NB BJJ" should be — is actually
  Woodstock, **Ontario** (own bio: "Woodstock Ontario, Canada 🇨🇦," 12 Kent Street). The real
  Woodstock, NB business trades as **B7 Jiu Jitsu** and was found and confirmed separately.
- **Alliance Jiu Jitsu Tennessee is filed under the wrong city.** The record's own Facebook page
  gives its address as Memphis, TN — not Nashville as stored — while confirming it is genuinely
  "Tennessee Affiliate of the Alliance Brazilian Jiu-Jitsu Team."
- **Cheticamp Martial Arts's own site never uses the stored city "Petit Etang"** — it repeatedly
  brands itself "Cheticamp, Nova Scotia." Recommend correcting the city string.
- **Two Alaska "settle them" targets are both confirmed NOT-BJJ, not just unread.** Tonbo Dojo -
  Alaska Samurai Arts is a Nami Ryu Aiki Heiho (Japanese sword arts / Aiki-jujutsu) study group,
  confirmed on the parent organization's own site. Shoshindo of Alaska's own bios never mention
  Brazilian Jiu-Jitsu and independent content referencing "kata" and "bunkai" (karate-specific
  terms not used in BJJ) supports a traditional-karate-family classification instead.

## Rows still UNVERIFIED and why

Kingsport BJJ, Murfreesboro BJJ, Loyalty Brazilian Jiu-Jitsu, Samson Martial Arts & Fitness,
Sprawl or Brawl MMA, and Tri-Cities BJJ remain UNVERIFIED. In every case a first-party page either
would not load at all (dead/parked domain, Facebook "content isn't available," Instagram "page
isn't available") or, where real BJJ schools clearly exist nearby/under a related name, I could not
pin down with confidence that they are the *same* entity as the stored record without risking a
wrong ADD or a duplicate-name collision (Murfreesboro in particular, given Gracie Barra's franchise
density). These are flagged rather than guessed.
