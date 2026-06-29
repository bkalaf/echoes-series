# Locales Concept-Art Intake

This folder stores the parsing architecture for city / locale concept art.

## Folder Contract

```text
locales/
  images/   # source concept art + same-basename JSON sidecars; usually a local symlink
  parsed/   # parsed city-locale JSON output created from images + sidecars
  schemas/  # schemas for parsed locale files and image sidecars
```

`/locales/images` is treated as the source image folder during parsing, even when it is a local symlink to another repository.

---

# Image + Sidecar Rule

Consume concept art from `/locales/images`.

For every image, find the same-basename JSON sidecar.

Example:

```text
AQM-HERO-NW-v001.png
AQM-HERO-NW-v001.json
```

The JSON sidecar defines the intended metadata for that image, including:

- intended camera;
- view type;
- visible sections;
- canonical anchors;
- prompt version;
- prompt hash;
- named landmark roles.

Use the sidecar as intended metadata.

Then parse the actual image and record visual deviations separately.

Do **not** overwrite the sidecar’s intended anchors based on image interpretation.

## Parse Authority Order

1. Sidecar JSON = intended metadata authority.
2. Actual image = visual observation source.
3. Parsed locale JSON = synthesis surface that records both intended metadata and deviations.

If the image shows something different from the sidecar, keep the sidecar intent and add the difference to `visualDeviations` or equivalent notes.

---

# Naming Pattern

Use this basename pattern for images and sidecars:

```text
{CITY_CODE}-{VIEW_CODE}-v{NNN}.{ext}
{CITY_CODE}-{VIEW_CODE}-v{NNN}.json
```

Examples:

```text
AQM-HERO-NW-v001.png
AQM-HERO-NW-v001.json
LUM-STREET-TALLOW-v002.png
LUM-STREET-TALLOW-v002.json
NVR-PALACE-APPROACH-v001.png
NVR-PALACE-APPROACH-v001.json
```

The city code is three uppercase letters. The view code is uppercase hyphenated text. The version is lowercase `v` plus three digits.

---

# Local Symlink Setup

The concept-art images may live in another repository. In that case, link that repository’s image folder into this repository at `locales/images`.

## macOS / Linux / WSL

From the root of `echoes-series`:

```bash
# Replace this with the real path to the other repository's locale image folder.
TARGET="../<concept-art-repo>/locales/images"

# The repository ignores /locales/images, so this is a local working-copy setup.
rm -rf locales/images
ln -s "$TARGET" locales/images

# Verify the link.
ls -la locales/images
```

## Windows PowerShell

From the root of `echoes-series`:

```powershell
# Replace this with the real path to the other repository's locale image folder.
$Target = "..\<concept-art-repo>\locales\images"

# The repository ignores /locales/images, so this is a local working-copy setup.
Remove-Item -Recurse -Force .\locales\images -ErrorAction SilentlyContinue
New-Item -ItemType SymbolicLink -Path .\locales\images -Target $Target

# Verify the link.
Get-ChildItem .\locales\images
```

Use a directory junction instead if local Windows permissions block symbolic links:

```powershell
cmd /c mklink /J locales\images ..\<concept-art-repo>\locales\images
```

## Git rule

Do not commit generated concept-art images or the local symlink into this repository unless intentionally changing source ownership.

This repository should track:

- schemas;
- parsed JSON outputs;
- documentation;
- canon references.

The source concept-art image folder can remain owned by the other repository.

---

# Parsing Output

Parsed city-locale files should be written to:

```text
/locales/parsed/{CITY_CODE}.locale.json
```

Example:

```text
/locales/parsed/AQM.locale.json
```

Each parsed locale file should aggregate all source views for that city, preserve the intended metadata from each image sidecar, and record visual deviations separately.

---

# Schemas

- `schemas/locale.schema.json` — parsed aggregate city-locale output.
- `schemas/image-sidecar.schema.json` — intended metadata sidecar living next to each image.
