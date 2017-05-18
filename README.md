# Nomie API Proxy
Proxy requests to the API through Nomie with name substitution.

## Setup
* Whether using Heroku or a personal server, you will need to create two
  environement variables (NOMIE_API_KEY and PROXY_KEY). NOMIE_API_KEY should
  equal your Nomie Pro device key, and the PROXY_KEY is a variable that helps
  prevent random people from using the proxy to log items without your consent.
* To deploy to Heroku, simply type `heroku create` followed by `git push heroku
  master`. Your proxy is now live.
