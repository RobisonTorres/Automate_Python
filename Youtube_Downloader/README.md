# YouTube Downloader

This repository stores a function to download content from Youtube.

## Intro

Sometimes, after finding a great video on YouTube, we want to download at least the audio to our device. However, finding a reliable site or free program to do this can be challenging. The primary goal of these functions is to simplify this process.

## Features 

 - Download video or audio.
 - Download playlist.

## Prerequisites

You must have Python installed in your computer.

## Usage Instructions

To use this repository, follow these steps:

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/RobisonTorres/Automate_Python.git

2. Install the library pytube.

   ```bash
   pip install pytube

3. Navigate to the directory:

   ```bash
   cd Automate_Python/Youtube_Downloader

4. Choose a option:

    * To download video or audio execute the main.py:
    ```bash
   python main.py

5. Follow the instructions prompted into your screen to download.

## Note

For the first time you run this program the terminal will display a code. Copy and paste this code into your browser to log in to your personal account on Youtube. 

## Issue

Occasionally, YouTube updates its mechanisms to prevent downloads. If you encounter an error related to the file cipher.py (located in site-packages) during the operation, modifications may be required.

When using PyTube version 15.0.0, update cipher.py on lines 272 and 273 with the following:

   ```bash
   r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
   r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',
   ```

If the problem persist, you may need to search for other solution.
