import sys, getopt
from report import load_data, build_report

def main(argv):
    if argv:
        inputfile = argv[0]
    else:
        raise ValueError("python main.py <inputfile>")
    presences = load_data(inputfile)
    report = build_report(presences)
    print(report)
    
if __name__ == "__main__":
    main(sys.argv[1:])