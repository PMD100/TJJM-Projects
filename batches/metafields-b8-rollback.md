# metafieldsSet rollback — 13 Aug 2026

Values as they were **immediately before** the post-batch-7 metafield fix. Namespace `global`,
type `single_line_text_field`. To roll back, set these exact strings.

Nine pages touched. `title_tag` changed on six (count drift); `description_tag` changed on
nine (six counts + four dead city names).

---

## TN — `gid://shopify/Page/121184223404` (count 34 → 52)

- title_tag: `BJJ Schools in Tennessee | 34 Jiu Jitsu Gyms & Academies`
- description_tag: `Find Brazilian Jiu Jitsu schools in Tennessee. 34 BJJ gyms and academies including Knoxville, Nashville and Cookeville. Free directory from The Jiu Jitsu Mindset.`

## NS — `gid://shopify/Page/121183830188` (count 23 → 29)

- title_tag: `BJJ Schools in Nova Scotia | 23 Gyms & Academies`
- description_tag: `Find Brazilian Jiu Jitsu schools in Nova Scotia. 23 BJJ gyms and academies including Halifax, Dartmouth and Sydney. Free directory from The Jiu Jitsu Mindset.`

## AK — `gid://shopify/Page/121182585004` (count 22 → 14, Wasilla → Juneau)

- title_tag: `BJJ Schools in Alaska | 22 Jiu Jitsu Gyms & Academies`
- description_tag: `Find Brazilian Jiu Jitsu schools in Alaska. 22 BJJ gyms and academies including Anchorage, Fairbanks and Wasilla. Free directory from The Jiu Jitsu Mindset.`

## NL — `gid://shopify/Page/121183699116` (count 15 → 13)

- title_tag: `BJJ Schools in Newfoundland and Labrador | 15 Gyms`
- description_tag: `Find Brazilian Jiu Jitsu schools in Newfoundland and Labrador. 15 BJJ gyms and academies including St. John's, Corner Brook and Paradise. Free directory from The Jiu Jitsu Mindset.`

## DE — `gid://shopify/Page/121182814380` (count 7 → 8)

- title_tag: `BJJ Schools in Delaware | 7 Jiu Jitsu Gyms & Academies`
- description_tag: `Find Brazilian Jiu Jitsu schools in Delaware. 7 BJJ gyms and academies including Wilmington, Dover and Middletown. Free directory from The Jiu Jitsu Mindset.`

## DC — `gid://shopify/Page/121184420012` (count 7 → 6)

- title_tag: `BJJ Schools in Washington DC | 7 Gyms & Academies`
- description_tag: `Find Brazilian Jiu Jitsu schools in Washington DC. 7 BJJ gyms and academies across the District. Free directory from The Jiu Jitsu Mindset.`

---

## Description-only changes — count was already correct, city name was dead

## CT — `gid://shopify/Page/121182781612` (New Haven → Norwalk)

- title_tag: **unchanged**
- description_tag: `Find Brazilian Jiu Jitsu in Connecticut. 85 BJJ gyms and academies across 47 cities, from Stamford and Bridgeport to Hartford and New Haven. Every school listed free.`

## GA — `gid://shopify/Page/121182879916` (Columbus → Lawrenceville)

- title_tag: **unchanged**
- description_tag: `Every Brazilian Jiu Jitsu school in Georgia: 152 BJJ gyms and academies across 78 cities, including Atlanta, Savannah, Marietta, Augusta, Alpharetta and Columbus. Addresses, websites and free listings.`

## NJ — `gid://shopify/Page/121183600812` (Cherry Hill → Toms River)

- title_tag: **unchanged**
- description_tag: `Find Brazilian Jiu Jitsu schools in New Jersey. 210 BJJ gyms and academies across 137 towns including Newark, Jersey City, Hoboken and Cherry Hill. Free directory from The Jiu Jitsu Mindset.`

---

## Deliberately NOT changed

**NY** `gid://shopify/Page/121183666348` names "New York City", which is not a literal city
value in the corpus — those 40 records are filed as `New York`, alongside Brooklyn (23),
Queens (20), Bronx (6) and Staten Island (6). This is colloquially correct, matches search
intent, and the count (182) is right. Left alone on purpose.

## Replacement city rationale — all verified against the live corpus

| region | removed | live records | replacement | live records |
|---|---|---|---|---|
| AK | Wasilla | 0 (2 stored, both suppressed) | Juneau | 1 |
| CT | New Haven | 0 (1 stored, suppressed) | Norwalk | 5 — joint-largest in CT |
| GA | Columbus | 0 (1 stored, suppressed) | Lawrenceville | 6 |
| NJ | Cherry Hill | 0 (never in corpus) | Toms River | 5 |

Only the count and the dead city name were altered. No other hand-written SEO copy was
rewritten — per the precedent set in `ny-step5-verdicts.md` step 10, changing more than the
count is the larger risk.
