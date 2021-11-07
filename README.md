<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Yoshi275/ism-youtube-scraper">
    <img src="https://cdn.analyticsvidhya.com/wp-content/uploads/2019/05/youtube-data-scraping.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Independent Study Module</h3>

  <p align="center">
    An attempt to understand YouTube collaborations.
    <br />
    <a href="https://github.com/Yoshi275/ism-youtube-scraper"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Yoshi275/ism-youtube-scraper">View Demo</a>
    ·
    <a href="https://github.com/Yoshi275/ism-youtube-scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/Yoshi275/ism-youtube-scraper/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

### Built With

* [Python](https://python.org/)
* [Scikit](https://scikit-learn.org/)
* [Pandas](https://pandas.pydata.org/)
* [YouTube Data API v3](https://developers.google.com/youtube/v3)

<p align="right">(<a href="#top">back to top</a>)</p>

### Modules

* YouTube API Scraper (./youtube_api_scrapper)
* Entity Recognition Model (./collab_labelling/entity_recognition)
* Machine Learning Modelling (./collab_labelling/machine_learning)

<!-- GETTING STARTED -->
## Getting Started
### Installation

1. Get a free API Key for YouTube Data API v3
2. Clone the repo
   ```sh
   git clone https://github.com/Yoshi275/ism-youtube-scraper.git
   ```
3. Install Python packages in a virtualenv
   ```sh
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. Enter your API in a new file at `.\youtube_api_scrapper\.env`
   ```js
   const DEVELOPER_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage of YouTube Scraper

1.  Enter the `youtube_api_scrapper` folder
2.  Run `python <FILE_NAME.py>` with the following files:
    * `channel_info_table_populator.py` - gives channel information based on channel ID or username
    * `video_info_table_populator.py` - gives video information based on video ID
    * `channels_to_ids.py` - converts channel usernames into unique YouTube channel IDs
    * `id_to_uploads_playlist.py` - gets all videos from specified channel ID
    

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
<!-- ## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

Your Name - [@icherylcode](https://twitter.com/icherylcode) - cheryl.nqj@gmail.com.com

Project Link: [https://github.com/Yoshi275/ism-youtube-scraper](https://github.com/Yoshi275/ism-youtube-scraper)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Project Partner - [Shauna Tan](https://www.linkedin.com/in/s-tanhs/)
* Supervisor - [Dr Kokil Jaidka](https://profile.nus.edu.sg/fass/cnmkj/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png