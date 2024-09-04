// ==UserScript==
// @name         Auto Login for XJTU WebVPN
// @namespace    https://webvpn.xjtu.edu.cn/
// @version      1.2
// @description  Automatically fills username and password and logs in on specific XJTU WebVPN pages
// @author       LyuFG
// @match        https://webvpn.xjtu.edu.cn/http*/*/openplatform/login.html
// @match        https://org.xjtu.edu.cn/*/login.html
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Define your username and password here
    var username = "学号";
    var password = "密码";

    // Wait for the DOM to be fully loaded
    window.addEventListener('load', function() {
        // Find the username and password input fields
        var usernameField = document.querySelector("input[name='username']");
        var passwordField = document.querySelector("input[name='pwd']");

        // Check if both fields exist
        if (usernameField && passwordField) {
            // Fill in the username and password
            usernameField.value = username;
            passwordField.value = password;

            // Find and click the login button
            var loginButton = document.querySelector("div#account_login");
            if (loginButton) {
                loginButton.click();
            }
        }
    });
})();
