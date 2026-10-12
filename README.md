# COVID-19 Vaccine Management System

A Django web app for registering people for COVID-19 vaccination, assigning vaccines and appointments, and issuing vaccination certificates. Built for **CSE370 Database Systems** at BRAC University (2021).

## Features

- Account sign-up, login and logout
- Vaccine registration with name, address, mobile, national ID (unique) and preferred vaccine
- Admin assignment of vaccine, appointment and vaccinated status (Django admin)
- Edit and delete registrations, with a confirmation page for deletes
- Printable vaccination certificate page
- Notice board for announcements

## Data model

| Model | Key fields |
|---|---|
| `VaccineRegistration` | `name`, `address`, `mobile`, `nid` (unique), `p_vac` (preferred), `a_vac` (assigned), `appointment`, `vaced` |
| `Notices` | announcements shown on the profile page |

The original project ran on **MySQL**. It now defaults to **SQLite** so it runs with no setup; set `DB_ENGINE=mysql` to use MySQL again.

## Run it locally

```bash
cd vacmanagement
python -m venv .venv && source .venv/bin/activate
pip install -r ../requirements.txt
python manage.py migrate
python manage.py createsuperuser   # for the admin site
python manage.py runserver
```

Open http://127.0.0.1:8000/signup/ to create an account.

### Configuration (environment variables)

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_SECRET_KEY` | dev-only placeholder | **Set this for any real deployment** |
| `DJANGO_DEBUG` | `1` | Set to `0` in production |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated hosts |
| `DB_ENGINE` | SQLite | `mysql` to use `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` |

## Tests

```bash
cd vacmanagement
python manage.py test covapp
```

Covers sign-up and login, the logout route, login protection, the register, edit, certificate and delete flow, duplicate national-ID rejection, and 404s for missing records.

## Maintenance notes (2026)

- Moved the secret key and database settings into environment variables, and removed the committed SQLite database
- Fixed the logout route (it was registered as `logout/,`)
- Pages that show or change registrations now require login, and missing records return 404 instead of a server error
- Added a test suite, `requirements.txt` and `.gitignore`

**Known limitation:** registrations aren't linked to user accounts, so any logged-in user can see all of them. A production version would add an owner field and restrict access per user.

## Tech

Python · Django · SQLite / MySQL · HTML templates
