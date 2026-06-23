from collections import Counter
import matplotlib.pyplot as plt

file = open("log.txt", "r")
logs = file.readlines()
file.close()

info_count = 0
warning_count = 0
error_count = 0

errors = []

for line in logs:

    if "INFO" in line:
        info_count += 1

    elif "WARNING" in line:
        warning_count += 1

    elif "ERROR" in line:
        error_count += 1
        errors.append(line.strip())

print("===== LOG SUMMARY =====")
print("INFO:", info_count)
print("WARNING:", warning_count)
print("ERROR:", error_count)

print("\nMost Common Errors")

error_counter = Counter(errors)

for error, count in error_counter.items():
    print(error, ":", count)

report = open("report.txt", "w")

report.write("LOG ANALYSIS REPORT\n")
report.write("===================\n")
report.write(f"INFO: {info_count}\n")
report.write(f"WARNING: {warning_count}\n")
report.write(f"ERROR: {error_count}\n")

report.close()

print("\nReport Generated Successfully")
labels = ["INFO", "WARNING", "ERROR"]
values = [info_count, warning_count, error_count]

plt.bar(labels, values)

plt.title("Log Analysis")
plt.xlabel("Log Type")
plt.ylabel("Count")

plt.show()