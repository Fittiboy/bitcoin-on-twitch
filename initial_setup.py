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
    env['LNTXBOT_KEY'] = f'"{api_key}"\n'
    env['LNBITS_BACKEND_WALLET_CLASS'] = "LntxbotWallet\n"
    with open("./lnbits/.env", "w") as env_file:
        for key, value in env.items():
            env_file.write(f'{key}={value}')

    print("\nAll done! Please continue to the next step in the guide!")
