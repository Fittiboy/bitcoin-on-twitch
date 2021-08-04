if __name__ == "__main__":
    with open("./lnbits/.env") as env_file:
        env = {}
        for line in env_file.readlines():
            if "=" in line:
                key, value = line.split("=", 1)
                env[key] = value
    user = input("Input your user ID: ")
    allowed_users = env['LNBITS_ALLOWED_USERS'].strip('"\n')
    if not allowed_users:
        env['LNBITS_ALLOWED_USERS'] = f'"{user}"\n'
    else:
        env['LNBITS_ALLOWED_USERS'] = f'"{allowed_users},{user}"\n'
    with open("./lnbits/.env", "w") as env_file:
        for key, value in env.items():
            env_file.write(f'{key}={value}')

    print("User added to LNBITS_ALLOWED_USERS!")
