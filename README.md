# Rest-Assistant
Creating a custom rest interface for personal use with iOS Shortcuts
## Setup

### Security
Create a 'secret' file in the root of this directory. Add your authentication keys separated by newlines. (If no secret files is found the server will listen to all requests)
### Assistant
Setting up the google assistant REST service requires you to authorize the device to access your assistant through your own google account. Follow the steps below to enable this:
1. Go to the [Projects](https://console.cloud.google.com/project) page in the Google Cloud Platform Console.
2. Click on “Create Project” up top.
3. Name the Project “My Google Assistant” and click “Create.”
4. Wait a few seconds for the Console to create your new Project. You should see a spinning progress icon in the top right. After it is done creating your Project, you will be brought to your Project’s configuration page.
5. [Click this link](https://console.developers.google.com/apis/api/embeddedassistant.googleapis.com/overview) to go straight to the Google Assistant API page. Up top, click “Enable.”
6. Google will warn you that you need to create credentials to use this API. Click “Create credentials” in the top right. This will take you to a setup wizard page where Google helps you figure out what kind of credentials you need to use this API.
7. Under “where will you be calling the API from”, select “Other UI (e.g. Windows, CLI tool)“. For “what data will you be accessing” select the “User data” circle. Now tap “what credentials do I need?”
8. Google should recommend that you create an OAuth 2.0 client ID. Name the Client ID anything you want, for example, your name + Desktop. Once done picking a name, click “create client ID.”
9. Under “product name shown to users” enter “My Google Assistant.” Click continue.
10. Click “done.” There’s no need to click download here as we only need the client secret, which we will download next.
11. Now under the list of OAuth 2.0 client IDs, you should see the client ID you just made. All the way to the right, click on the download icon to download the client_secret_XXX.json file, where ‘XXX’ is your client ID. Save this file anywhere on your computer, ideally in a new folder called “googleassistant.”
12. Go to the [Activity controls page](https://myaccount.google.com/activitycontrols) for your Google account and make sure that “Web & App Activity”, “Location History”, “Device Information”, and “Voice & Audio Activity” are enabled. This is so Google Assistant can actually read you personalized information.

Source: https://www.xda-developers.com/how-to-get-google-assistant-on-your-windows-mac-or-linux-machine/

