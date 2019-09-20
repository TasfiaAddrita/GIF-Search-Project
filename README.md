# GIF Search

## Description
Built a GIF search page that uses basic routing to display content by integrating the Tenor API.

## Goals
### Requirements
- [x] The page must use templates
- [x] The page must display GIFs (10 at the most)
- [x] GIFs should appear in a single vertical list
- [x] At the top of the page there should be a page title
- [x] Below the title there should be a search bar with a “Search” button near it (placement up to you, but needs to be on one side of the bar)
- [x] Users should be able to type a string into the search bar, press the search button, and be shown up to 10 GIFs related to the search query
- [x] GIFs should be displayed on a fresh load of the page, i.e. before a query has even been typed.
- [x] GIFs should only update once a user has pressed the “Search” button
- [ ] If no GIFs could be found for the search term, display an error message saying that no GIFs could be found, and to try another search query
- [x] The following elements should have some custom styling (i.e. CSS rules) added to them:
    - Page title
    - Search Bar
    - Search Button
- [x] All code must be commented with a description of what the code is doing, expected input, and expected output

### Stretch Challenges
- [x] Add a gitignore file and edit it so that “.DS_Store” and “.env” won’t get tracked in Git. What else shouldn't be tracked?
- [ ] Center-align everything on the page
- [x] Display the GIFs in a grid instead of a list
- [x] Add a button that displays the top 10 trending GIFs on Tenor
    - Check the documentation!
- [x] Add a button that displays 10 random GIFs on Tenor
    - Check the documentation!
- [x] Type-ahead: as the user types in the search box, the page is reloading the gifs to match the search query in real time (no longer needing to click the search button)


## How to run/setup
Clone or download this repo, go to the directory where the downloaded file is, then type in the terminal
```
python3 app.py
```

## Resources
Bootstrap: https://getbootstrap.com/
Masonry.js: https://masonry.desandro.com
jQuery, AJAX
Stack Overflow
