[![The project has reached a stable, usable state but is no longer being actively developed; support/maintenance will be provided as time allows](https://www.repostatus.org/badges/latest/inactive.svg)](https://www.repostatus.org/#inactive)

### About
ssTweet is a command line tool to screenshot all the tweets in a thread and upload them to a seperate album in your google photos account.

### To do
- [x] Write a quick python module to prove the concept if everything works as expected. hard code most of the things.
- [x] Write a python module to give url and generate screenshot to local machine.
- [x] Write a python module to upload an image to Google Photos from a locally stored image.
- [x] Mix up the two modules to generate & upload in one go.
- [ ] Improve the code quality, darling.
    - [x] Log every step into a log file as the code runs using the log module.
    - [x] Classes for Albums, Users, Photos, Tweet Authors.
    - [ ] Add unit tests.
- [ ] Solve the issue for authenticating account every time by uploading a photo using `refresh_tokens`
- [x] Get the `url_list` of every tweet in a thread from the URL of first tweet.
- [x] Generate screenshot of every tweet in a thread and upload to Photos.
- [ ] Directly write the image to Google Photos instead of saving & uploading to save up on space.
- [ ] Verify the ssTweet app with Google Photos to avoid unsafe error.
- [x] Instead of a tweet, make a `cli` tool first with a local DB.
- [ ] Work on a simple website where users could connect their twitter and Google Photos account
- [ ] Design the database needed to store the Photos `authentication_token` in encrypted format from Photos app and map them with Twitter usernames.
- [ ] Convert the library to a twitter bot
- [ ] Unroll the contents of the entire thread and upload a single screenshot with text of entire thread.


### Set Up

Install all dependencies from `requirements.txt` (preferably in a virtualenv)

head over to [developer.twitter](https://developer.twitter.com/en), create a sample app and get tokens for it and populate the same in `src/twitter.keys.py`

do the same by [google.photos.developers](https://developers.google.com/photos), create an app and get tokens for it and populate the same in `src/gphotos_keys.json`

edit the url, album_title in `src/main.py` & run it.