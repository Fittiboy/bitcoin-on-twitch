#### [Support the project here](https://fitti.io/tips)! Since this is all free to use, I will gladly accept any donations you're willing to throw my way! 

### Need help?
**If you have truly no idea how to do any of this, or you're having problems:  
fitti@btctwt.ch or (very cheap) [paid Bitcoin priority DMs](https://fitti.io/dm) (remember to include information for me to contact you back).**

# Bitcoin on Twitch
***Want to accept Bitcoin donations on Twitch?*** This will allow you to not only accept Bitcoin, but also have those donations show up in your Streamlabs alerts!
And the best part: While it supports on-chain payments, it's [lightning](https://youtu.be/XCSfoiD8wUA)-first!  
To enable this, [LNbits](https://github.com/lnbits/lnbits) is utilized, for which I wrote a special extension.  
*It's open source all the ways down!*

### The system in action
Check out [how seamlessly the project works](https://twitter.com/Fittiboy/status/1422287674048720898)!

## Setup Guide

For this to work, you need to have git, python, and its virtualenv module installed.  
This will only work on Linux, and should preferably run on an always-on machine.  
You *can* run this on Windows, using [WSL](https://duckduckgo.com/?q=how+to+install+wsl), and run it on your streaming PC while you're live.
When using ngrok, keep in mind that your URL will change every time you restart it.  
If you want to run it on Windows via WSL, I recommend installing [Ubuntu](https://ubuntu.com/wsl), and running `sudo apt update ; sudo apt upgrade ; sudo apt install python3-venv git`.  
1. Clone the repo and `cd` into it (`git clone https://github.com/Fittiboy/bitcoin-on-twitch ; cd bitcoin-on-twitch`)
1. [Get an lntxbot wallet](https://t.me/lntxbot).  
   If you have a different [backend](https://lnbits.org/guide/wallets.html) that you would like to use, you can just hit enter without typing anything when you are later asked for the lntxbot API key.  
   Keep in mind that you will have to manually set the backend in `lnbits/.env`, as explained [here](https://lnbits.org/guide/wallets.html)
1. Get an API key from lntxbot by messaging it `/api full`.
1. Run `python initial_setup.py` and follow the instructions.
   When it asks whether or not you want to use "ngrok," you have to make a decision:
   The ngrok extension in LNbits will allow you to host it publicly and for free.  
   You can read the "How it works" section [here](https://github.com/Fittiboy/lnbits/blob/TwitchAlerts/lnbits/extensions/ngrok/README.md#how-it-works) for more information. If you want to use this, simply type "y" and hit enter, otherwise "n".  
   If you need help with web hosting, you can [send me an email](mailto:fitti@btctwt.ch) at fitti@btctwt.ch! I might be able to help you out.
1. You should now be able to run `. ./start_lnbits.sh`, which should launch  
   LNbits in the background, making it reachable at http://localhost:5000/  
   Issues will be recorded in a file called `lnbits.log`
1. In LNbits, create a wallet.  
   This should bring you to a url that ends in this format : `/wallet?usr=XXXXXXXXXX&wal=YYYYYYYYYYYYY`.  
   Keep the XXXX and YYYY (yours will look like random text and numbers) secret, but copy the **FULL URL** somewhere safe.  
   Visiting this URL is essentially how you log in to LNbits, and so anyone who knows this URL, or the XXXX and YYYY could access your wallet.  
   For added security, you can move your funds to a different wallet after every stream!     
1. Follow the [extension guide](https://github.com/Fittiboy/lnbits/blob/TwitchAlerts/lnbits/extensions/streamalerts/README.md).
1. When you publicly host this, go ahead and open your wallet through your public URL (for example, the URL shown in the ngrok extension).  
   To access your wallet on this public URL, simply add the `/wallet?usr=XXXXXXXXXX&wal=YYYYYYYYYYYYY` part from the URL you saved.  
   Then, navigate to the Stream Alerts extension again and there you can get the donation page link, as described in the guide in the previous step.

You can try sending yourself a test donation afterwards.  
If everything worked, you should see the donation pop up [here](https://streamlabs.com/dashboard#/donations) (remember to refresh).  
If something went wrong, please [submit an issue](https://github.com/Fittiboy/bitcoin-on-twitch/issues/new/choose) or [send me an email](mailto:fitti@btctwt.ch) at fitti@btctwt.ch!  

To stop LNbits (and ngrok if it's running), run `. ./kill_lnbits.sh`, but be aware that this will kill all processes that have "lnbits" and "ngrok" in their name.
If for whatever reason you have other processes running that have those names in them, kill LNbits (and potentially ngrok) manually.

# Streamers who use this
### Feel free to add yourself or others to this list via Pull Request!
[Fitti](https://twitch.tv/Fitti), donate [here](https://fitti.io/twitch) - _Variety gaming streamer (and also the guy who made this)_

## Contributing
I want this to be a project that allows streamers on Twitch to integrate Bitcoin donations  
into their on-stream alerts with as little setup as possible.  
Things you can help with:  
* Clarifying steps in the guide, or linking to/writing more detailed guides to get non-technical users up to speed
* Writing scripts that would make this run on Windows (in case a streamer opts for self-hosting on Windows)

I'm not at all used to maintaining projects with other contributors, so I don't know, just follow the  
common etiquette or whatever if you wanna help :)  
I would especially appreciate help with just making things cleaner and more efficient (I'm not a professional),  
as well as potentially integrating services other than Streamlabs (not sure if there are any  
that are widely used like Streamlabs and actually have an API for this).
