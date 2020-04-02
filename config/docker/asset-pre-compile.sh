#!/bin/sh

# Precompile assets for production
bundle exec rake assets:precompile
echo "Assets Pre-compiled!"

bundle exec rake webpacker:compile
echo "Ran Webpacker Compile!"
