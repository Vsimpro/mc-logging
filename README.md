# Minecraft server log parser

### Tool I am working on to make better use of Minecraft servers logging system.
  - Creates .json for api usage
  - Forwards server `WARN`'s and `/say` into Discord via Webhooks.

#### To run:
Tweak config.json;
```c
{
    "interval": Integer to represent interval of the loop,
    "path_to_log": Path of the "latest.log" file of your server,
    "webhook": Url of your Discord webhook,
    "path_to_output": Path to where you want your .json to appear.
}
```
After configuration, run `Python3 run.py`
