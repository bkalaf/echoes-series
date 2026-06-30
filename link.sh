# From the root of echoes-series
TARGET="../eidolon-map-assets-app/locales/images"

# rm -rf locales/images
ln -s "$TARGET" locales/images

# verify
ls -la locales/images
