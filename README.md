# greenhollowapps.github.io

The Green Hollow Apps website, served by GitHub Pages at https://greenhollowapps.github.io/.
Plain static HTML and CSS: no build step, no framework, no trackers.

## Pages

| Path | Page |
|---|---|
| `index.html` | Home: the studio and its apps |
| `intervalworkout/` | IntervalWorkout app page |
| `flickm/` | Flickm app page |
| `support/` | Contact details and FAQs for both apps (`#intervalworkout`, `#flickm`) |
| `privacy/` | Links to each app's privacy policy and terms |
| `404.html` | Not-found page (GitHub Pages serves it automatically) |

The legal documents themselves live in their own repos and keep their URLs, because the store
listings and the apps link to them:

- `intervalworkout-privacy` → https://greenhollowapps.github.io/intervalworkout-privacy/
- `flickm-legal` → https://greenhollowapps.github.io/flickm-legal/

## Files that must stay put

- `app-ads.txt` authorises AdMob to sell ad inventory for IntervalWorkout. It must stay at the
  domain root; AdMob crawls `https://greenhollowapps.github.io/app-ads.txt` because this URL is
  the Play listing's developer website.
- `.nojekyll` serves files as-is.

## Editing

- Styles are in `assets/site.css`. Brand colours come from `GreenHollowApps/brand/README.md`;
  each app page uses its own theme class (`theme-intervalworkout`, `theme-flickm`).
- The header and footer are repeated in every page. Change all of them together.
- When adding a page, add it to `sitemap.xml`.
- The logo (`favicon.svg`, `assets/img/logo.svg`, `apple-touch-icon.png`) is the placeholder
  mark from `GreenHollowApps/brand/logos/`. Replace all three when the final logo is chosen.

## Images

`assets/img/<app>/` holds web-sized copies of each app's store art. To refresh them after the
store screenshots change, check out `IntervalWorkout` and `Flickm` next to this repo and run:

```
python tools/make-images.py
```

## Preview locally

```
python -m http.server 8000
```

Then open http://localhost:8000/.

## When IntervalWorkout goes live

Replace the "Coming soon to Google Play" button in `intervalworkout/index.html` (see the TODO
comment) and the "Coming soon" tag in `index.html` with the store link.
