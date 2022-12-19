import sys
from sddns import Config, TXTRecord, Zone, ARecord, CNAMERecord, MXRecord, CAARecord, CAAFlag

caa = [
    CAARecord("@", 0, flag, ca) for flag in [
        CAAFlag.Issue, CAAFlag.IssueWildcard
    ] for ca in [
        "letsencrypt.org", "sectigo.com", "digicert.com", "comodoca.com"
    ]
]

mailgun = [
    TXTRecord("@", "v=spf1 include:mailgun.org ~all"),
    MXRecord("@", "mxa.eu.mailgun.org", 10),
    MXRecord("@", "mxb.eu.mailgun.org", 10),
]

Config().add_zone(Zone("example.com")
    .add_records(caa)
    .add_records([ARecord("@", ip) for ip in [f"192.168.1.{x}" for x in range(1, 10)]])
).add_zone(Zone("example.net")
    .add_records(caa)
    .add_records([
        # Mailgun
        MXRecord("mail", "mxa.mailgun.org", 10),
        MXRecord("mail", "mxb.mailgun.org", 10),
        TXTRecord("mail", "v=spf1 include:mailgun.org ~all"),
        TXTRecord("email._domainkey", open("mail.example.net.dkim").read())
    ]).add_records([
        # Email routing, can not change
        MXRecord("mail", "route1.mx.cloudflare.net", 10),
        MXRecord("mail", "route2.mx.cloudflare.net", 20),
        MXRecord("mail", "route3.mx.cloudflare.net", 30),
        TXTRecord("mail", "v=spf1 include:_spf.mx.cloudflare.net ~all"),
        TXTRecord("_dmarc", "v=DMARC1; p=quarantine; rua=mailto:postmaster@example.net")
    ])
).add_zone(Zone("example.org")
    .add_records(caa)
).write_yaml("config").octodns("octodns.yaml", sys.argv)
