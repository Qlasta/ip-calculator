# ip-calculator
program receives ip format (ipv4,ipv6), 2 IPs and returns number of addresses between them

- Go to Linux terminal.
- Make sure you have python3 installed (`sudo apt-get install python3`)
- Make sure you have git installed (`sudo apt-get install git`)
- In your terminal enter: `git clone https://github.com/Qlasta/ip-calculator.git`
- Go into directory: `cd ip-calculator`
- Run program main.py, by giving 3 arguments [IP type] [Starting IP] [Ending IP]: `python3 main.py ipv4 10.2.2.5 10.2.2.100`
- Program will return count of addresses between given, not including the ending one.
- If IP format is not valid or starting address is greater than the ending one, program will return errors.

P.S.: You can enter IP's manually by starting a program without command line arguments: `python3 main.py` and follow instructions.

