# Webhhooks

Just a simple webhook server for my own purposes.

Currently only supports GitHub webhooks.

Executes `scripts/<repo_name>.sh` script when a push event is received.

## Configuration

```
PORT=5000
GITHUB_SECRET=<webhook secret>
SCRIPTS_DIR=./scripts
```

## Usage

```
./run.sh
```

`run.sh` starts a `waitress` WSGI server serving the Flask app from `hooks.py`. Check the script contents for details.
