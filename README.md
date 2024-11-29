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

## Service

There is an example systemd service file `webhooks.service`

The service assumes:

* You have an user and group `webhooks`
* The repository is cloned to `/src/webhooks`
* `/srv/webhooks` is owned by `webhooks:webhooks`

Modify the service file as needed.

** Create `webhooks` user as needed **

```
sudo useradd -r -s /usr/bin/nologin -d /nonexistent serviceuser
```

** Test beforehand **

Probably best to test the app first before deploying the service by manually executing `run.sh` as the `webhooks` user.

** Deploy the service **

```
sudo cp webhooks.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now webhooks
```

Check the status

```
sudo systemctl status webhooks
```
