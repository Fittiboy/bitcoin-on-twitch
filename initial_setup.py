import json

from subprocess import run

if __name__ == "__main__":
    print("Now installing LNbits...\n")
    run('. ./install_lnbits.sh', shell=True)
    # Set the .env file for LNbits to use LNPay
    with open("./lnbits/.env") as env_file:
        env = {}
        for line in env_file.readlines():
            if "=" in line:
                key, value = line.split("=")
                env[key] = value
    api_key = input("\nPlease input the lntxbot API key: ")
    choices = ["y", "n"]
    while (remove := input("Use ngrok? (y/n) ").lower()) not in choices:
        print("Please type y or n!")
    if remove == "y":
        disabled = env['LNBITS_DISABLED_EXTENSIONS']
        env['LNBITS_DISABLED_EXTENSIONS'] = disabled.replace(",ngrok", "")
        run('. ./enable_ngrok.sh', shell=True)
    env['LNTXBOT_KEY'] = f'"{api_key}"\n'
    env['LNBITS_BACKEND_WALLET_CLASS'] = "LntxbotWallet\n"
    with open("./lnbits/.env", "w") as env_file:
        for key, value in env.items():
            env_file.write(f'{key}={value}')

    print("\nAll done! Please continue to the next step in the guide!")
