[![The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

### About
ssTweet is a command line tool to screenshot all the tweets in a thread and upload them to a seperate album in your google photos account.

### To do
- [x] Write a quick python module to prove the concept if everything works as expected. hard code most of the things.
- [x] Write a python module to give url and generate screenshot to local machine.
- [x] Write a python module to upload an image to Google Photos from a locally stored image.
- [x] Mix up the two modules to generate & upload in one go.
- [x] Get the `url_list` of every tweet in a thread from the URL of first tweet.
- [x] Generate screenshot of every tweet in a thread and upload to Photos.
-------
in priority:
- [ ] Move from tweepy to latest Twitter official API and write the search through algorithm myself to make it faster and more reliable (learn how thread reader apps do it) under `fetch_thread.py`
- [ ] Solve the issue for authenticating account every time by uploading a photo using `refresh_tokens`
- [ ] Verify the ssTweet app with Google Photos to avoid unsafe error.
- [ ] Work on a simple website where users could connect their twitter and Google Photos account
- [ ] Design the database needed to store the Photos `authentication_token` in encrypted format from Photos app and map them with Twitter usernames.
- [ ] Unroll the contents of the entire thread and upload a single screenshot with text of entire thread.


### Set Up
- [x] activate a virtualenv named env & install all dependencies from `requirements.txt`
- [x] remove `sample_` from the filnames of `sample_twitter_keys.py` and `sample_gphotos_keys.json`
- [x] head over to [developer.twitter](https://developer.twitter.com/en), create a sample app and get tokens for it and populate the same in `src/twitter.keys.py`
- [x] do the same on [google.photos.developers](https://developers.google.com/photos), create an app and get tokens for it and populate the same in `src/gphotos_keys.json`
- [x] edit the url, album_title in `src/main.py` & run it.
