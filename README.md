# VoteStream

A desktop-based electronic voting prototype built with Python, Tkinter, sockets, and CSV-backed storage.  
VoteStream provides separate admin and voter flows, secure one-time voting checks, and real-time vote tally updates through a client-server architecture.

## Overview

VoteStream demonstrates how a lightweight election system can be structured with:
- a **GUI layer** for admin and voter operations,
- a **socket server** for vote-session handling,
- and a **data layer** using CSV files for voter records and candidate counts.

It is designed as an educational project for understanding voting workflows, state management, and concurrent request handling in Python.

## Key Features

- **Role-based flow**:
  - Admin login and control panel
  - Voter login and ballot casting
- **Voter registration** with auto-generated voter IDs.
- **One-person-one-vote enforcement** using `hasVoted` checks.
- **Candidate-based ballot UI** with party symbols and NOTA option.
- **Threaded socket server** to handle multiple voting clients.
- **Live vote count display** in admin panel.

## Architecture

- `homePage.py` - entry point for navigation between admin and voter modules.
- `Admin.py` - admin authentication and admin dashboard actions.
- `registerVoter.py` - voter enrollment form and registration logic.
- `voter.py` - voter authentication and server communication.
- `VotingPage.py` - ballot interface and vote submission.
- `Server.py` - threaded TCP voting server.
- `dframe.py` - CSV database operations (verify, eligibility, vote updates, results).
- `admFunc.py` - admin utilities like vote count display.
- `database/voterList.csv` - voter registry and vote status.
- `database/cand_list.csv` - candidate list and vote counts.
- `img/` - party/candidate symbol assets used in the ballot UI.

## Tech Stack

- **Language:** Python
- **GUI:** Tkinter
- **Networking:** Python socket programming
- **Storage:** Pandas + CSV files
- **Imaging:** Pillow (PIL)
- **Concurrency:** Python threading

## How It Works

1. **Admin starts the server** from the admin panel (`Run Server`).
2. **Voter logs in** using voter ID and password.
3. Server validates:
   - voter credentials,
   - vote eligibility (`hasVoted == 0`).
4. Voter selects a party/NOTA in the voting page.
5. Server updates:
   - candidate vote count,
   - voter `hasVoted` flag.
6. Admin can open **Show Votes** to view latest tallies.

## Setup and Run

### 1) Install dependencies

```bash
pip install pandas pillow
```

### 2) Start the application

```bash
python homePage.py
```

### 3) Typical run sequence

- Open **Admin Login** from Home.
- Login with default admin credentials:
  - **ID:** `Admin`
  - **Password:** `admin`
- Click **Run Server**.
- Register voters using **Register Voter**.
- Open voter flow from Home and cast votes.
- Use **Show Votes** in admin panel to monitor counts.

## Data Files

- `database/voterList.csv`
  - `voter_id`, `Name`, `Gender`, `Zone`, `City`, `Passw`, `hasVoted`
- `database/cand_list.csv`
  - `Sign`, `Name`, `Vote Count`

## Notes

- This project is a **prototype for academic/learning use**, not a production-grade election platform.
- Current authentication and storage are basic; production use would require encrypted credentials, robust database design, audit logs, and hardened security controls.

## Future Improvements

- Replace CSV with SQL/NoSQL database.
- Add password hashing and secure authentication.
- Introduce voter OTP / identity verification.
- Add tamper-evident audit logs and vote receipts.
- Package as a cross-platform executable.
