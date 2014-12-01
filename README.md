PurgeIRCLog
===========

A simple python class for purging IRC logs from unneeded messages that clutter your reading experience.

## Example usage

```
% python2
    log_path = "/home/foo/.irssi/irclogs/#python.log"
    pil = purgeirclog.PurgeIRCLog()
    pil.log_path = log_path
    pil.parse()
    pil.print_log()
    pil.store()

    log_path = "/home/foo/.irssi/irclogs/##linux.log"
    pil.log_path = log_path
    pil.strip_nick_changes = True
    pil.parse()
    pil.store()

    log_path = "/home/foo/.irssi/irclogs/#archlinux.log"
    pil.log_path = log_path
    pil.add_filter(troll_list)
    pil.parse()
    pil.store("/opt/purgedlogs")
```
