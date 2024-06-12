---
cover: https://faraitltd.com/wp-content/uploads/2023/02/Screenshot_7.jpg
coverY: 0
---

# 📢 Develop, Build and Visualize

### Simulate Production Environment

Constantly simulating your code in the production environment is a best practice to avoid future problems. For each considerable change you make, remember to run the following command:

```bash
npx expo start --no-dev
```

### Deploy on Stage

If you have made any modifications to the Rails backend, send it to the stage environment, following the step-by-step instructions in this documentation:

!!! info
    Your development branch must be on Github

{% embed url="https://docs.google.com/document/d/1SJv4iTv6kn44ACNgzLX-96WZQy8zKWAr-JR6evh-rDI/edit" %}
DEPLOY ON DEVELOPMENT / PRODUCTION
{% endembed %}

### Pull Request

Everything ok with the test, make a pull request to the **Develop branch** with your changes and add reviewers.

![Image title](../../files/image (12).png)

### Building the App

To build the app, run the following command:

```bash
eas build
```

Select platform: Android, IOS or All. And wait for it to be completed:

![Image title](../../files/image (30).png)

### Publish on Expo

After building your app, publish it to Expo with changes from the **Develop** branch:

```bash
eas update --branch develop
```

![Image title](../../files/image (16).png)

You can also follow the application build through the Expo website:

![Image title](../../files/image (13).png)

![Image title](../../files/image (14).png)

### Share the Updates

Now that your app is on Expo, you can share the QRCode or access link to anyone who has the Expo Go app installed on their cell phone.

![Image title](../../files/image (15).png)

![Image title](../../files/image (10).png)

![Image title](../../files/image (11).png)
