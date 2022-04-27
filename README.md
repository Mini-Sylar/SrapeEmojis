# Scraping Scripts For [Client Server Chat App](https://github.com/Mini-Sylar/Server-Client-ChatApp)

## Overview
A scrapper built using selenium to extract emojis from EmojiPedia website
currently it scrapes the Google version but can easily be modified to scrape other versions.<br/>
It is currently being used in another project here: [Client Server Chat App](https://github.com/Mini-Sylar/Server-Client-ChatApp) <br>
- Works with Only Chromium Edge (Can easily to adapted to other browsers)

## Usage
<pre>
- Download the <a href="https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/">Chromium Edge Web Driver</a>  
- pip install <a href="./requirements.txt">requirements.txt</a>
- Run any of the scripts
</pre>

## Scrape.py
This opens an emoji, clicks on the copy button on each emoji and places it in *emoji.txt*

## ScrapeEmojiImages
This saves every emoji as a png in a folder called *Emojis* <br/>
samples included in [Emojis](./Emojis)

## Contribution
Any insight is welcome. especially better ways of reading emojis instead of using a txt file

