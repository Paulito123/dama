


class Dama:
    def __init__(self, input_fdir, output_fdir):
        self.input_fdir = input_fdir
        self.output_fdir = output_fdir

        self.intervals = {
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


    def resample_to(self, interval="1h"):
        if self.intervals.get(interval):
            pass
        else:
            pass

