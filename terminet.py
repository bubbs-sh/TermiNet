try:
    from bs4 import BeautifulSoup
    import requests
    import time
    import sys
    import datetime

    try:
        #printing out TERMINET
        def print_ascii_art(version):
            red = "\033[91m"  
            yellow = "\033[93m"  
            green = "\033[92m"  
            reset_color = "\033[0m" 
            ascii_art = f"""
    {red} _____                   _ _   _      _   {reset_color}
    {red}|_   _|__ _ __ _ __ ___ (_) \ | | ___| |_ {reset_color}
    {yellow}  | |/ _ \ '__| '_ ` _ \| |  \| |/ _ \ __|{reset_color}
    {yellow}  | |  __/ |  | | | | | | | |\  |  __/ |_ {reset_color}
    {green}  |_|\___|_|  |_| |_| |_|_|_| \_|\___|\__|{version}{reset_color}
    {green}   By bubbs-sh {reset_color}@{reset_color} {green}bubbs.sh{reset_color}
    """
            print(ascii_art)

        if __name__ == "__main__":
            version = "v1.0"
            print_ascii_art(version)



        # getting a message based on the device time
        def greet():
            current_time = datetime.datetime.now()
            hour = current_time.hour

            if 5 <= hour < 12:
                return "morning?"
            elif 12 <= hour < 17:
                return "afternoon?"
            else:
                return "evening?"

        greeting = greet()

        if len(sys.argv) < 2:
            print("Wait, seriously? It's either [MOVIE -m] or [SERIES -s].\nPick one and let's roll!")
            exit()

        else:

            what = sys.argv[1]

        

            # check if arguments is greater than 1
            if what == "-m":
                if len(sys.argv) > 2:

                    # getting the keywords as args
                    args = sys.argv[2:]

                    keyword = "+".join(args)
                    domain = "https://netnaija.xyz/?s="
                    print()
                    # print(domain+keyword)
                    print("\033[94mShowing results for", '"' + " ".join(sys.argv[2:]) + '"\033[0m')
                    print()
                    # requesting the url data
                    page = requests.get(domain + keyword)

                    # parsing page data
                    soup = BeautifulSoup(page.text, "lxml")
                    pages = soup.find("ul", class_="pages-numbers")
                    last = soup.find("li", class_="last-page first-last-pages")

                    for data in soup.find_all(
                        "li",
                        class_=["post-item tie-standard", "post-item is-trending tie-standard","date meta tie-icon"],
                    ):
                        if data:

                            try:
                                #
                                z = data.text
                                z = z.lstrip()
                                z = z.split(" ")
                                #i = i[0]
                                try:
                                    title = data.a["aria-label"]
                                except KeyError:
                                    continue
                                #
                                link = data.a["href"]
                                link1 = "https://netnaija.xyz/"
                                print()

                                print("\033[92mTITLE:\033[0m", title)
                                print("\033[92mUPLOADED:\033[0m",z[0],z[1],z[2])
                                print("\033[92mMOVIE URL:\033[0m","\033[94m"+ link1 + link+"\033[0m")
                                print("\033[92m__________________________________________\033[0m")
                                print()
                                # print()
                            except:
                                print("\033[91mMovie N/A\033[0m")

                # algorithm to list the number of pages and choose from the list
                    if pages:
                        if last is not None:
                            print("\033[93m[", "END OF PAGE 1", "]\033[0m")
                            print()
                            print()

                            last1 = last.a["href"]
                            i = "/?s=" + keyword
                            j = last1.split(i)
                            k = "".join(j)
                            l = k.split("page/")
                            m = "".join(l)

                            length = m
                            length = int(length)
                            length_str = str(length)


                            while length > 1:
                                select = input("Select a page from 1 to " + length_str + ":\n")

                                try:
                                    select = int(select)
                                    if 1 <= select <= length:
                                        if select == 1:
                                            page = requests.get(domain + keyword)

                                            if page.status_code == 404:
                                                print("\033[91m"+"404 Page Not Found *_*"+"\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon"
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    title = data.a["aria-label"]

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m",z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a["href"]

                                                    print(
                                                        "\033[92mMOVIE URL:\033[0m","\033[94m"+
                                                        "https://netnaija.xyz/" + vid_link+"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()

                                        else:
                                            # retrieving the HTML content
                                            page = requests.get(
                                                "https://netnaija.xyz/page/" + str(select) + "/" + "?s=" + keyword
                                            )

                                            if page.status_code == 404:
                                                print("\033[91m"+"404 Page Not Found *_*"+"\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon"
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title

                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    try:
                                                        title = data.a["aria-label"]
                                                    except KeyError:
                                                        continue

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m",z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a['href']

                                                    print(
                                                        "\033[92mMOVIE URL:\033[0m","\033[94m"+
                                                        "https://netnaija.xyz/" + vid_link+"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()
                                                    # print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()

                                    else:
                                        print("\033[91mInvalid range. Select from 1 to ", length_str,"\033[0m")

                                        # converting select to int

                                        # logic from user input

                                except ValueError:
                                    print("\033[91mInvalid character. Please enter a valid integer\033[0m")

                        else:
                            print("\033[94m[", "END OF PAGE 1", "]\033[0m")
                            print()
                            print()
                            length = len(pages)
                            length = int(length) - 2
                            length_str = str(length)

                            while length > 1:
                                select = input("Select a page from 1 to " + length_str + ":\n")

                                try:
                                    select = int(select)
                                    if 1 <= select <= length:
                                        if select == 1:
                                            page = requests.get(domain + keyword)

                                            if page.status_code == 404:
                                                print("\033[91m404 Page Not Found *_*\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon"
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    title = data.a["aria-label"]

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m",z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a["href"]

                                                    print(
                                                        "\033[92mMOVIE URL:\033[0m","\033[94m"+
                                                        "https://netnaija.xyz/" + vid_link,"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()
                                                    # print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()
                                        else:
                                            # retrieving the HTML content
                                            page = requests.get(
                                                "https://netnaija.xyz/page/" + str(select) + "/"
                                            )

                                            if page.status_code == 404:
                                                print("\033[91m404 Page Not Found *_*\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon",
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    title = data.a["aria-label"]

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m",z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a["href"]

                                                    print(
                                                        "\033[92mMOVIE URL:\033[0m","\033[94m"+
                                                        "https://netnaija.xyz/" + vid_link,"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()
                                                    # print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()

                                    else:
                                        print("\033[91mInvalid range. Select from 1 to ", length_str,"\033[0m")

                                        # converting select to int

                                        # logic from user input

                                except ValueError:
                                    print("\033[91mInvalid character. Please enter a valid integer\033[0m")

                # if arguments is greater than one
                else:

                    # accept input, convert it int then to str
                    try:
                        print()
                        print("\033[94mWhat would you like to watch, this", greeting,"\033[0m")
                        print()
                        print()
                        page = requests.get("https://netnaija.xyz/")
                        # creating soup
                        soup = BeautifulSoup(page.text, "lxml")
                        pages = soup.find("ul", class_="pages-numbers")
                        last = soup.find("li", class_="last-page first-last-pages")

                        for data in soup.find_all(
                            "li",
                            class_=["post-item tie-standard", "post-item is-trending tie-standard","date meta tie-icon"],
                        ):
                            # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                            # scrapping video title
                            z = data.text
                            z = z.lstrip()
                            z = z.split(" ")
                            z = z[0],z[1],z[2]
                            z = " ".join(z)
                            z = z.split("0")
                            z = z[0]
                            #i = i[0]
                            try:
                                title = data.a["aria-label"]
                            except KeyError:
                                continue

                            
                            print("\033[92mTITLE:\033[0m", title)
                            print("\033[92mUPLOADED:\033[0m", z)

                            # movie date
                            # print("UPLOADED:", span_tag.text)

                            # getting vid link
                            vid_link = data.a["href"]

                            print("\033[92mMOVIE URL:\033[0m","\033[94m"+ "https://netnaija.xyz/" + vid_link+"\033[0m")
                            print("\033[92m__________________________________________\033[0m")
                            print()

                        print()
                        print("\033[93m[ END OF PAGE 1 ]\033[0m")
                        print()

                        while True:

                            last1 = last.a["href"]
                            i = "/"
                            j = last1.split(i)
                            k = "".join(j)
                            l = k.split("page")
                            m = "".join(l)

                            length = m
                            length = int(length)
                            length_str = str(length)

                            raw = input("Select a page from 1 to "+ length_str +":\n")

                            try:
                                raw = int(raw)
                                if 1 <= raw <= length:
                                    raw2 = str(raw)

                                    # retrieving the HTML content
                                    page = requests.get("https://netnaija.xyz/page/" + raw2 + "/")

                                    if page.status_code == 404:
                                        print("\033[91m404 Page Not Found *_*\033[0m")
                                    else:

                                        # creating soup
                                        soup = BeautifulSoup(page.text, "lxml")

                                        for data in soup.find_all(
                                            "li",
                                            class_=[
                                                "post-item tie-standard",
                                                "post-item is-trending tie-standard",
                                                "date meta tie-icon",
                                            ],
                                        ):
                                            # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                            # scrapping video title
                                            z = data.text
                                            z = z.lstrip()
                                            z = z.split(" ")
                                            z = z[0],z[1],z[2]
                                            # date tuple
                                            my_tuple = z

                                            # convert tuple  to strings
                                            tuple_as_strings = [str(item) for item in my_tuple]

                                            # joining elements
                                            result_string = ' '.join(tuple_as_strings)

                                            z = result_string[:-1]
                                            #z = z.split("0")
                                            #z = z[0]
                                            #i = i[0]
                                            try:
                                                title = data.a["aria-label"]
                                            except KeyError:
                                                continue

                                            print()
                                            print("\033[92mTITLE:\033[0m", title)
                                            print("\033[92mUPLOADED:\033[0m", z)

                                            # movie date
                                            # print("UPLOADED:", span_tag.text)

                                            # getting vid link
                                            vid_link = data.a["href"]

                                            print("\033[92mMOVIE URL:\033[0m","\033[94m"+ "https://netnaija.xyz/" + vid_link,"\033[0m")
                                            print("\033[92m__________________________________________\033[0m")
                                            print()
                                            # print()

                                        print()
                                        print("\033[93m[", "END OF PAGE", raw2, "]\033[0m")
                                        print()

                                else:
                                    print("\033[91mInvalid range. Select from 1 -", length_str,"\033[0m")
                            except ValueError:
                                print("\033[91mInvalid character. Please enter a valid integer\033[0m")

                    except requests.exceptions.ConnectionError:
                        print("\033[91mConnect to the internet first :)\033[0m")

            elif what == "-s":
                #checking the length of args
                if len(sys.argv) > 2:
                    # getting the keywords as args
                    args = sys.argv[2:]

                    keyword = "+".join(args)
                    domain = "https://series.netnaija.xyz/?s="
                    print()
                    # print(domain+keyword)
                    print("\033[94m","Showing results for", '"' + " ".join(sys.argv[2:]) + '"\033[0m')
                    print()
                    # requesting the url data
                    page = requests.get(domain + keyword)

                    # parsing page data
                    soup = BeautifulSoup(page.text, "lxml")
                    pages = soup.find("ul", class_="pages-numbers")
                    last = soup.find("li", class_="last-page first-last-pages")

                    for data in soup.find_all(["li","span"], class_=["post-item tie-standard", "post-item is-trending tie-standard","date meta tie-icon"],):
                        if data:

                            try:
                                #
                                i = data.text
                                i = i.lstrip()
                                i = i.split(" ")
                                #i = i[0]
                                #
                                try:
                                    title = data.a["aria-label"]
                                except KeyError:
                                    continue
                                #
                                link = data.a["href"]
                                link1 = "https://series.netnaija.xyz/"
                                print()

                                print("\033[92mTITLE:\033[0m", title)
                                print("\033[92mUPLOADED:\033[0m", i[0],i[1],i[2])
                                print("\033[92mSHOW URL:\033[0m","\033[94m", link1 + link+"\033[0m")
                                print("\033[92m__________________________________________\033[0m")
                                print()
                                # print()
                            except:
                                print("\033[91mTV SHOW N/A\033[0m")
                        
                    #algorithm to check available pages
                    if pages:
                        if last is not None:
                            print()
                            print("\033[93m[", "END OF PAGE 1", "]\033[0m")
                            print()

                            last1 = last.a["href"]
                            i = "/?s=" + keyword
                            j = last1.split(i)
                            k = "".join(j)
                            l = k.split("page/")
                            m = "".join(l)

                            length = m
                            length = int(length)
                            length_str = str(length)

                            while length > 1:
                                select = input("Select a page from 1 to " + length_str + ":\n")

                                try:
                                    select = int(select)
                                    if 1 <= select <= length:
                                        if select == 1:
                                            page = requests.get(domain + keyword)

                                            if page.status_code == 404:
                                                print("\033[91m404 Page Not Found UwU\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(["li","span"],class_=["post-item tie-standard","post-item is-trending tie-standard","date meta tie-icon",],):
                                                    
                                                    #getting the uploaded date from the data
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]

                                                    #scrapping video title
                                                    try:
                                                        title = data.a["aria-label"]
                                                    except KeyError:
                                                        continue

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m", z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a["href"]

                                                    print(
                                                        "\033[92mSHOW URL:\033[0m","\033[94m"
                                                        "https://series.netnaija.xyz/" + vid_link,"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()

                                        else:
                                            # retrieving the HTML content
                                            page = requests.get(
                                                "https://series.netnaija.xyz/page/" + str(select) + "/" + "?s=" + keyword 
                                                
                                            )

                                            if page.status_code == 404:
                                                print("\033[91m","404 Page Not Found *_*","\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon",
                                                        "post-thumb"
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title
                                                    #getting uploaded date from data
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    try:
                                                        title = data.a['aria-label']
                                                    except KeyError:
                                                        continue

                                                    print()
                                                    print("\033[92mTITLE:]\033[0m", title)
                                                    print("\033[92mUPLOADED:]\033[0m", z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a['href']

                                                    print(
                                                        "\033[92mSHOW URL:]\033[0m","\033[94m"+
                                                        "https://series.netnaija.xyz/" + vid_link,"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________]\033[0m"
                                                    )
                                                    print()
                                                    # print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()

                                    else:
                                        print("\033[91mInvalid range. Select from 1 to ", length_str+"\033[0m")

                                        # converting select to int

                                        # logic from user input

                                except ValueError:
                                    print("\033[91mInvalid character. Please enter a valid integer\033[0m")

                        else:
                            print()
                            print("\033[93m[", "END OF PAGE 1", "]\033[0m")
                            print()
                            length = len(pages)
                            length = int(length) - 2
                            length_str = str(length)

                            while length > 1:
                                select = input("Select a page from 1 to " + length_str + ":\n")

                                try:
                                    select = int(select)
                                    if 1 <= select <= length:
                                        if select == 1:
                                            page = requests.get(domain + keyword)

                                            if page.status_code == 404:
                                                print("\033[91m404 Page Not Found *_*\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon",
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title
                                                    #getting uploaded date from data
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    try:
                                                        title = data.a["aria-label"]
                                                    except KeyError:
                                                        continue

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m", z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a["href"]

                                                    print(
                                                        "\033[92mSHOW URL:\033[0m","\033[94m"+
                                                        "https://series.netnaija.xyz/" + vid_link,"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()
                                                    # print()

                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()
                                                print()
                                        else:
                                            # retrieving the HTML content
                                            page = requests.get(
                                                "https://series.netnaija.xyz/page/" + str(select) + "/" + keyword 
                                            )

                                            if page.status_code == 404:
                                                print("\033[91m","404 Page Not Found *_*","\033[0m")
                                            else:

                                                # creating soup
                                                soup = BeautifulSoup(page.text, "lxml")

                                                for data in soup.find_all(
                                                    "li",
                                                    class_=[
                                                        "post-item tie-standard",
                                                        "post-item is-trending tie-standard",
                                                        "date meta tie-icon",
                                                    ],
                                                ):
                                                    # for span_tag in soup.find_all("span", class_="date meta-item tie-icon"):

                                                    # scrapping video title
                                                    #getting uplaoded date from data
                                                    z = data.text
                                                    z = z.lstrip()
                                                    z = z.split(" ")
                                                    #i = i[0]
                                                    try:
                                                        title = data.a["aria-label"]
                                                    except KeyError:
                                                        continue

                                                    print()
                                                    print("\033[92mTITLE:\033[0m", title)
                                                    print("\033[92mUPLOADED:\033[0m", z[0],z[1],z[2])

                                                    # movie date
                                                    # print("UPLOADED:", span_tag.text)

                                                    # getting vid link
                                                    vid_link = data.a["href"]

                                                    print(
                                                        "\033[92mSHOW URL:\033[0m","\033[94m"+
                                                        "https://series.netnaija.xyz/" + vid_link,"\033[0m"
                                                    )
                                                    print(
                                                        "\033[92m__________________________________________\033[0m"
                                                    )
                                                    print()
                                                    # print()

                                                print()
                                                print("\033[93m[", "END OF PAGE", str(select), "]\033[0m")
                                                print()

                                    else:
                                        print("\033[91mInvalid range. Select from 1 to ", length_str,"\033[0m")

                                        # converting select to int

                                        # logic from user input

                                except ValueError:
                                    print("\033[91mInvalid character. Please enter a valid integer")


                #if args is greater than 1:
                else:
                    print()
                    print("\033[94mWhat would you like to watch, this", greeting,"\033[0m")
                    print()
                    print()
                    domain = "https://series.netnaija.xyz/"

                    page = requests.get("https://series.netnaija.xyz/")
                    #create soup
                    soup = BeautifulSoup(page.text, "lxml")
                    datas = soup.find_all(["li","span"],class_=["post-item tie-standard","post-item is-trending tie-standard","date meta tie-icon",])
                    pages = soup.find("ul", class_="pages-numbers")
                    last = soup.find("li", class_="last-page first-last-pages")

                    for data in datas:
                        z = data.text
                        z = z.lstrip()
                        z = z.split(" ")
                        z = z[0],z[1],z[2]
                        z = " ".join(z)
                        z = z.split("0")
                        z = z[0]
                        #i = i[0]

                        try:
                            title = data.a['aria-label']
                        except KeyError:
                            continue

                        link = data.a['href']
                        print("\033[92mTITLE:\033[0m",title)
                        print("\033[92mUPLOADED:\033[0m", z)

                        print("\033[92mSHOW URL:\033[0m","\033[94m"+ domain+link,"\033[0m")
                        print("\033[92m__________________________________________\033[0m")
                        print()

                    print()
                    print("\033[93m[ END OF PAGE 1 ]\033[0m")
                    print()


                    while True:

                        last1 = last.a["href"]
                        i = "/"
                        j = last1.split(i)
                        k = "".join(j)
                        l = k.split("page")
                        m = "".join(l)

                        length = m
                        length = int(length)
                        length_str = str(length)

                        raw = input("Select a page from 1 to "+ length_str+":\n")

                        try:
                            raw = int(raw)
                            if 1 <= raw <= length:
                                raw2 = str(raw)

                                # retrieving the HTML content
                                page = requests.get("https://series.netnaija.xyz/page/" + raw2 + "/")

                                if page.status_code == 404:
                                    print("\033[91m404 Page Not Found UwU\033[0m")
                                else:

                                    # creating soup
                                    soup = BeautifulSoup(page.text, "lxml")

                                    for data in soup.find_all(
                                        "li",
                                        class_=[
                                            "post-item tie-standard",
                                            "post-item is-trending tie-standard",
                                            "date meta tie-icon",
                                        ],
                                    ):


                                        # scrapping video title
                                        z = data.text
                                        z = z.lstrip()
                                        z = z.split(" ")
                                        z = z[0],z[1],z[2]
                                        # date tuple
                                        my_tuple = z

                                        # convert tuple  to strings
                                        tuple_as_strings = [str(item) for item in my_tuple]

                                        # joining elements
                                        result_string = ' '.join(tuple_as_strings)

                                        z = result_string[:-1]
                                        #z = z.split("0")
                                        #z = z[0]
                                        #i = i[0]
                                        try:
                                            title = data.a["aria-label"]
                                        except KeyError:
                                            continue

                                        print()
                                        print("\033[92mTITLE:\033[0m", title)
                                        print("\033[92mUPLOADED:\033[0m", z)

                                        # movie date
                                        # print("UPLOADED:", span_tag.text)

                                        # getting vid link
                                        vid_link = data.a["href"]

                                        print("\033[92mSHOW URL:\033[0m","\033[94m"+ "https://series.netnaija.xyz/" + vid_link, "\033[0m")
                                        print("\033[92m__________________________________________\033[0m")
                                        print()
                                        # print()

                                    print()
                                    print("\033[93m[", "END OF PAGE", raw2, "]\033[0m")
                                    print()

                            else:
                                print()
                                print("\033[91mInvalid range.\033[0m")
                        except ValueError:
                            print("\033[91mInvalid character. Please enter a valid integer\033[0m")

            

            
    except KeyboardInterrupt:
        print("\033[33mbubbs-sh\033[0m @ \033[33mbubbs.sh\033[0m : \033[95mArigato!\033[0m")
        exit()
except requests.exceptions.ConnectionError:
    print("\033[91mConnect to the internet first :)\033[0m")