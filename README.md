## Support the project
You can tip me with some sats [here](https://fitti.io/tips)!  
This is, and always will be, entirely free to use of course!

# Rough test setup guide
This is currently intended for testing only.  
You need to have git, python, and it's virtualenv module installed.
1. Clone the repo and `cd` into it
1. Create and enable a virtualenv
1. In the venv, run `pip install -r requirements.txt`
1. [Get an lntxbot wallet](https://t.me/lntxbot)
1. Get an API key from lntxbot by messageing it `/api full`
1. Log in to https://streamlabs.com/
1. [Register an App](https://streamlabs.com/dashboard#/apps/register)  
     As this is an app just for you, you can fill the name, description  
     phone, and email fields with whatever you want. They are not relevant.  
     In the "Whitelist Users" field, enter your Twitch username.  
     In "Redirect URI", enter "http://localhost:6969".  
1. After hitting "Create", leave this page open for now, as it contains  
     your Client ID and Secret, which you will need in the next step  
1. Run `python initial_setup.py` and follow the instructions (enter `localhost` as the IP for now)
1. Run `python wait_for_token.py` and leave this running
1. On the Streamlabs App page, click the link that says "Sample Authentication URL"  
     towards the bottom of the page
1. Click "Approve"; this should redirect you to a plain text page that tells you to stop the server
1. Go back to the terminal that is running `wait_for_token.py`,  
     and hit ctrl+c to stop the server
1. You should now be able to run `. ./start_lnbits.sh`, which should launch  
     LNbits in the background, making it reachable at http://localhost:5000/
1. Run `python webhook.py` and leave it running in the background
1. In LNbits, create a wallet, and enable the SatsPayServer extension under "Manage extensions"
1. In SatsPayServer, hit "NEW CHARGE," and fill out all the required fields
     In the "webhook" field, enter http://localhost:5001/
1. Pay the charge with any lightning wallet  

If everything worked, you should see a new donation pop up [here](https://streamlabs.com/dashboard#/donations) (remember to refresh).  
If something went wrong, please [submit an issue](https://github.com/Fittiboy/bitcoin-on-twitch/issues/new/choose)!

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
