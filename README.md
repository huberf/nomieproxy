# Nomie API Proxy
Proxy requests to the API through Nomie with name substitution.

## Setup
* Whether using Heroku or a personal server, you will need to create two
  environement variables (NOMIE_API_KEY and PROXY_KEY). NOMIE_API_KEY should
  equal your Nomie Pro device key, and the PROXY_KEY is a variable that helps
  prevent random people from using the proxy to log items without your consent.
* To deploy to Heroku, simply type `heroku create` followed by `git push heroku
  master`. Your proxy is now live.

## Use
* POST/GET `/<PROXY_KEY>/<TRACKER_NAME>` or `<PROXY_KEY>/<TRACKER_NAME>/<VALUE>` - Logs
  an event with the specified value or if no value is supplied will log it
  without providing a value to the Nomie API
* POST/GET `/note/<PROXY_KEY>/<TEXT>` - This will log the text provided as a note. You
  can use URL encoding to include more complicated text additions.
