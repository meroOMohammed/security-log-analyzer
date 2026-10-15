\# Security Log Analyzer



\## Project Overview



Security Log Analyzer is a lightweight Python command-line tool that analyzes authentication logs stored in CSV format.



It summarizes login activity, counts failed login attempts by source IP address, validates input records, and flags IP addresses with repeated failed logins for further review.



This project uses synthetic authentication logs for educational and portfolio demonstration purposes.



\## Features



\- Reads authentication logs from CSV files.

\- Counts valid events, successful logins, and failed logins.

\- Identifies unique source IP addresses.

\- Validates required fields and source IP addresses.

\- Skips records with missing fields, invalid IP addresses, or unsupported login statuses.

\- Flags source IP addresses with three or more failed login attempts.

\- Exports analysis results to a CSV report for each successfully processed input file.

\- Handles missing input files and missing required CSV columns.



\## Requirements



\- Python 3.8 or later

\- No third-party Python packages required.



\## Project Files



\- `analyzer.py` — Main log analysis script.

\- `auth\_logs.csv` — Synthetic authentication log dataset.

\- `test\_logs.csv` — Test dataset containing valid and invalid records.

\- `bad\_headers.csv` — Test file with missing required columns.

\- `analysis\_report\_auth\_logs.csv` — Report generated from the main dataset.

\- `analysis\_report\_test\_logs.csv` — Report generated from the validation dataset.



\## How to Run



Open a terminal in the project directory.



Analyze the default dataset:



```bash

python analyzer.py

```



Analyze a specific CSV file:



```bash

python analyzer.py auth\_logs.csv

```



Run the validation test dataset:



```bash

python analyzer.py test\_logs.csv

```



Test a CSV file with missing required columns:



```bash

python analyzer.py bad\_headers.csv

```



Test missing-file handling:



```bash

python analyzer.py missing\_file.csv

```



\## Detection Logic



The tool counts failed login attempts for each source IP address.



An IP address with three or more failed login attempts is marked with `\[REVIEW]` for further investigation.



This is a fixed-threshold demonstration rule. A flagged IP address is not, by itself, proof of an attack or malicious activity. The tool does not correlate events over a time window.



\## Testing



The main synthetic dataset was tested with the following results:



\- Valid events: 13

\- Successful logins: 4

\- Failed logins: 9

\- Unique source IP addresses: 6

\- Invalid records skipped: 0



The validation dataset was also tested:



\- Valid events: 2

\- Successful logins: 1

\- Failed logins: 1

\- Unique source IP addresses: 2

\- Invalid records skipped: 3



Additional tests confirmed that the tool reports an error when required CSV columns are missing or the input file cannot be found.



\## Limitations



\- Analyzes authentication logs only; it does not inspect network traffic.

\- Uses a fixed threshold rather than time-based correlation or behavioral analysis.

\- Does not block IP addresses or perform automated incident response.

\- Uses synthetic data that does not represent real security incidents.

\- Is an educational tool, not a production SIEM solution.



\## Skills Demonstrated



\- Python scripting

\- CSV parsing and data validation

\- IP address validation

\- Authentication log analysis

\- Basic security event detection

\- Error handling and test-case validation

\- CSV report generation



\## Disclaimer



This project is an educational demonstration and is not intended to replace a production Security Information and Event Management (SIEM) solution.

