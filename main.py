import pandas as pd
import configparser
import os


# Read local file `config.ini`.
config = configparser.ConfigParser()
config.read('config.ini')

# Local variables
intervals = {
    "1m" : 1,
    "3m" : 3,
    "5m" : 5,
    "15m" : 15,
    "30m" : 30,
    "1h" : 60,
    "2h" : 120,
    "4h" : 240,
    "6h" : 360,
    "8h" : 480,
    "12h" : 720,
    "1d" : 1440,
    "1M" : 2880,
}

panda_conversion = {
    "1m" : "1Min",
    "3m" : "3Min",
    "5m" : "5Min",
    "15m" : "15Min",
    "30m" : "30Min",
    "1h" : "1H",
    # "2h" : 120,
    # "4h" : 240,
    # "6h" : 360,
    # "8h" : 480,
    # "12h" : 720,
    # "1d" : 1440,
    # "1M" : 2880,
}


def main():
    # iterate over files in
    # that directory
    for filename in os.scandir(config["APP"]["SOURCE_FILE_PATH"]):
        if filename.is_file():
            new_interval = '2T'
            df = pd.read_csv(filepath_or_buffer=filename.path, header=0)
            df['ts'] = pd.to_datetime(df['ts'])
            # df = df.set_index('ts')
            # print(df.head(10))
            df.resample(new_interval, on='ts')\
                .agg({'o': 'first',
                      'h': 'max',
                      'l': 'min',
                      'c': 'last',
                      'v': 'sum',
                      'nt': 'sum'})
            old_filename = filename.name
            old_interval = old_filename.split('_')[1]
            new_filename = f"{config['APP']['DESTINATION_PATH']}/{old_filename.replace(old_interval, new_interval)}"
            df.to_csv(new_filename, encoding='utf-8', index=False, header=True)

if __name__ == '__main__':
    main()
