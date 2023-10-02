Please note that you can change the value of SCROLL_PAUSE_TIME in getevents.py line 22 as you want. When your internet connection is bad, please increase the value not to miss some data.

1. Install Python > 3.10
2. Install necessary modules.
pip install bs4 pandas openpyxl
3. Run main.py
python main.py
4. Input the city.
The city name should be in camelcase. The state name should be in lowercase and those must be separated by ", ".
e.g. Port Isabel, tx
Some city names should be checked on Meetup. You can check this name in the search url.
e.g. Washington D.C -> Washington, dc
5. Press Enter. When the browser opens, do not close it.
6. Wait for a while and you will get the images, xlsx and csv.