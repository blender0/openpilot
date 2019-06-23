[![](https://i.imgur.com/xY2gdHv.png)](#)

Welcome to openpilot by Emmertex
https://www.youtube.com/ku7tech
======

Please support my work by becoming a [Patreon](https://www.patreon.com/ku7)
Or donating via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=9P9NFMAFZR5XE&source=url)


What is special about this port?
------

It's unfettered awesome with no corporate fears!
Where non standard features were made by someone other than me @ku7, they are credited with there Slack Username

Based on OpenPilot 0.5.12 from comma.ai

- Auto-Support almost all Hyundai/Kia/Genesis --- NO FINGERPRINTS!!!
- - If it doesn't work, hit me up on discord, theres no need for fingerprints, don't stress!
- Branch Switching from UI (Thanks @pjlao307 from community-pilot)
- Do not disable when Accelerator is depressed (MAD button*)
- - Off means only enabled when cruise is set, and disables on pedals.
- - LKAS means it enables and disables based on LKAS Kick Panel Button (EXPERIMENTAL, thanks @xx979xx)
- - CRUISE means it enables and disables based on cruise state
- Disable auto-steering on blinker, but leave OP engaged
- - Disabled on first blink, and stays disabled until 1 second of no blinking.
- Sounds! (Thanks Sid and @BogGyver and #Tesla in general) (SND button*)
- Tesla UI (Thanks everyone in #Tesla)
- - 3 Switch positions change the display, you probably want it far left. (OnePlus Only)
- Advanced Lane Change Assist (Thanks @BogGyver) (ALCA button*) (EXPERIMENTAL)
- - And with Blind Spot Detection for any Kia/Hyundai with it
- Panda auto-detects Camera Pinout
- - And now so does OP!  LKAS on CAN 2 or CAN 3, it doesn't matter!
- No need for giraffe switches, If no EON, then forwards stock camera (Thanks @JamesT-1)
- Dashcam Recorder (Thanks @pjlao307)
- Full Time Stock LKAS passthrough*
- - Including High Beam Assist and Automatic Emergency Braking, Blind Spot, Traffic Sign Detection, and more.
- - This includes Land Departure Warning, but stock LKAS must be enabled for this.
- Optional Dynamic Stock and OP Steering.  The moment OP isn't steering, it switched back to Stock (LKAS button*)*
- Cruise Setpoint set from OSM Speed Limit
- - With Slow Down before speed limites
- - and NO slow down in corners!!
- Compress when not uploading
- Automatically detects CAN Specifics (checksum, SCC, so on)
- Probably other things I have forgotten

* Has known issues

Known issues
------

- ALCA (Advanced Lane Change Assist) is not properly tuned.  Use with caution
- CAM (Stock LKAS Forwarding) occasionally silenetly faults, turning off stock LKAS

Licensing
------

openpilot is released under the MIT license. Some parts of the software are released under other licenses as specified.

Any user of this software shall indemnify and hold harmless Comma.ai, Inc. and its directors, officers, employees, agents, stockholders, affiliates, subcontractors and customers from and against all allegations, claims, actions, suits, demands, damages, liabilities, obligations, losses, settlements, judgments, costs and expenses (including without limitation attorneys’ fees and costs) which arise out of, relate to or result from any use of this software by user.

**THIS IS ALPHA QUALITY SOFTWARE FOR RESEARCH PURPOSES ONLY. THIS IS NOT A PRODUCT.
YOU ARE RESPONSIBLE FOR COMPLYING WITH LOCAL LAWS AND REGULATIONS.
NO WARRANTY EXPRESSED OR IMPLIED.**

---

<img src="https://d1qb2nb5cznatu.cloudfront.net/startups/i/1061157-bc7e9bf3b246ece7322e6ffe653f6af8-medium_jpg.jpg?buster=1458363130" width="75"></img> <img src="https://cdn-images-1.medium.com/max/1600/1*C87EjxGeMPrkTuVRVWVg4w.png" width="225"></img>