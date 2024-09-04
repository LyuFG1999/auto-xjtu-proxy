// ==UserScript==
// @name         Auto Click Login for XJTU WebVPN
// @namespace    https://webvpn.xjtu.edu.cn/
// @version      1.0
// @description  Automatically clicks the login button on the XJTU WebVPN login page
// @author       LyuFG
// @match        https://webvpn.xjtu.edu.cn/login
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    // Wait for the DOM to be fully loaded
    window.addEventListener('load', function() {
        // Find the login button
        var loginButton = document.querySelector("a#oauth-login.link-login");

        // Check if the login button exists
        if (loginButton) {
            // Click the login button
            loginButton.click();
        }
    });
})();
