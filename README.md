# dsfkit
[![Build Status](https://travis-ci.org/jamesridgway/dsfkit.svg?branch=master)](https://travis-ci.org/jamesridgway/dsfkit)

A suite of utilities for converting and working with data serialization formats

## CSV Tools

* **`csvjson`**

  Converts a CSV file to a JSON file.

      usage: csvjson [-h] [--sort] [--pretty] [CSV_FILE] [JSON_FILE]

      positional arguments:
        CSV_FILE    CSV file (if empty stdin is used)
        JSON_FILE   JSON file (if empty stdout is used)

      optional arguments:
        -h, --help  show this help message and exit
        --sort      Sort JSON output
        --pretty    Pretty print JSON output
