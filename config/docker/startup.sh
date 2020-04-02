#!/bin/sh

# Wait for DB services
#bash ./config/docker/wait-for-services.sh

# Prepare DB (Migrate - If not? Create db & Migrate)
sh ./config/docker/prepare-db.sh

# Pre-comple app assets
sh ./config/docker/asset-pre-compile.sh

# Start Application
bundle exec puma -C config/puma.rb
