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
AQM-HERO-NW-v004.png
AQM-HERO-NW-v004.json
```

The JSON sidecar defines the intended metadata for that image, including:

- schema version;
- city code / city name;
- view code;
- version number;
- image path;
- metadata path;
- prompt record key;
- prompt version;
- prompt source hash;
- generated timestamp;
- intended camera;
- visible sections;
- canonical anchors;
- consumption notes.

Use the sidecar as intended metadata.

Then parse the actual image and record visual deviations separately.

Do **not** overwrite the sidecar’s intended anchors based on image interpretation.

## Parse Authority Order

1. Sidecar JSON = intended metadata authority.
2. Actual image = visual observation source.
3. Parsed locale JSON = synthesis surface that records both intended metadata and deviations.

If the image shows something different from the sidecar, keep the sidecar intent and add the difference to `visualDeviations` or equivalent notes.

---

# Sidecar Shape

The current sidecar schema is flat, not nested.

Example:

```json
{
  "schemaVersion": 1,
  "cityCode": "AQM",
  "cityName": "Aquila Matara",
  "viewCode": "HERO-NW",
  "version": 4,
  "imagePath": "/locales/images/AQM-HERO-NW-v004.png",
  "metadataPath": "/locales/images/AQM-HERO-NW-v004.json",
  "promptRecordKey": "AQM-HERO-NW",
  "promptVersion": 4,
  "promptSourceHash": "4a2d01b9",
  "generatedAt": "2026-06-29T07:36:44.880Z",
  "camera": {
    "viewType": "hero",
    "origin": "northwest",
    "target": "city center / District 13 seat of power",
    "oppositeSide": "southeast"
  },
  "visibleSections": [1, 2],
  "canonicalAnchors": [
    {
      "key": "seatOfPower",
      "assetId": "AQM_CITADEL",
      "name": "Civic Blue Glow Tide-Seal Citadel",
      "type": "CITADEL",
      "role": "dominant central civic anchor / District 13 seat of power",
      "promptDescription": "The intended prompt description for this anchor."
    }
  ],
  "consumptionNotes": [
    "Use this sidecar as intended metadata.",
    "Record visual deviations separately."
  ]
}
```

`canonicalAnchors[].sectionNumber` is optional and should be used when an anchor is tied to a specific visible city section.

---

# Naming Pattern

Use this basename pattern for images and sidecars:

```text
{CITY_CODE}-{VIEW_CODE}-v{NNN}.{ext}
{CITY_CODE}-{VIEW_CODE}-v{NNN}.json
```

Examples:

```text
AQM-HERO-NW-v004.png
AQM-HERO-NW-v004.json
LUM-STREET-TALLOW-v002.png
LUM-STREET-TALLOW-v002.json
NVR-PALACE-APPROACH-v001.png
NVR-PALACE-APPROACH-v001.json
```

The city code is three uppercase letters. The view code is uppercase hyphenated text. The file suffix is lowercase `v` plus three digits. The sidecar’s `version` field is the integer form of that suffix.

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

For each source image record in a parsed locale output, use:

- `schemaVersion` from the sidecar;
- `viewCode` from the sidecar;
- integer `version` from the sidecar;
- `path` from sidecar `imagePath`;
- `metadataPath` from the sidecar;
- prompt lineage fields;
- `metadataAuthority: "sidecar-intended-metadata"`;
- `visualDeviations` as parser observations.

---

# Schemas

- `schemas/locale.schema.json` — parsed aggregate city-locale output.
- `schemas/image-sidecar.schema.json` — intended metadata sidecar living next to each image.
