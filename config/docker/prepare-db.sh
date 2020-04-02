#!/bin/sh

# If the database exists, migrate. Otherwise setup (create and migrate)
bundle exec rake db:migrate 2>/dev/null || bundle exec rake db:create db:migrate
echo "Done!"

# Clear any data in those two tables 
python3 ./config/docker/refresh_db.py

# Install the simulated user and credit card data
echo "Starting to insert simulated users"
python3 ./config/docker/gen_users.py
echo "Starting to insert simulated credit card data"
python3 ./config/docker/gen_creditdata.py
echo "Finished inserting simulated user and credit card data"
