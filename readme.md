# Banks-Rest-Api
Django Rest Api for Accessing Bank Details based on IFSC Code , Bank name or City name

## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ python -m venv venv
$ . venv/bin/activate
$ git clone https://github.com/goyal-aman/Bank-Rest-Api.git
$ cd Banks-Rest-Api
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Get Branch Details using IFSC CODE : `<local_ip>/api/ifsc/`**`<ifsc_code>`**

* Get all branches using CITY and BANK : `<local_ip>/api/branch/` **`<bank_name>`/`<city_name>`**
* Enter Ifsc code, bank name and city name in place of `<ifsc_code>` , `<bank_name>`, `<city_name>`

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
