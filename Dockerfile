FROM ruby:2.6.3
RUN apt-get update && apt-get install default-libmysqlclient-dev default-mysql-client python3 python3-pip -y
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - 
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN apt-get update && apt-get install -y nodejs yarn 
RUN python3 -m pip install Faker
RUN pip3 install pymysql
RUN mkdir /app

ENV HOME /root

WORKDIR /app
COPY Gemfile Gemfile.lock ./
RUN bundle install

COPY . .

EXPOSE 3000

ENTRYPOINT ["sh", "./config/docker/startup.sh"]

CMD ["rails", "server", "-b", "0.0.0.0"]
