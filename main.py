from getevents import get_events
from toexcelandcsv import toexcelandcsv

if __name__ == '__main__':
    city = input("Enter the city:")
    results = get_events(city)
    toexcelandcsv(results, city)
    print("Data Scrapped")
