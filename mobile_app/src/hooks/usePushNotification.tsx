import React from "react";
import messaging from "@react-native-firebase/messaging";
import { PermissionsAndroid, Platform } from "react-native";
import { v4 as uuidv4 } from "uuid";

const usePushNotification = () => {
  const requestUserPermission = async () => {
    if (Platform.OS === "ios") {
      //Request iOS permission
      const authStatus = await messaging().requestPermission();
      const enabled =
        authStatus === messaging.AuthorizationStatus.AUTHORIZED ||
        authStatus === messaging.AuthorizationStatus.PROVISIONAL;

      if (enabled) {
        console.log("Authorization status:", authStatus);
      }
    } else if (Platform.OS === "android") {
      //Request Android permission (For API level 33+, for 32 or below is not required)
      const res = await PermissionsAndroid.request(
        PermissionsAndroid.PERMISSIONS.POST_NOTIFICATIONS
      );
    }
  };

  const getFCMToken = async () => {
    const fcmToken = await messaging().getToken();
    if (fcmToken) {
      console.log("Your Firebase Token is:", fcmToken);
    } else {
      console.log("Failed", "No token received");
    }

    await updateDeviceTokenAPI(fcmToken);
  };

  const updateDeviceTokenAPI = async (fcmToken: string) => {
    const alertsBasePath = process.env.REACT_APP_API_BASE_PATH;
    if (!alertsBasePath) {
      console.log("Skipping device token registration, API base path not found");
      return;
    }

    const apiUrl = `${alertsBasePath}/alerts/register-device`;
    await fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        user_id: uuidv4(),
        device_token: fcmToken,
        enabled: true
      })
    });
  };

  const listenToForegroundNotifications = async () => {
    const unsubscribe = messaging().onMessage(async remoteMessage => {
      console.log(
        "A new message arrived! (FOREGROUND)",
        JSON.stringify(remoteMessage)
      );
      console.log("Notification received at:", new Date().getTime())
    });
    return unsubscribe;
  };

  const listenToBackgroundNotifications = async () => {
    const unsubscribe = messaging().setBackgroundMessageHandler(
      async remoteMessage => {
        console.log(
          "A new message arrived! (BACKGROUND)",
          JSON.stringify(remoteMessage)
        );
        console.log("Notification received at:", new Date().getTime())
      }
    );
    return unsubscribe;
  };

  const onNotificationOpenedAppFromBackground = async () => {
    const unsubscribe = messaging().onNotificationOpenedApp(
      async remoteMessage => {
        console.log(
          "App opened from BACKGROUND by tapping notification:",
          JSON.stringify(remoteMessage)
        );
        console.log("Notification received at:", new Date().getTime())
      }
    );
    return unsubscribe;
  };

  const onNotificationOpenedAppFromQuit = async () => {
    const message = await messaging().getInitialNotification();

    if (message) {
      console.log("App opened from QUIT by tapping notification:", JSON.stringify(message));
      console.log("Notification received at:", new Date().getTime())
    }
  };

  return {
    requestUserPermission,
    getFCMToken,
    listenToForegroundNotifications,
    listenToBackgroundNotifications,
    onNotificationOpenedAppFromBackground,
    onNotificationOpenedAppFromQuit
  };
};

export default usePushNotification;
