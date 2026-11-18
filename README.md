# SLA Calculator

A command-line tool that reports whether a support ticket is within its
first-response deadline.

A support agent enters the ticket's ID, priority, age in hours, and whether a
first response has been sent. The program validates the input and returns one
of four statuses.

## Rules

| Priority | First-response target |
|----------|-----------------------|
| High     | 1 hour                |
| Medium   | 4 hours               |
| Low      | 24 hours              |

| Status           | Condition                                           |
|------------------|-----------------------------------------------------|
| No action needed | A first response has already been sent              |
| BREACHED         | Hours open exceed the target                        |
| AT RISK          | Hours open are at least 80% of the target           |
| ON TRACK         | Hours open are below 80% of the target              |

A ticket at exactly its target is AT RISK with 0 hours remaining, because the
target has been reached but not exceeded.

## Input validation

- Ticket ID: must start with `TCK-` followed by digits. Case and surrounding
  spaces are ignored.
- Priority: `high`, `medium` or `low`, in any case.
- Hours: zero or greater. Decimals are accepted.
- Responded: `yes` or `no`, in any case.

Each invalid input produces its own message stating what is wrong.

## Requirements

Python 3.10 or later. No third-party packages.

## Usage

```bash
python SLA_calculator.py
```

Example:

```
Enter the ticket ID: TCK-00123
What is the ticket priority? HIGH
Enter hours since the ticket was opened: 0.5
Has a first reponse been sent yet? Yes
Ticket TCK-00123: No action needed. A first response was sent.
```

## Tests

Tested manually against the cases below. Expected results were written before
each run.

#  Ticket ID            Priority       Hours        Responded      Expected output                   Actual output      Pass
1. tck-00123            high            2           no              BREACHED by 1 hour                Same              Yes    
2. Tck-00123            medium          3           no              ON TRACK  remaining 1 hour        Same              Yes 
3. TCK-ABC              low             10          no              must have digits only after TCK-  Same              Yes    
4. TCK-00123            urgent          0.5         no              must be high, medium or low       Same              Yes
5.  TCK-00123           low             12          no              ON TRACK  remaining 12 hours      Same              Yes
6.  ABC-1               high            1           no              ID must start with TCK-           Same              Yes
7. TCK-00123            medium          -4          no              No negative hours                 Same              Yes
8. TCK-00123            high            4           no              BREACHED by 3 hours               Same              Yes
8. TCK-00123            medium          3.5         no              AT RISk remaining 0.5 hour        Same              Yes
9. TCK-00123            medium          2           no              ON TRACK  remaining 2 hours       Same              Yes
10.                     low             18          no              cannot be empty                   Same              Yes
11. TCK-00123           medium          3.1         no              ON TRACK remaining 0.9 hours      Same              Yes
12. TCK-00123           medium          3.2         no              AT RISK remaining 0.8 hours       Same              Yes
13. TCK-00123           medium          4           no              AT RISK remaining 0 hour          Same              Yes
14. TCK-00123           medium          4.1         no              BREACHED by 0.1 hour              Same              Yes
15. TCK-00123           high            0           no              ON TRACK  remaining 1 hour        Same              Yes
16. TCK-00123           medium          6           yes             no action needed                  Same              Yes
17. TCK-00123           HIGH            0.5         Yes             no action needed                  Same              Yes
18. TCK-00123           low             5           maybe           must be yes or no                 Same              Yes

## Known limitations

- Non-numeric input for hours (for example `four`) stops the program with a
  `ValueError`. Error handling is planned for a later version.
- Handles one ticket per run.
- Targets are fixed in the code and count calendar hours, not business hours.
- A ticket that received its first response after the deadline is reported as
  "No action needed"; the time of the response is not recorded.

## Design decisions

See [DECISIONS.md](DECISIONS.md).

## Author

Ezekiel Oluwabamise Jude; https://github.com/settings/profile