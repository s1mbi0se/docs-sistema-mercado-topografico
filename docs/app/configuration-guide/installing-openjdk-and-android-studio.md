---
hide:
  - toc
---

# 💻 Installing OpenJDK and Android Studio

### Installing OpenJDK on Ubuntu 22.04

#### Step 1: Install OpenJDK

If you don't have OpenJDK installed on your Ubuntu 22.04 system, you can do so by following these steps:

1. Open a terminal.
2.  Run the following command to install OpenJDK 11:

    <pre class="language-bash"><code class="lang-bash"><strong>sudo apt install openjdk-11-jdk 
    </strong></code></pre>
3. During the installation process, you might be asked whether you want to continue or not. Press 'Y' to continue.

#### Step 2: Verify Installation

After the installation, you can verify that OpenJDK was successfully installed by running the following command:

<pre class="language-bash"><code class="lang-bash"><strong>java --version
</strong></code></pre>

![Image title](../../files/image (17).png)

You should see the version information of the installed OpenJDK, confirming that the installation was successful.

### Installing Android Studio on Ubuntu 22.04

#### Step 3: Add Android Studio Repository

With OpenJDK installed, you can now add the android-studio repository by running the following command:

```bash
sudo add-apt-repository ppa:maarten-fonville/android-studio
```

#### Step 4: Update System

Before you proceed with installing Android Studio, make sure to update your system by running:

```bash
sudo apt update
```

#### Step 5: Install Android Studio

After updating your system, you can install Android Studio with the following command:

```bash
sudo apt install android-studio -y
```

This will install Android Studio on your Ubuntu 22.04 system.

![Image title](../../files/image (18).png)

#### Step 6: Usage

Once the installation is complete, you can find Android Studio in the menu. Click on it to launch the application and start developing your Android applications.

***

### Recommendations for Windows and macOS Users

For Windows and macOS users, follow these recommendations:

#### Windows Users:

1. Download the Android Studio installer from the [official website](https://developer.android.com/studio).
2. Run the installer and follow the on-screen instructions to install Android Studio.
3. During installation, you'll have the option to choose the JDK version. You can select the bundled JDK or specify your own.

#### macOS Users:

1. Download the Android Studio DMG file from the [official website](https://developer.android.com/studio).
2. Open the DMG file and drag Android Studio into the Applications folder.
3. Run Android Studio from the Applications folder. It will automatically use the JDK bundled with Android Studio.

Remember to refer to the official Android Studio documentation for more detailed installation and setup instructions based on your operating system.

***

### Configure **the ANDROID\_HOME environment variable**

The React Native tools require some environment variables to be set up in order to build apps with native code.

Add the following lines to your `$HOME/.bash_profile` or `$HOME/.bashrc`&#x20;

if you are using `zsh` then `~/.zprofile` or `~/.zshrc`) config file:

![](<../../files/image (19).png>)![](<../../files/image (20).png>)

```
export ANDROID_HOME=$HOME/Android/Sdk
export PATH=$PATH:$ANDROID_HOME/emulator
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

![Image title](../../files/image%20(21).png)

Reference: [https://reactnative.dev/docs/next/environment-setup?guide=native#android-sdk](https://reactnative.dev/docs/next/environment-setup?guide=native#android-sdk)

