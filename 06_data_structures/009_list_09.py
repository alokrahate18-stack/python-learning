"""Q2: Log analyzer (time library + strings + lists + loops + conditions + functions)
python
logs = \"""2026-09-06 14:03:22 | ERROR | disk full
2026-09-06 14:03:25 | INFO | retrying
bad line here
2026-09-06 13:59:01 | ERROR | disk full
2026-09-06 14:10:00 | ERROR | timeout
2026-09-06 25:00:00 | ERROR | impossible hour
2026-09-06 14:20:45 | WARN | slow
2026-09-06 14:20:45 | ERROR | disk full\"""

Without try/except and without dicts:

Parse every valid line into [datetime, level, message]. Skip lines with the wrong structure and lines whose time is impossible (hour ≥ 24, minute or second ≥ 60). Validate the time part yourself with slicing and conditions before calling datetime.strptime. Assume the dates themselves are real.
Sort the entries chronologically. Entries with the same timestamp must keep their original input order.
For each level (in first-appearance order), find the longest gap between consecutive entries of that level. Levels with a single entry print n/a. Format the gap as 1h 02m 03s using // and %, in a function.
Find the single minute (YYYY-MM-DD HH:MM) with the most entries. On a tie, choose the earliest.
Print a neat aligned table using f-string format specs (:<8, :>12).
- By Claude"""

from datetime import datetime


logs = """2026-09-06 14:03:22 | ERROR | disk full
2026-09-06 14:03:25 | INFO | retrying
bad line here
2026-09-06 13:59:01 | ERROR | disk full
2026-09-06 14:10:00 | ERROR | timeout
2026-09-06 25:00:00 | ERROR | impossible hour
2026-09-06 14:20:45 | WARN | slow
2026-09-06 14:20:45 | ERROR | disk full"""


def is_valid_time_text(time_text):
    """Validate HH:MM:SS manually before calling datetime.strptime."""
    if len(time_text) != 8:
        return False

    if time_text[2] != ":" or time_text[5] != ":":
        return False

    hour_text = time_text[0:2]
    minute_text = time_text[3:5]
    second_text = time_text[6:8]

    if not hour_text.isascii() or not hour_text.isdigit():
        return False

    if not minute_text.isascii() or not minute_text.isdigit():
        return False

    if not second_text.isascii() or not second_text.isdigit():
        return False

    hour = int(hour_text)
    minute = int(minute_text)
    second = int(second_text)

    if hour >= 24 or minute >= 60 or second >= 60:
        return False

    return True


def parse_log_line(line):
    """
    Return [datetime, level, message] for a valid line.
    Return None for a malformed or invalid-time line.
    """
    parts = line.split(" | ")

    if len(parts) != 3:
        return None

    timestamp_text = parts[0]
    level = parts[1]
    message = parts[2]

    if not level or not message:
        return None

    if len(timestamp_text) != 19:
        return None

    if timestamp_text[10] != " ":
        return None

    date_text = timestamp_text[0:10]
    time_text = timestamp_text[11:19]

    if not is_valid_time_text(time_text):
        return None

    # Time has already been validated manually.
    # The prompt says all dates themselves are real.
    stamp = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")

    return [stamp, level, message]


def parse_logs(log_text):
    entries = []

    for line in log_text.splitlines():
        entry = parse_log_line(line)

        if entry is not None:
            entries.append(entry)

    return entries


def format_gap(total_seconds):
    """Convert seconds to the required format: 1h 02m 03s."""
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return f"{hours}h {minutes:02d}m {seconds:02d}s"


def find_level_index(levels, level):
    """Return matching level index, or -1 when not found."""
    for i in range(len(levels)):
        if levels[i] == level:
            return i

    return -1


def level_longest_gaps(entries):
    """
    Return parallel lists:
    - levels: levels in first-appearance order from chronological entries
    - largest_gaps: largest gap in seconds, or None for only one entry
    """
    levels = []
    previous_times = []
    largest_gaps = []
    occurrences = []

    for entry in entries:
        stamp = entry[0]
        level = entry[1]

        index = find_level_index(levels, level)

        if index == -1:
            levels.append(level)
            previous_times.append(stamp)
            largest_gaps.append(None)
            occurrences.append(1)
        else:
            gap_seconds = int((stamp - previous_times[index]).total_seconds())

            if largest_gaps[index] is None or gap_seconds > largest_gaps[index]:
                largest_gaps[index] = gap_seconds

            previous_times[index] = stamp
            occurrences[index] += 1

    return levels, largest_gaps, occurrences


def minute_with_most_entries(entries):
    """
    Return the minute string with the most entries and its count.
    On a count tie, return the earliest minute.
    """
    minutes = []
    minute_counts = []

    for entry in entries:
        minute_text = entry[0].strftime("%Y-%m-%d %H:%M")

        found_index = -1

        for i in range(len(minutes)):
            if minutes[i] == minute_text:
                found_index = i
                break

        if found_index == -1:
            minutes.append(minute_text)
            minute_counts.append(1)
        else:
            minute_counts[found_index] += 1

    if not minutes:
        return None, 0

    best_index = 0

    for i in range(1, len(minutes)):
        if minute_counts[i] > minute_counts[best_index]:
            best_index = i

        elif minute_counts[i] == minute_counts[best_index]:
            if minutes[i] < minutes[best_index]:
                best_index = i

    return minutes[best_index], minute_counts[best_index]


def print_entries_table(entries):
    print(f"{'Timestamp':<19} {'Level':<8} {'Message':<20}")
    print("-" * 50)

    for entry in entries:
        stamp = entry[0].strftime("%Y-%m-%d %H:%M:%S")
        level = entry[1]
        message = entry[2]

        print(f"{stamp:<19} {level:<8} {message:<20}")


def print_gap_table(levels, largest_gaps, occurrences):
    print()
    print(f"{'Level':<8} {'Entries':>12} {'Longest gap':>12}")
    print("-" * 36)

    for i in range(len(levels)):
        if occurrences[i] == 1:
            gap_text = "n/a"
        else:
            gap_text = format_gap(largest_gaps[i])

        print(f"{levels[i]:<8} {occurrences[i]:>12} {gap_text:>12}")


def analyze_logs(log_text):
    entries = parse_logs(log_text)

    # Python's list.sort() is stable: entries with identical timestamps
    # retain their original input order.
    entries.sort(key=lambda entry: entry[0])

    print("Chronological log entries")
    print_entries_table(entries)

    levels, largest_gaps, occurrences = level_longest_gaps(entries)

    print()
    print("Longest gaps by level")
    print_gap_table(levels, largest_gaps, occurrences)

    best_minute, count = minute_with_most_entries(entries)

    print()
    if best_minute is None:
        print("Busiest minute: n/a")
    else:
        print(f"Busiest minute: {best_minute} ({count} entries)")


analyze_logs(logs)
