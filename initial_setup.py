import json

from subprocess import run

if __name__ == "__main__":
    # List of currency codes supported by both
    # Streamlabs' and CoinGecko's APIs
    supported_currencies = [
        "aud", "brl", "cad", "czk", "dkk", "eur",
        "hkd", "ils", "inr", "jpy", "myr", "mxn",
        "nok", "nzd", "php", "pln", "gbp", "rub",
        "sgd", "sek", "chf", "thb", "try", "usd",
    ]
    input_string = "Enter the three-letter code of the currency you use " \
                   "for Streamlabs donations: "
    while (fiat := input(input_string).lower()) not in supported_currencies:
        input_string = "Your currency is either not supported, or " \
                       "you had a typo. Please try again: "
    with open('settings.json', 'w') as settings_file:
        settings = {"fiat": fiat}
        json.dump(settings, settings_file, indent=4)
    print("Now installing LNbits...\n")
    run('. ./install_lnbits.sh', shell=True)
    print("\nAll done! Please continue to the next step in the guide!")
