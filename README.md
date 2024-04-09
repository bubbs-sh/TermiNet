```
     _____                   _ _   _      _   
    |_   _|__ _ __ _ __ ___ (_) \ | | ___| |_ 
      | |/ _ \ '__| '_ ` _ \| |  \| |/ _ \ __|
      | |  __/ |  | | | | | | | |\  |  __/ |_ 
      |_|\___|_|  |_| |_| |_|_|_| \_|\___|\__|v1.0     
```
# TermiNet
TermiNet is a command-line tool that enables you to search for your favorite TV shows and movies from NetNaija directly within your terminal. With TermiNet, you can effortlessly browse through the vast library of content without leaving your command line interface.

## Features
- **Search**: Instantly find TV shows and movies using simple commands right from your terminal.
- **Browse**: Quickly scroll through search results within the terminal for seamless exploration.
- **Downloads**: Effortlessly open your default web browser to access the download link for selected content.

## Requirements
```
sudo apt update -y

sudo apt install python3

pip install lxml

pip install requests

pip install beautifulsoup4
```

## Installation For Linux/Termux
```
git clone https://github.com/bubbs-sh/TermiNet.git

cd TermiNet

pip install -r requirements.txt
```


## Usage

### Searching Movie/TV show
- To browse all movies: ` python3 terminet.py -m `
- To browse all TV shows/series: ` python3 terminet.py -s `
- To search for a particular movie: ` python3 terminet.py -m [movie name] `
- To search for a particular show: ` python3 terminet.py -s [series name] `

**Copy Movie/Show URL**

### Download Movie/TV show
- To download movie: ` python3 getnet.py -m [movie URL] `
- To download TV show/series: ` python3 getnet.py -m [show URL] `

**Open download link in a browser**
