---
hide:
  - toc
---

# 📲 Expo: emulate your app

### Step 1: Create account on Expo

Access the Expo website and create an account on the platform. It is recommended that you create an account by entering your email and password and not by SSO login, this will make it easier when you login through the terminal with the command _**eas login**_.

**Website**: [https://expo.dev/signup](https://expo.dev/signup)

![Image title](../../files/image (24).png)

### Step 2: Install and Login EAS CLI

1. Open a terminal.
2.  Install EAS CLI globally using npm:

    ```bash
    npm install --global eas-cli
    ```
3.  Log in to your Expo account with EAS CLI:

    ```bash
    eas login
    ```

![Image title](../../files/image (23).png)

### Step 2: Request access to organization

In order for you to be able to build and make the app available to be viewed on your cell phone, you need to request access to the organization. Ask one of the admins to add you.

Path: [https://expo.dev/accounts/mercado-topografico/settings/members](https://expo.dev/accounts/mercado-topografico/settings/members)

![Image title](../../files/image (28).png)

![Image title](../../files/image (29).png)

### Step 3: Starting your project

In your **project directory**, run the command:

```bash
npx expo start --tunnel
```

After that press "**a**" to open Android Emulator:

![Image title](../../files/image (26).png)

Or you can run the following command which also works:

```bash
npm run android  
```

![Image title](../../files/image (27).png)
