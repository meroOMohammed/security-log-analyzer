
import csv
import sys
import ipaddress

failed_logins = {}
total_events = 0
successful_logins = 0
unique_ips = set()
invalid_records = 0

log_file = sys.argv[1] if len(sys.argv) > 1 else "auth_logs.csv"

try:
    with open(log_file, "r", newline="") as file:
        lines = (line for line in file if line.strip())
        reader = csv.DictReader(lines)

        required_fields = [
            "timestamp",
            "source_ip",
            "username",
            "event_type",
            "status"
        ]

        if not reader.fieldnames or not all(
            field in reader.fieldnames for field in required_fields
        ):
            print("Error: CSV file is missing required columns.")
            raise SystemExit(1)

        for row in reader:
            if not all(row.get(field) for field in required_fields):
                invalid_records += 1
                continue

            if row["status"] not in ("success", "failed"):
                invalid_records += 1
                continue

            try:
                ipaddress.ip_address(row["source_ip"])
            except ValueError:
                invalid_records += 1
                continue

            total_events += 1
            unique_ips.add(row["source_ip"])

            if row["status"] == "success":
                successful_logins += 1

            elif row["status"] == "failed":
                ip = row["source_ip"]
                failed_logins[ip] = failed_logins.get(ip, 0) + 1

except FileNotFoundError:
    print(f"Error: {log_file} was not found.")
    raise SystemExit(1)

print("Log Summary")
print("-----------")
print(f"Valid events: {total_events}")
print(f"Successful logins: {successful_logins}")
print(f"Failed logins: {sum(failed_logins.values())}")
print(f"Unique source IPs: {len(unique_ips)}")
print(f"Invalid records skipped: {invalid_records}")

print("\nFailed Login Attempts")
print("---------------------")

for ip, count in failed_logins.items():
    print(f"{ip}: {count}")

print("\nIPs Requiring Review")
print("--------------------")

for ip, count in failed_logins.items():
    if count >= 3:
        print(f"[REVIEW] {ip}: {count} failed attempts")

# Save the analysis results to a CSV report
report_name = f"analysis_report_{log_file.rsplit('.', 1)[0]}.csv"

with open(report_name, "w", newline="", encoding="utf-8") as report_file:
    writer = csv.writer(report_file)

    writer.writerow(["Report Type", "Source IP", "Count", "Status"])
    writer.writerow(["Summary", "Input file", log_file, ""])

    writer.writerow(["Summary", "Valid events", total_events, ""])
    writer.writerow(["Summary", "Successful logins", successful_logins, ""])
    writer.writerow(["Summary", "Failed logins", sum(failed_logins.values()), ""])
    writer.writerow(["Summary", "Unique source IPs", len(unique_ips), ""])
    writer.writerow(["Summary", "Invalid records skipped", invalid_records, ""])

    for ip, count in failed_logins.items():
        status = "REVIEW" if count >= 3 else "Normal"
        writer.writerow(["Failed login attempts", ip, count, status])

print(f"\nReport saved to {report_name}")
