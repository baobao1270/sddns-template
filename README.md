# SDDNS Config Template
The SDDNS repository is at https://github.com/baobao1270/sddns

## Installation
```bash
git clone https://github.com/baobao1270/sddns-template.git
cd sddns-template
python3 -m venv venv
source venv/bin/activate
pip install sddns
```

## Configuration
 1. Configure the OctoDNS in `octodns.yaml` file. See [OctoDNS Configuration](https://github.com/octodns/octodns) for more details.
 2. Write something in `conf.py`.
 3. Run `python3 conf.py`. The args will be passed to `octodns-sync` command.

Do not forget to pass `--doit` argument, or your configuration will not be applied.

Make sure you change the `LICENSE` file if you don't want to relicense your DNS records as MIT license!
