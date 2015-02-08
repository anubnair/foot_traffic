# -*- coding: utf-8 -*-
#!/usr/bin/python

from imports import*
__version__     = '1.0'
__author__      = 'Anu B Nair'


progname = os.path.basename(sys.argv[0])
usage = """\
usage: %s -f filename_with_path

options:
    -h --help
    -f --file
""" % progname

class FootTraffic:
    #This takes a formatted log file that describes the overall
    #gallery's foot-traffic on a minute-to-minute basis. From
    #this data we compute the average time spent in each
    #room, and how many visitors there were in each room.

    def __init__(self, traffic_list):
        """
        Constructor
        """
        self.traffic_list = traffic_list
        self.dict_traffic = {}
        self.list_rooms = []

    def __call__(self):
        """
        Call
        """
        self.process_traffic()
        self.show_result()

    def process_traffic(self):
        """
        Process daily visitors traffic
        """
        for visitor, room_number, in_out, time in self.traffic_list:
            if room_number not in self.dict_traffic:
                self.dict_traffic[room_number] = []
            self.dict_traffic[room_number].append(-int(time) \
                if in_out == 'I' else int(time))

        self.list_rooms = sorted(self.dict_traffic, \
                            key=lambda key_value: int(key_value))

    def show_result(self):
        """
        show result
        """
        for key in self.list_rooms:
            visitors = len(self.dict_traffic[key])/2
            print("Room %2s, %d minute average visit, %d visitor(s) total" \
                    % (key, sum(self.dict_traffic[key])/visitors+1, visitors))

def main():
    """
    Main Function
    """
    if len(sys.argv) < 1 or "-h" in sys.argv or "--help" in sys.argv:
        sys.exit(usage)
    parser = argparse.ArgumentParser(description='Process Foot-Traffic Analysis.')
    parser.add_argument('-f', metavar='--file', \
                                help='file name with path for processing')

    args = parser.parse_args()
    if args.f == None:
        sys.exit(usage)
    try:
        f = [line.split() for line in open(args.f)][1:]
        foottraffic = FootTraffic(f)
        foottraffic()

    except IOError:
        print '*'*100
        print 'cannot open the file/No such file in path exist.'
        print '*'*100
        sys.exit(usage)

if __name__ == '__main__':
    main()
