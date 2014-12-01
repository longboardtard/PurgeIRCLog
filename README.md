PurgeIRCLog
===========

A simple python class for purging IRC logs from unneeded messages that clutter your reading experience.

## Example usage

```
% python2
    import purgeirclog
    pil = purgeirclog.PurgeIRCLog()
    
    pil.log_path = "/home/foo/.irssi/irclogs/#python.log"
    pil.parse()
    pil.print_log()
    pil.store()

    pil.log_path = "/home/foo/.irssi/irclogs/##linux.log"
    pil.strip_nick_changes = True
    pil.parse()
    pil.store()

    pil.log_path = "/home/foo/.irssi/irclogs/#archlinux.log"
    pil.add_filter(troll_list)
    pil.parse()
    pil.store(path="/opt/purgedlogs")
```
