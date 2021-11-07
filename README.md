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
        <li><a href="#modules">Modules</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage">Usage</a>
      <ul>
        <li><a href="#using-youtube-scraper">Using YouTube Scraper</a></li>
        <li><a href="#using-entity-recognition-model">Using Entity Recognition Model</a></li>
        <li><a href="#using-machine-learning-model">Using Machine Learning Model</a></li>
      </ul>
    </li>
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
5. If using spaCy entity recognition model, download model
    ```sh
    python -m spacy download en_core_web_lg
    ```
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
### Using YouTube Scraper

1.  Enter the `youtube_api_scrapper` folder
2.  Run `python <FILE_NAME.py>` with the following files:
    * `channel_info_table_populator.py` - gives channel information based on channel ID or username
    * `video_info_table_populator.py` - gives video information based on video ID
    * `channels_to_ids.py` - converts channel usernames into unique YouTube channel IDs
    * `id_to_uploads_playlist.py` - gets all videos from specified channel ID

### Using Entity Recognition Model

1.  Enter the `.\collab_labelling\entity_recognition` folder
2.  Ensure that there is a `gservice_account.json` file within the    folder, and an input file named according to the `INPUT_CSV_FILE_NAME` in `entity_recognition_model.py` in the same folder. The default input file name to be read is `test_videos.csv`
3.  In the `entity_recognition_model.py`, change the following variables as relevant:
    *   ENTITY_RECOGNITION_MODEL - options: Model.GOOGLE_MODEL, Model.SPACY_MODEL. This determines the ER model being used
    *   INPUT_CSV_FILE_NAME and OUTPUT_CSV_FILE_NAME - This determines the input and output files. The input file reads the same structure as that of the video data in OneDrive. The output file returns 
    *   SELECTED_COLS - This determines the names of the relevant columns, which has text that you want to run through the ER model. In the background, we simply combine all texts into one to send through the ER model.

### Using Machine Learning Model

1.  Enter the `.\collab_labelling\machine_learning` folder
2.  Run `jupyter notebook` within the folder
3.  Run code on Jupyter notebook environment

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