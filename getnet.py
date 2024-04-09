from bs4 import BeautifulSoup
import requests
import sys
args = sys.argv
def print_ascii_art(version):
    red = "\033[91m"  # ANSI escape code for red color
    yellow = "\033[93m"  # ANSI escape code for yellow color
    green = "\033[92m"  # ANSI escape code for green color
    reset_color = "\033[0m"  # ANSI escape code to reset color
    ascii_art = f"""
{red} _____                   _ _   _      _   {reset_color}
{red}|_   _|__ _ __ _ __ ___ (_) \ | | ___| |_ {reset_color}
{yellow}  | |/ _ \ '__| '_ ` _ \| |  \| |/ _ \ __|{reset_color}
{yellow}  | |  __/ |  | | | | | | | |\  |  __/ |_ {reset_color}
{green}  |_|\___|_|  |_| |_| |_|_|_| \_|\___|\__|{version}{reset_color}
{green}   By Bubbs-sh{reset_color}   
"""
    print(ascii_art)

if __name__ == "__main__":
    version = "v1.0"
    print_ascii_art(version)

if len(sys.argv) < 2:
    print("Wait, seriously? It's either [MOVIE -m] or [SERIES -s].\nPick one and let's roll!")
elif len(sys.argv) < 3:
    print("Really? Where's the download link? 🤔")
else:
    what = sys.argv[1]

    if what == "-m":

        try:
            #getting the url
            page = requests.get(sys.argv[2])

            #creating a download page soup
            soup = BeautifulSoup(page.text, "lxml")

            data = soup.find("div", class_="main-content tie-col-md-12")
            name = soup.find("h1", class_="post-title entry-title")
            details = soup.find("blockquote", class_="wp-block-quote")
            #p_tags = soup.find("blockquote", class_="wp-block-quote").find_all("p")

            #scrapping movie title/name
            print()
            print("\033[92mTitle:\033[0m")
            print(name.text)
            print("\033[92m_______________________________\033[0m")
            print()

            #getting movie plot
            plot = data.p
            plot = plot.text

            print("\033[92mPlot:\033[0m")
            print(plot)
            print("\033[92m_______________________________\033[0m")
            print()
            print()

            #getting movie info

            if details:
                # Find all <p> tags within the <blockquote> element
                p_tags = details.find_all("p")
            
                # Check if there are at least two <p> tags
                if len(p_tags) >= 4:
                    # Get the content of the second <p> tag
                    print(p_tags[0].text)
                    print(p_tags[1].text)
                    print(p_tags[2].text)
                    print(p_tags[3].text)
                elif len(p_tags) >= 3:
                    print(p_tags[0].text)
                    print(p_tags[1].text)
                    print(p_tags[2].text)
                elif len(p_tags) >= 2:
                    print(p_tags[0].text)
                    print(p_tags[1].text)
                elif len(p_tags) >= 1:
                    print(p_tags[0].text)
                else:
                    print("Info N/A")
            print("\033[92m"+"_______________________________"+"\033[0m")
            print()
            print()
            #print(p_tags[0].text)
            #print(p_tags[1].text)
            #print(p_tags[2].text)
            #print(p_tags[3].text)
            #print()

            #accessing vid link
            link = soup.find("div", class_="wp-block-button")
            url = link.a["href"]
            i = "https:"
            download_link = i + url

            print("Download Movie:")
            print("\033[34m"+download_link+"\033[0m")  
            print()
        except requests.exceptions.ConnectionError:
            print("\033[91mConnect to the internet first :)\033[0m")
    elif what == "-s":
        try:
            #getting the url
            page = requests.get(sys.argv[2])

            #creating a download page soup
            soup = BeautifulSoup(page.text, "lxml")

            data = soup.find("div", class_="main-content tie-col-md-12")
            name = soup.find("h1", class_="post-title entry-title")
            details = soup.find("blockquote", class_="wp-block-quote")
            #p_tags = soup.find("blockquote", class_="wp-block-quote").find_all("p")

            #scrapping movie title/name
            print()
            print("\033[92mTitle:\033[0m")
            print(name.text)
            print("\033[92m_______________________________\033[0m")
            print()

            #getting movie plot
            plot = data.p
            plot = plot.text

            print("\033[92mPlot:\033[0m")
            print(plot)
            print("\033[92m_______________________________\033[0m")
            print()
            print()

            #getting movie info

            if details:
                # Find all <p> tags within the <blockquote> element
                p_tags = details.find_all("p")
            
                # Check if there are at least two <p> tags
                if len(p_tags) >= 4:
                    # Get the content of the second <p> tag
                    print(p_tags[0].text)
                    print(p_tags[1].text)
                    print(p_tags[2].text)
                    print(p_tags[3].text)
                elif len(p_tags) >= 3:
                    print(p_tags[0].text)
                    print(p_tags[1].text)
                    print(p_tags[2].text)
                elif len(p_tags) >= 2:
                    print(p_tags[0].text)
                    print(p_tags[1].text)
                elif len(p_tags) >= 1:
                    print(p_tags[0].text)
                elif len(p_tags) < 2 and len(p_tags) == 1:
                    print("Info N/A")
            print("\033[92m_______________________________\033[0m")
            print()
            print()
            #print(p_tags[0].text)
            #print(p_tags[1].text)
            #print(p_tags[2].text)
            #print(p_tags[3].text)
            #print()

            #accessing vid link
            link = soup.find_all("div", class_="wp-block-button")
            
            #this represents the number of episodes
            a = 0

            for l in link:
                url = l.a["href"]
                i = "https:"
                download_link = i + url
                a += 1
                print(f"Download Episode {a}:")
                print("\033[34m"+download_link+"\033[0m")  
                #print("\033[92m_______________________________\033[0m")
                print()
        except requests.exceptions.ConnectionError:
            print("\033[91mConnect to the internet first :)\033[0m")
    elif what != "-s" and what != "-m" :
        print("Wait, seriously? It's either [MOVIE -m] or [SERIES -s].\nPick one and let's roll!")